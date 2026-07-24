import spotipy
from spotipy.oauth2 import SpotifyOAuth
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
import time
 
# --- CREDENCIALES ---
CLIENT_ID = "tu_client_id_real_aqui"
CLIENT_SECRET = "tu_client_secret_real_aqui"
REDIRECT_URI = "https://www.google.com/"
 
SCOPES = (
    "user-library-read user-modify-playback-state user-read-playback-state "
    "playlist-read-private playlist-read-collaborative"
)
 
console = Console()
 
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPES
))
 
# ──────────────────────────────────────────
# UTILIDADES VISUALES
# ──────────────────────────────────────────
 
def mostrar_logo():
    console.print()
    console.print("[bold green]  ╔══════════════════════════════════════╗[/bold green]")
    console.print("[bold green]  ║[/bold green]  [bold white]🎵 SPOTIFY CLI PLAYER[/bold white]              [bold green]║[/bold green]")
    console.print("[bold green]  ║[/bold green]  [dim white]Controla tu música desde la terminal[/dim white]  [bold green]║[/bold green]")
    console.print("[bold green]  ╚══════════════════════════════════════╝[/bold green]")
    console.print()
 
 
def barra_volumen(vol_percent):
    """Convierte volumen 0-100 en una barra visual de 10 bloques."""
    bloques = round(vol_percent / 10)
    llenos  = "█" * bloques
    vacios  = "░" * (10 - bloques)
    return f"[bright_green]{llenos}[/bright_green][dim]{vacios}[/dim] {bloques}/10"
 
 
