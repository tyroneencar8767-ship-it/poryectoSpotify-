<div align="center">

# 🎵 Spotify CLI Player

<img width="700" height="200" alt="Spotify CLI Player" src="https://github.com/user-attachments/assets/2bff6efc-2b26-4507-917e-cf79055a5da5" />

### Controla tu música completa desde la línea de comandos — sin abrir nunca la app gráfica.

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Spotipy](https://img.shields.io/badge/Spotipy-API%20Client-1DB954?style=for-the-badge&logo=spotify&logoColor=white)](https://spotipy.readthedocs.io/)
[![Rich](https://img.shields.io/badge/Rich-Terminal%20UI-8A2BE2?style=for-the-badge)](https://rich.readthedocs.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](#-licencia)
[![Status](https://img.shields.io/badge/Status-Activo-brightgreen?style=for-the-badge)](#)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-ff69b4?style=for-the-badge)](#-contribuciones)

<br>

Un reproductor de **Spotify** con interfaz visual construida 100 % en la terminal, usando `spotipy` para hablar con la API oficial y `rich` para que la consola se vea como una app real: paneles, tablas, colores y barras de progreso.

</div>

---

## 📑 Índice

| | Sección | Qué vas a encontrar |
|:---:|---|---|
| ✨ | [Demostración](#-demostración) | Cómo se ve en funcionamiento |
| 🚀 | [Características principales](#-características-principales) | Qué puede hacer el reproductor |
| 🧰 | [Requisitos](#-requisitos) | Lo que necesitás antes de empezar |
| ⚡ | [Instalación rápida](#-instalación-rápida) | De cero a funcionando en 3 pasos |
| 🔑 | [Credenciales de Spotify](#-credenciales-de-spotify) | Crear tu app en el Dashboard |
| ⚙️ | [Configuración](#️-configuración) | Dónde poner tu Client ID y Secret |
| 🕹️ | [Uso](#️-uso) | El menú y sus opciones |
| 🗂️ | [Estructura del proyecto](#️-estructura-del-proyecto) | Qué hace cada archivo |
| 🧯 | [Solución de problemas](#-solución-de-problemas) | Errores comunes y cómo resolverlos |
| 🤝 | [Contribuciones](#-contribuciones) | Cómo aportar al proyecto |
| 👥 | [Créditos](#-créditos-y-colaboradores) | Quiénes lo hicieron |
| 📄 | [Licencia](#-licencia) | MIT |

---

## ✨ Demostración

<div align="center">

<img width="610" height="442" alt="Demostración del Spotify CLI Player en la terminal" src="https://github.com/user-attachments/assets/b9d41e4b-5b58-4f1b-9a17-6a92a6dd594f" />

</div>

---

## 🚀 Características principales

<table>
<tr>
<td width="50%" valign="top">

### 🔍 Búsqueda inteligente
Busca canciones o artistas directamente desde la terminal y obtené hasta 8 resultados organizados en una tabla clara: canción, artista, álbum y duración.

</td>
<td width="50%" valign="top">

### ⏯️ Control de reproducción
Un solo botón que actúa como **play/pausa dinámico**: detecta el estado real de tu reproducción y alterna automáticamente.

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🔊 Volumen simplificado
Escala amigable de **0 a 10** (en vez de 0-100), con una barra visual de bloques que se actualiza al instante.

</td>
<td width="50%" valign="top">

### 🎨 Interfaz con estilo
Paneles, colores, tablas alineadas e íconos gracias a `rich` — la terminal deja de verse como texto plano.

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🛡️ Manejo de errores robusto
Cada acción está protegida con `try/except`: mensajes claros si falta Premium, si no hay dispositivo activo o si algo falla en la API.

</td>
<td width="50%" valign="top">

### 🔐 Autenticación OAuth
Login seguro vía navegador con `SpotifyOAuth`, con renovación automática del token — iniciás sesión una sola vez.

</td>
</tr>
</table>

---

## 🧰 Requisitos

| Categoría | Detalle |
|---|---|
| 🐍 Lenguaje | [Python](https://www.python.org/) 3.8 o superior |
| 📡 Cliente de API | [`spotipy`](https://spotipy.readthedocs.io/) — wrapper de la Web API de Spotify |
| 🎨 Interfaz visual | [`rich`](https://rich.readthedocs.io/) — renderizado avanzado en terminal |
| 🎧 Cuenta | **Spotify Premium** (requerida para controlar reproducción y volumen) |
| 👨‍💻 Cuenta de desarrollador | [Spotify for Developers](https://developer.spotify.com/dashboard) (gratuita) |
| 🌐 Conexión | Internet activa (todo pasa por la Web API de Spotify) |
| 🎫 Código fuente | [`spotify.py`](spotify.py) |

> [!IMPORTANT]
> Las cuentas **gratuitas** de Spotify pueden usar la búsqueda, pero **no** pueden controlar reproducción, pausa ni volumen — la propia API de Spotify restringe esas acciones a cuentas Premium.

---

## ⚡ Instalación rápida

**1. Cloná el repositorio**

```bash
git clone https://github.com/tyronx7/spotify-cli-player.git
cd spotify-cli-player
```

**2. Instalá las dependencias**

```bash
pip install -r requirements.txt
```

<details>
<summary>💡 Recomendado: usar un entorno virtual</summary>

```bash
# Crear y activar el entorno
python -m venv .venv

# Linux / macOS
source .venv/bin/activate

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Luego instalar
pip install -r requirements.txt
```

</details>

**3. Configurá tus credenciales** → seguí las secciones [🔑 Credenciales](#-credenciales-de-spotify) y [⚙️ Configuración](#️-configuración).

**4. Ejecutá el programa**

```bash
python spotify.py
```

La primera vez se abrirá tu navegador pidiéndote iniciar sesión en Spotify y autorizar la aplicación. Copiá la URL a la que te redirige y pegala en la terminal cuando te la pida. Después de eso, el token queda cacheado y no vuelve a pedírtelo.

---

## 🔑 Credenciales de Spotify

Para que la app pueda autenticarse contra la Web API, necesitás registrar tu propia aplicación en el Dashboard de Spotify.

**1.** Entrá a [developer.spotify.com/dashboard](https://developer.spotify.com/dashboard) e iniciá sesión con tu cuenta de Spotify.

**2.** Hacé clic en **"Create app"** y completá:

| Campo | Valor |
|---|---|
| **App name** | El nombre que quieras (ej. `Spotify por Terminal`) |
| **App description** | Una descripción breve |
| **Redirect URI** | `https://www.google.com/` |
| **API/SDKs** | Marcá **Web API** |

> [!NOTE]
> La *Redirect URI* debe coincidir **exactamente**, carácter por carácter (incluyendo la barra final `/`), con la que uses en tu código. Si no coinciden, Spotify devolverá el error `INVALID_CLIENT: Invalid redirect URI`.

**3.** Aceptá los términos de servicio y hacé clic en **"Save"**.

**4.** Entrá a **"Settings"** dentro de tu app recién creada. Ahí vas a encontrar:

- **Client ID** → visible directamente.
- **Client Secret** → hacé clic en *"View client secret"*.

**5.** Copiá ambos valores — los vas a usar en el paso siguiente.

> [!WARNING]
> Nunca subas tu `Client Secret` a un repositorio público. Tratalo como una contraseña. El archivo [`.gitignore`](.gitignore) de este proyecto ya excluye `.env` y el archivo `.cache` de Spotipy (que contiene tu token de acceso).

---

## ⚙️ Configuración

Tenés **dos formas** de darle tus credenciales al programa. La primera es la recomendada.

### Opción A — Variables de entorno (recomendada) ✅

No tocás el código, así que no hay riesgo de commitear tus secretos por accidente.

<details open>
<summary><b>Linux / macOS</b></summary>

```bash
export SPOTIPY_CLIENT_ID="tu_client_id"
export SPOTIPY_CLIENT_SECRET="tu_client_secret"
export SPOTIPY_REDIRECT_URI="https://www.google.com/"
```

</details>

<details>
<summary><b>Windows (PowerShell)</b></summary>

```powershell
$env:SPOTIPY_CLIENT_ID = "tu_client_id"
$env:SPOTIPY_CLIENT_SECRET = "tu_client_secret"
$env:SPOTIPY_REDIRECT_URI = "https://www.google.com/"
```

</details>

### Opción B — Editar el archivo

Abrí [`spotify.py`](spotify.py) y reemplazá los valores por defecto al inicio del archivo:

```python
CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID", "tu_client_id_real_aqui")
CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET", "tu_client_secret_real_aqui")
REDIRECT_URI = os.environ.get("SPOTIPY_REDIRECT_URI", "https://www.google.com/")
```

> [!TIP]
> Si ejecutás el programa sin configurar nada, te avisa con un mensaje claro en vez de fallar con un error críptico de OAuth.

---

## 🕹️ Uso

```bash
python spotify.py
```

Al ejecutar el script vas a ver el panel de reproducción actual y el menú principal con 4 opciones:

| Opción | Acción | Qué hace |
|:---:|---|---|
| `1` | 🔍 **Buscar y reproducir** | Busca hasta 8 canciones y reproduce la que elijas por número |
| `2` | ⏯️ **Play / Pausa** | Detecta el estado real y alterna automáticamente |
| `3` | 🔊 **Ajustar volumen** | Escala de 0 a 10 con barra visual |
| `4` | 🚪 **Salir** | Cierra el programa |

También podés salir en cualquier momento con <kbd>Ctrl</kbd> + <kbd>C</kbd>.

> [!IMPORTANT]
> Necesitás tener **Spotify abierto y activo en algún dispositivo** (celular, PC, web player) — este programa envía órdenes a la API, pero el audio se reproduce en el dispositivo que tengas encendido.

---

## 🗂️ Estructura del proyecto

```
spotify-cli-player/
├── spotify.py          # Todo el programa: auth, menú, búsqueda, reproducción y volumen
├── requirements.txt    # Dependencias (spotipy, rich)
├── .gitignore          # Excluye .cache, .env y artefactos de Python
├── LICENSE         # Licencia MIT
└── README.md           # Este archivo
```

<details>
<summary>🔎 Funciones principales de <code>spotify.py</code></summary>

| Función | Responsabilidad |
|---|---|
| `mostrar_logo()` | Dibuja el encabezado del programa |
| `barra_volumen()` | Convierte 0-100 en una barra visual de 10 bloques |
| `nombre_artista()` | Devuelve el primer artista de una canción de forma segura |
| `obtener_estado_reproduccion()` | Arma el panel "EN REPRODUCCIÓN" |
| `ajustar_volumen()` | Pide un nivel 0-10 y lo aplica al dispositivo activo |
| `buscar_cancion()` | Busca, muestra la tabla de resultados y reproduce la elegida |
| `ejecutar_accion()` | Enruta la opción del menú y centraliza el manejo de errores |
| `menu()` | Bucle principal de la interfaz |

</details>

---

## 🧯 Solución de problemas

| Error / síntoma | Causa | Solución |
|---|---|---|
| `❌ Faltan las credenciales de Spotify` | No configuraste `CLIENT_ID` / `CLIENT_SECRET` | Seguí la sección [⚙️ Configuración](#️-configuración) |
| `INVALID_CLIENT: Invalid redirect URI` | La Redirect URI del código no coincide con la del Dashboard | Verificá que sean idénticas, incluida la `/` final |
| `❌ Esta acción requiere Spotify Premium` | Tu cuenta es gratuita | La API solo permite controlar reproducción con Premium |
| `❌ Abre Spotify en tu dispositivo primero` | No hay ningún dispositivo activo | Abrí Spotify en el celular, PC o web player y reproducí algo |
| `ModuleNotFoundError: No module named 'spotipy'` | Faltan las dependencias | Ejecutá `pip install -r requirements.txt` |
| La sesión quedó con la cuenta equivocada | Token cacheado de un login anterior | Borrá el archivo `.cache` y volvé a ejecutar |

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si este proyecto te resultó útil:

1. ⭐ Dejá una **estrella** en el repositorio — ayuda muchísimo a que más gente lo encuentre.
2. 🍴 Hacé un **fork** y proponé tus propias mejoras.
3. 🐛 Abrí un **issue** si encontrás un bug o tenés una idea.
4. 🔀 Enviá un **Pull Request** con tus cambios.

```bash
# Flujo sugerido
git checkout -b feature/mi-mejora
git commit -m "Agrega: mi mejora"
git push origin feature/mi-mejora
```

---

## 👥 Créditos y Colaboradores

<div align="center">

| Avatar | Usuario de GitHub | Perfil |
| :---: | :--- | :--- |
| <img src="https://github.com/JoseCamilo667.png" width="40" style="border-radius: 50%;"> | **JoseCamilo667** | [@JoseCamilo667](https://github.com/JoseCamilo667) |
| <img src="https://github.com/manuelponcearmijos-lgtm.png" width="40" style="border-radius: 50%;"> | **manuelponcearmijos-lgtm** | [@manuelponcearmijos-lgtm](https://github.com/manuelponcearmijos-lgtm) |
| <img src="https://github.com/Cebillo.png" width="40" style="border-radius: 50%;"> | **Cebillo** | [@Cebillo](https://github.com/Cebillo) |
| <img src="https://github.com/tyronx7.png" width="40" style="border-radius: 50%;"> | **tyronx7** | [@tyronx7](https://github.com/tyronx7) |

</div>

---

## 📄 Licencia

Este proyecto está bajo la licencia **MIT**. Consultá el archivo [`LICENSE.txt`](LICENSE) para más detalles.

<div align="center">

---

**Hecho con Python** — si te sirvió, considerá dejar una ⭐

</div>

