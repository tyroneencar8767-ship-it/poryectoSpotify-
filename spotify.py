import spotipy
from spotipy.oauth2 import SpotifyOAuth      # Clase que maneja el login OAuth con Spotify
from rich.console import Console             # Representa la "pantalla" de la terminal
from rich.panel import Panel                 # Dibuja recuadros con borde
from rich.table import Table                 # Dibuja tablas con columnas alineadas
from rich.prompt import Prompt               # Pide texto/opciones al usuario
import time                                  # Para pausas (time.sleep)

# --- CREDENCIALES ---
# --- NO SE AGREGO LAS CREDENCIALES DE 'SPOTIFY-FOR-DEVELOPERS' A ESTE REPOSITORIO POR MEDIDAS DE SEGURIDAD ---
CLIENT_ID = "tu_client_id_real_aqui"         # Identificador público de la app (Developer Dashboard)
CLIENT_SECRET = "tu_client_secret_real_aqui" # Clave privada de la app
REDIRECT_URI = "https://www.google.com/"     # Debe coincidir con la registrada en el Dashboard

# Permisos que el usuario debe autorizar la primera vez
SCOPES = (
    "user-library-read user-modify-playback-state user-read-playback-state "
    "playlist-read-private playlist-read-collaborative"
)

console = Console()  # Objeto para imprimir con estilo en la terminal

# Cliente principal: TODO el programa usa "sp" para hablar con la API de Spotify
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
    # Imprime el encabezado del programa (recuadro con título)
    console.print()
    console.print("[bold green]  ╔══════════════════════════════════════╗[/bold green]")
    console.print("[bold green]  ║[/bold green]  [bold white]🎵 SPOTIFY CLI PLAYER[/bold white]              [bold green]║[/bold green]")
    console.print("[bold green]  ║[/bold green]  [dim white]Controla tu música desde la terminal[/dim white]  [bold green]║[/bold green]")
    console.print("[bold green]  ╚══════════════════════════════════════╝[/bold green]")
    console.print()


def barra_volumen(vol_percent):
    """Convierte volumen 0-100 en una barra visual de 10 bloques."""
    bloques = round(vol_percent / 10)        # Escala 0-100 -> 0-10
    llenos  = "█" * bloques                  # Repite el bloque lleno "bloques" veces
    vacios  = "░" * (10 - bloques)           # Rellena el resto con bloques vacíos
    return f"[bright_green]{llenos}[/bright_green][dim]{vacios}[/dim] {bloques}/10"