def obtener_estado_reproduccion(actual):
    """Construye el panel de reproducción actual (sin barra de avance dinámica)."""
    if not actual or not actual.get('item'):
        return Panel(
            "[yellow]⚠️  No hay ninguna canción activa.\n[dim]Abre Spotify en algún dispositivo para comenzar.[/dim][/yellow]",
            border_style="yellow",
            title="🎵 EN REPRODUCCIÓN"
        )
 
    track       = actual['item']
    album       = track.get('album', {})
    artistas    = ", ".join(a['name'] for a in track['artists'])
    nombre_album = album.get('name', '')
    estado      = "▶  Sonando" if actual['is_playing'] else "⏸  En pausa"
    estado_color = "bold green" if actual['is_playing'] else "bold yellow"
 
    duracion_ms = track['duration_ms']
    min_dur, seg_dur = divmod(duracion_ms // 1000, 60)
    duracion_str = f"{min_dur:02d}:{seg_dur:02d}"
 
    shuffle     = "🔀 ON" if actual.get('shuffle_state') else "🔀 OFF"
    repeat_map  = {"off": "🔁 OFF", "context": "🔁 Contexto", "track": "🔂 Canción"}
    repeat      = repeat_map.get(actual.get('repeat_state', 'off'), "")
 
    volumen     = actual.get('device', {}).get('volume_percent')
    vol_str     = barra_volumen(volumen) if volumen is not None else ""
 
    device_name = actual.get('device', {}).get('name', '')
 
    contenido = (
        f"[{estado_color}]{estado}[/{estado_color}]  [dim]{device_name}[/dim]\n"
        f"[bold white]{track['name']}[/bold white]\n"
        f"[cyan]{artistas}[/cyan]  [dim white]— {nombre_album}[/dim white]\n"
        f"[dim white]Duración: {duracion_str}[/dim white]\n\n"
        f"🔊 {vol_str}   [dim]{shuffle}   {repeat}[/dim]"
    )
    return Panel(contenido, border_style="green", title="🎵 EN REPRODUCCIÓN", padding=(0, 1))
 
 
# ──────────────────────────────────────────
# AJUSTE DE VOLUMEN (escala 0-10)
# ──────────────────────────────────────────
 
def ajustar_volumen():
    """Pide al usuario un nivel de 0 a 10 y aplica el volumen."""
    try:
        actual = sp.current_playback()
        vol_actual = actual.get('device', {}).get('volume_percent', 50) if actual else 50
        nivel_actual = round(vol_actual / 10)
 
        console.print(f"\n  Volumen actual: {barra_volumen(vol_actual)}")
        console.print("  [dim]Escala: 0 = silencio · 10 = máximo[/dim]\n")
 
        entrada = Prompt.ask(
            "  [bold yellow]Nuevo volumen (0-10)[/bold yellow]",
            default=str(nivel_actual)
        )
 
        if not entrada.isdigit():
            console.print("  [red]Valor no válido.[/red]")
            return
 
        nivel = int(entrada)
        if not 0 <= nivel <= 10:
            console.print("  [red]Ingresa un número entre 0 y 10.[/red]")
            return
 
        nuevo_vol = nivel * 10
        sp.volume(nuevo_vol)
        console.print(f"\n  🔊 Volumen ajustado a: {barra_volumen(nuevo_vol)}")
        time.sleep(1)
 
    except spotipy.SpotifyException as e:
        if "Premium" in str(e):
            console.print("\n[bold red]❌ Controlar el volumen requiere Spotify Premium.[/bold red]")
            time.sleep(1.5)
        else:
            console.print(f"\n[bold red]❌ Error:[/bold red] {e}")
            time.sleep(1.5)
    except Exception:
        console.print("\n[bold red]❌ Abre Spotify en tu dispositivo primero.[/bold red]")
        time.sleep(1.5)
 
 
# ──────────────────────────────────────────
# BÚSQUEDA
# ──────────────────────────────────────────
 
def buscar_cancion():
    query = Prompt.ask("\n[bold cyan]🔍 Nombre de la canción o artista[/bold cyan]")
    if not query.strip():
        return
 
    console.print(f"\n[dim]Buscando '{query}'...[/dim]")
    results = sp.search(q=query, limit=8, type='track')
    tracks  = results['tracks']['items']
 
    if not tracks:
        console.print("[bold red]No se encontraron resultados.[/bold red]")
        time.sleep(1.5)
        return
 
    table = Table(show_header=True, header_style="bold cyan", border_style="dim")
    table.add_column("N°",      style="dim", width=4)
    table.add_column("Canción", style="white")
    table.add_column("Artista", style="green")
    table.add_column("Álbum",   style="dim white")
    table.add_column("Dur.",    style="dim", justify="right")
 
    for idx, track in enumerate(tracks):
        m, s = divmod(track['duration_ms'] // 1000, 60)
        table.add_row(
            str(idx + 1),
            track['name'],
            track['artists'][0]['name'],
            track.get('album', {}).get('name', ''),
            f"{m}:{s:02d}"
        )
 
    console.print(table)
 
    seleccion = Prompt.ask("\n[bold yellow]Número para reproducir (ENTER para cancelar)[/bold yellow]", default="")
    if seleccion.isdigit() and 1 <= int(seleccion) <= len(tracks):
        elegido = tracks[int(seleccion) - 1]
        try:
            sp.start_playback(uris=[elegido['uri']])
            console.print(f"\n[bold green]▶  Reproduciendo:[/bold green] [bold white]{elegido['name']}[/bold white] — [cyan]{elegido['artists'][0]['name']}[/cyan]")
            time.sleep(1)
        except spotipy.SpotifyException as e:
            if "Premium" in str(e):
                console.print("\n[bold red]❌ Esta función requiere Spotify Premium.[/bold red]")
                time.sleep(1.5)
            else:
                console.print("\n[bold red]❌ Error:[/bold red] Abre Spotify en tu dispositivo primero.")
                time.sleep(1.5)
 
 
# ──────────────────────────────────────────
# MENÚ PRINCIPAL
# ──────────────────────────────────────────
 
def ejecutar_accion(opcion):
    try:
        if opcion == "1":
            buscar_cancion()
        elif opcion == "2":
            actual = sp.current_playback()
            if actual and actual['is_playing']:
                sp.pause_playback()
            else:
                sp.start_playback()
            time.sleep(0.5)
        elif opcion == "3":
            ajustar_volumen()
 
    except spotipy.SpotifyException as e:
        if "Premium" in str(e):
            console.print("\n[bold red]❌ Esta acción requiere Spotify Premium.[/bold red]")
            time.sleep(1.5)
        else:
            console.print(f"\n[bold red]❌ Error de Spotify:[/bold red] {e}")
            time.sleep(1.5)
    except Exception:
        console.print("\n[bold red]❌ Error:[/bold red] Asegúrate de tener Spotify abierto en algún dispositivo.")
        time.sleep(1.5)
 
 
def menu():
    while True:
        console.clear()
        mostrar_logo()
 
        try:
            actual = sp.current_playback()
            console.print(obtener_estado_reproduccion(actual))
        except Exception:
            pass
 
        console.print("\n[bold white]📝 MENÚ PRINCIPAL[/bold white]")
        console.print("─" * 42)
        console.print("[bold cyan]  [1][/bold cyan] 🔍 Buscar y reproducir canción")
        console.print("[bold green]  [2][/bold green] ⏯  Play / Pausa")
        console.print("[bold magenta]  [3][/bold magenta] 🔊 Ajustar volumen (0-10)")
        console.print("[bold red]  [4][/bold red] 🚪 Salir")
        console.print("─" * 42)
 
        opcion = Prompt.ask(
            "\n[bold yellow]Elige una opción[/bold yellow]",
            choices=["1", "2", "3", "4"]
        )
 
        if opcion == "4":
            console.print("\n[bold green]👋 ¡Hasta luego![/bold green]\n")
            break
 
        ejecutar_accion(opcion)
 
 
if __name__ == "__main__":
    menu()
