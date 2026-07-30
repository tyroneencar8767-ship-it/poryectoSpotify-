<div align="center">

# 🎵 Spotify por Terminal

<div align="center">
  <img width="700" height="200" alt="image" src="https://github.com/user-attachments/assets/2bff6efc-2b26-4507-917e-cf79055a5da5" />

</div>

### Controla tu música completa desde la línea de comandos — sin abrir nunca la app gráfica.

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Spotipy](https://img.shields.io/badge/Spotipy-API%20Client-1DB954?style=for-the-badge&logo=spotify&logoColor=white)](https://spotipy.readthedocs.io/)
[![Rich](https://img.shields.io/badge/Rich-Terminal%20UI-8A2BE2?style=for-the-badge)](https://rich.readthedocs.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](#-licencia)
[![Status](https://img.shields.io/badge/Status-Activo-brightgreen?style=for-the-badge)](#)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-ff69b4?style=for-the-badge)](#-contribuciones)

<br>

Un reproductor de **Spotify** con interfaz visual construida 100% en la terminal, usando `spotipy` para hablar con la API oficial y `rich` para que la consola se vea como una app real: paneles, tablas, colores y barras de progreso.

</div>

---

## 📑 Índice

- [✨ Demostración](#-demostración)
- [🚀 Características principales](#-características-principales)
- [🧰 Tecnologías y requisitos](#-tecnologías-y-requisitos)
- [🔑 Cómo obtener tus credenciales de Spotify](#-cómo-obtener-tus-credenciales-de-spotify)
- [⚙️ Instalación y configuración](#️-instalación-y-configuración)
- [🕹️ Uso](#️-uso)
- [🔒 Seguridad y buenas prácticas](#-seguridad-y-buenas-prácticas)
- [🗺️ Roadmap](#️-roadmap)
- [🤝 Contribuciones](#-contribuciones)
- [📄 Licencia](#-licencia)

---

## ✨ Demostración

<div align="center">


<img width="872" height="531" alt="image" src="https://github.com/user-attachments/assets/4d28e773-01c0-44d0-a915-8b79748aa9cc" />



</div>

> [!TIP]
> Reemplazá este bloque por un GIF real grabado con [Terminalizer](https://github.com/faressoft/terminalizer) o [asciinema](https://asciinema.org/) para maximizar el impacto visual en tu portafolio.

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

## 🧰 Tecnologías y requisitos

| Categoría | Detalle |
|---|---|
| 🐍 Lenguaje | [Python](https://www.python.org/) 3.8 o superior |
| 📡 Cliente de API | [`spotipy`](https://spotipy.readthedocs.io/) — wrapper oficial no oficial de la Web API de Spotify |
| 🎨 Interfaz visual | [`rich`](https://rich.readthedocs.io/) — renderizado avanzado en terminal |
| 🎧 Cuenta | **Spotify Premium** (requerida para controlar reproducción y volumen) |
| 👨‍💻 Cuenta de desarrollador | [Spotify for Developers](https://developer.spotify.com/dashboard) (gratuita) |
| 🌐 Conexión | Internet activa (todo pasa por la Web API de Spotify) |

> [!IMPORTANT]
> Las cuentas **gratuitas** de Spotify pueden usar la búsqueda, pero **no** pueden controlar reproducción, pausa ni volumen — la propia API de Spotify restringe esas acciones a cuentas Premium.

---

## 🔑 Cómo obtener tus credenciales de Spotify

Para que la app pueda autenticarse contra la Web API, necesitás registrar tu propia aplicación en el Dashboard de Spotify. Seguí estos pasos:

**1.** Entrá a [developer.spotify.com/dashboard](https://developer.spotify.com/dashboard) e iniciá sesión con tu cuenta de Spotify.

**2.** Hacé clic en **"Create app"** y completá:
   - **App name**: el nombre que quieras (ej. `Spotify por Terminal`)
   - **App description**: una descripción breve
   - **Redirect URI**: `https://www.google.com/`

> [!NOTE]
> La *Redirect URI* debe coincidir **exactamente**, carácter por carácter (incluyendo la barra final `/`), con la que uses en tu código. Si no coinciden, Spotify devolverá el error `redirect_uri: Not matching configuration`.

**3.** Aceptá los términos de servicio y hacé clic en **"Save"**.

**4.** Entrá a **"Settings"** dentro de tu app recién creada. Ahí vas a encontrar:
   - **Client ID** → visible directamente.
   - **Client Secret** → hacé clic en "View client secret".

> [!WARNING]
> Nunca subas tu `Client Secret` a un repositorio público. Tratalo como una contraseña.

**5.** Copiá ambos valores — los vas a necesitar en el paso de configuración de abajo.

---

## ⚙️ Instalación y configuración

**1. Cloná el repositorio**

```bash
git clone https://github.com/tu-usuario/spotify-por-terminal.git
cd spotify-por-terminal
```

**2. Creá y activá un entorno virtual**

```bash
python -m venv venv

# En Windows
venv\Scripts\activate

# En macOS / Linux
source venv/bin/activate
```

**3. Instalá las dependencias**

```bash
pip install -r requirements.txt
```

> [!TIP]
> Si no tenés un `requirements.txt`, podés generarlo con `pip freeze > requirements.txt` una vez que tengas `spotipy` y `rich` instalados, o instalarlos directo con `pip install spotipy rich`.

**4. Configurá tus credenciales**

Recomendado: usar variables de entorno en vez de escribir las credenciales directamente en el código.

Creá un archivo `.env` en la raíz del proyecto:

```bash
CLIENT_ID=tu_client_id_aqui
CLIENT_SECRET=tu_client_secret_aqui
REDIRECT_URI=https://www.google.com/
```

Y cargalas en tu script con `python-dotenv`:

```python
from dotenv import load_dotenv
import os

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
```

> [!NOTE]
> Si preferís simplicidad por sobre buenas prácticas para pruebas locales rápidas, podés pegar las credenciales directamente en las variables `CLIENT_ID` y `CLIENT_SECRET` del script — pero nunca subas ese archivo a un repositorio público así.

**5. Ejecutá el programa**

```bash
python spotify_cli.py
```

La primera vez se abrirá tu navegador pidiéndote iniciar sesión en Spotify y autorizar la aplicación. Una vez aceptado, podés volver a la terminal.

---

## 🕹️ Uso

Al ejecutar el script vas a ver el menú principal con 4 opciones:

| Opción | Acción |
|:---:|---|
| `1` | 🔍 Buscar una canción o artista y reproducirla |
| `2` | ⏯️ Play / Pausa (detecta el estado automáticamente) |
| `3` | 🔊 Ajustar el volumen en una escala de 0 a 10 |
| `4` | 🚪 Salir del programa |

> [!IMPORTANT]
> Necesitás tener **Spotify abierto y activo en algún dispositivo** (celular, PC, web player) — este programa envía órdenes a la API, pero el audio se reproduce en el dispositivo que tengas encendido.

---

## 🔒 Seguridad y buenas prácticas

> [!WARNING]
> Este proyecto interactúa con credenciales sensibles. Seguí estas recomendaciones antes de subir tu código a GitHub:

- ✅ Agregá `.env` y `.cache*` a tu `.gitignore`:

```gitignore
# Credenciales y tokens
.env
.cache
.cache-*

# Entorno virtual
venv/
__pycache__/
*.pyc
```

- ✅ Nunca hardcodees `CLIENT_SECRET` en un commit.
- ✅ Si accidentalmente subiste una credencial, **regenerala** desde el Dashboard de Spotify inmediatamente — no alcanza con borrarla del código.
- ✅ El archivo `.cache` que genera `spotipy` contiene tu token de acceso: tratalo con la misma precaución que una contraseña.

---

## 🗺️ Roadmap

Ideas para futuras contribuciones:

- [ ] ⏭️ Soporte para saltar a la siguiente / canción anterior
- [ ] ⌨️ Atajos de teclado sin necesidad de presionar Enter
- [ ] 📃 Soporte para reproducir playlists completas
- [ ] 🔀 Control de shuffle y modo repetición desde el menú
- [ ] 📊 Barra de progreso de la canción en tiempo real

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

## 📄 Licencia

Este proyecto está bajo la licencia **MIT**. Consultá el archivo [`LICENSE`](./LICENSE) para más detalles.

<div align="center">

---

**Hecho con 🎧 y Python** — si te sirvió, considerá dejar una ⭐

</div>