def obtener_estado_reproduccion(actual):
    """Construye el panel de reproducción actual (sin barra de avance dinámica)."""
    # Si no hay datos o no hay canción activa, se muestra un aviso
    if not actual or not actual.get('item'):
        return Panel(
            "[yellow]⚠️  No hay ninguna canción activa.\n[dim]Abre Spotify en algún dispositivo para comenzar.[/dim][/yellow]",
            border_style="yellow",
            title="🎵 EN REPRODUCCIÓN"
        )

    track       = actual['item']                                  # Datos de la canción
    album       = track.get('album', {})
    artistas    = ", ".join(a['name'] for a in track['artists'])  # Une todos los artistas
    nombre_album = album.get('name', '')
    estado      = "▶  Sonando" if actual['is_playing'] else "⏸  En pausa"
    estado_color = "bold green" if actual['is_playing'] else "bold yellow"

    duracion_ms = track['duration_ms']
    min_dur, seg_dur = divmod(duracion_ms // 1000, 60)   # ms -> minutos y segundos
    duracion_str = f"{min_dur:02d}:{seg_dur:02d}"

    volumen     = actual.get('device', {}).get('volume_percent')
    vol_str     = barra_volumen(volumen) if volumen is not None else ""  # Reusa la función de arriba

    device_name = actual.get('device', {}).get('name', '')

    # Arma el texto final del panel, línea por línea
    contenido = (
        f"[{estado_color}]{estado}[/{estado_color}]  [dim]{device_name}[/dim]\n"
        f"[bold white]{track['name']}[/bold white]\n"
        f"[cyan]{artistas}[/cyan]  [dim white]— {nombre_album}[/dim white]\n"
        f"[dim white]Duración: {duracion_str}[/dim white]\n\n"
        f"🔊 {vol_str}"
    )
    return Panel(contenido, border_style="green", title="🎵 EN REPRODUCCIÓN", padding=(0, 1))


# ──────────────────────────────────────────
# AJUSTE DE VOLUMEN (escala 0-10)
# ──────────────────────────────────────────

def ajustar_volumen():
    """Pide al usuario un nivel de 0 a 10 y aplica el volumen."""

    try:
        # Obtiene la información de la reproducción actual desde Spotify
        actual = sp.current_playback()

        # Obtiene el volumen actual del dispositivo.
        # Si no existe un dispositivo activo, usa 50 como valor por defecto.
        vol_actual = actual.get('device', {}).get('volume_percent', 50) if actual else 50

        # Convierte el volumen de la escala 0-100 a una escala más simple de 0-10
        nivel_actual = round(vol_actual / 10)

        # Muestra el volumen actual utilizando una barra visual
        console.print(f"\n  Volumen actual: {barra_volumen(vol_actual)}")

        # Muestra al usuario la escala de volumen permitida
        console.print("  [dim]Escala: 0 = silencio · 10 = máximo[/dim]\n")

        # Solicita al usuario un nuevo nivel de volumen.
        # Si solo presiona Enter, se utilizará el volumen actual.
        entrada = Prompt.ask(
            "  [bold yellow]Nuevo volumen (0-10)[/bold yellow]",
            default=str(nivel_actual)
        )

        # Verifica que la entrada contenga únicamente números
        if not entrada.isdigit():
            console.print("  [red]Valor no válido.[/red]")
            return  # Finaliza la función si el dato es incorrecto

        # Convierte el texto ingresado por el usuario a un número entero
        nivel = int(entrada)

        # Comprueba que el número esté dentro del rango permitido (0 a 10)
        if not 0 <= nivel <= 10:
            console.print("  [red]Ingresa un número entre 0 y 10.[/red]")
            return  # Termina la función si el valor está fuera del rango

        # Convierte la escala de 0-10 nuevamente a la escala de Spotify (0-100)
        nuevo_vol = nivel * 10

        # Envía la orden a Spotify para cambiar el volumen del dispositivo activo
        sp.volume(nuevo_vol)

        # Muestra el nuevo volumen utilizando la barra visual
        console.print(f"\n  🔊 Volumen ajustado a: {barra_volumen(nuevo_vol)}")

        # Espera un segundo para que el usuario pueda leer el mensaje
        time.sleep(1)

    # Captura errores específicos generados por la API de Spotify
    except spotipy.SpotifyException as e:

        # Verifica si el error se debe a que la cuenta no es Premium
        if "Premium" in str(e):
            console.print("\n[bold red]❌ Controlar el volumen requiere Spotify Premium.[/bold red]")
            time.sleep(1.5)

        # Si es otro error de Spotify, muestra el mensaje recibido
        else:
            console.print(f"\n[bold red]❌ Error:[/bold red] {e}")
            time.sleep(1.5)

    # Captura cualquier otro error inesperado
    except Exception:
        console.print("\n[bold red]❌ Abre Spotify en tu dispositivo primero.[/bold red]")
        time.sleep(1.5)

# ──────────────────────────────────────────
# BÚSQUEDA
# ──────────────────────────────────────────

def buscar_cancion():

    # Solicita al usuario el nombre de una canción o un artista
    query = Prompt.ask("\n[bold cyan]🔍 Nombre de la canción o artista[/bold cyan]")

    # Elimina espacios en blanco y verifica que el usuario haya escrito algo
    # Si la búsqueda está vacía, termina la función
    if not query.strip():
        return

    # Muestra un mensaje indicando que se está realizando la búsqueda
    console.print(f"\n[dim]Buscando '{query}'...[/dim]")

    # Envía la búsqueda a la API de Spotify
    # q=query  -> texto que escribió el usuario
    # limit=8 -> máximo 8 resultados
    # type='track' -> buscar únicamente canciones
    results = sp.search(q=query, limit=8, type='track')

    # Extrae únicamente la lista de canciones encontradas
    tracks = results['tracks']['items']

    # Si no se encontró ninguna canción, muestra un mensaje y termina la función
    if not tracks:
        console.print("[bold red]No se encontraron resultados.[/bold red]")
        time.sleep(1.5)
        return

    # Crea una tabla para mostrar los resultados de forma ordenada
    table = Table(show_header=True, header_style="bold cyan", border_style="dim")

    # Agrega las columnas de la tabla
    table.add_column("N°", style="dim", width=4)
    table.add_column("Canción", style="white")
    table.add_column("Artista", style="green")
    table.add_column("Álbum", style="dim white")
    table.add_column("Dur.", style="dim", justify="right")

    # Recorre todas las canciones encontradas
    for idx, track in enumerate(tracks):

        # Convierte la duración de milisegundos a minutos y segundos
        m, s = divmod(track['duration_ms'] // 1000, 60)

        # Agrega una fila con la información de cada canción
        table.add_row(
            str(idx + 1),                      # Número de la canción
            track['name'],                     # Nombre de la canción
            track['artists'][0]['name'],       # Primer artista de la lista
            track.get('album', {}).get('name', ''),  # Nombre del álbum
            f"{m}:{s:02d}"                     # Duración en formato mm:ss
        )

    # Muestra la tabla completa en la consola
    console.print(table)

    # Pide al usuario el número de la canción que desea reproducir
    # Si presiona Enter, la operación se cancela
    seleccion = Prompt.ask(
        "\n[bold yellow]Número para reproducir (ENTER para cancelar)[/bold yellow]",
        default=""
    )

    # Verifica que el usuario haya ingresado un número
    # y que ese número exista dentro de la lista de resultados
    if seleccion.isdigit() and 1 <= int(seleccion) <= len(tracks):

        # Obtiene la canción elegida por el usuario
        # Se resta 1 porque las listas comienzan en la posición 0
        elegido = tracks[int(seleccion) - 1]

        try:

            # Envía la orden a Spotify para reproducir la canción seleccionada
            # utilizando su URI (identificador único)
            sp.start_playback(uris=[elegido['uri']])

            # Muestra el nombre de la canción que comenzó a reproducirse
            console.print(
                f"\n[bold green]▶ Reproduciendo:[/bold green] "
                f"[bold white]{elegido['name']}[/bold white] "
                f"— [cyan]{elegido['artists'][0]['name']}[/cyan]"
            )

            # Espera un segundo para que el usuario pueda leer el mensaje
            time.sleep(1)

        # Captura errores específicos de Spotify
        except spotipy.SpotifyException as e:

            # Comprueba si el error se debe a que la cuenta no es Premium
            if "Premium" in str(e):
                console.print(
                    "\n[bold red]❌ Esta función requiere Spotify Premium.[/bold red]"
                )
                time.sleep(1.5)

            # Si el error es otro, informa al usuario que debe abrir Spotify
            else:
                console.print(
                    "\n[bold red]❌ Error:[/bold red] Abre Spotify en tu dispositivo primero."
                )
                time.sleep(1.5)


# ────────────────────────────────────────────────────────────────────
# MENÚ PRINCIPAL
# ────────────────────────────────────────────────────────────────────

def ejecutar_accion(opcion):
    try:
        if opcion == "1": # si selecciona la opcion 1 y llama a la funcion buscar cancion
            buscar_cancion()
        elif opcion == "2": #si seleccion la opcion 2
            actual = sp.current_playback() #  obtiene el estado actual del reproductor (canción, dispositivo, si está sonando o no) y dependiendo de eso ejecuta.
            if actual and actual['is_playing']: #Si hay un reproductor abierto Y la música está sonando actualmente
                sp.pause_playback() #Envía la orden a Spotify para que pause la canción
            else:
                sp.start_playback() #Envía la orden a Spotify para que inicie o reanude la reproducción.
            time.sleep(0.5)
        elif opcion == "3": # si selecciona la opcion 3 y llama a la funcion de ajustar volumen
            ajustar_volumen()

    except spotipy.SpotifyException as e: #Si es un problema con la apy
        if "Premium" in str(e): #si detecta la palabra premium ejecuta el mensaje
            console.print("\n[bold red]❌ Esta acción requiere Spotify Premium.[/bold red]")
            time.sleep(1.5) # Esperamos 1.5 segundos para no saturar el servidor / simular tiempo de respuesta
        else:
            console.print(f"\n[bold red]❌ Error de Spotify:[/bold red] {e}")
            time.sleep(1.5)
    except Exception: # sirve para culaquier tipo de fallo general
        console.print("\n[bold red]❌ Error:[/bold red] Asegúrate de tener Spotify abierto en algún dispositivo.") # muestra la advertencia
        time.sleep(1.5)


def menu():
    while True: #crea un bucle infinito
        console.clear() # Limpia todo el texto anterior
        mostrar_logo()

        try: # Intenta ejecutar la apy de spotify
            actual = sp.current_playback() # consulta a Spotify qué canción está sonando en este instante.
            console.print(obtener_estado_reproduccion(actual)) #mprime en pantalla el estado de la cancion
        except Exception:
            pass #si encuentra un fallo, lo omite

        #Interfaz visual del menu principal
        console.print("\n[bold white]📝 MENÚ PRINCIPAL[/bold white]")
        console.print("─" * 42)
        console.print("[bold cyan]  [1][/bold cyan] 🔍 Buscar y reproducir canción")
        console.print("[bold green]  [2][/bold green] ⏯  Play / Pausa")
        console.print("[bold magenta]  [3][/bold magenta] 🔊 Ajustar volumen (0-10)")
        console.print("[bold red]  [4][/bold red] 🚪 Salir")
        console.print("─" * 42)

        opcion = Prompt.ask( #pide al usuario un numero
            "\n[bold yellow]Elige una opción[/bold yellow]",
            choices=["1", "2", "3", "4"] #Validación automática, librería no lo acepta y le vuelve a pedir un número válido.
        )

        if opcion == "4":
            console.print("\n[bold green]👋 ¡Hasta luego![/bold green]\n")
            break #rompre el bucle while

        ejecutar_accion(opcion) # Envia la opcion a la funcion Anteriormente


if __name__ == "__main__":
    menu()
