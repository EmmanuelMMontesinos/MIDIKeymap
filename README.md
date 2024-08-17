# MIDIKeymap

**MIDIKeymap** es una herramienta basada en CLI que permite mapear entradas de un controlador MIDI a atajos de teclado y comandos personalizados en tu sistema. Es ideal para automatizar tareas en aplicaciones como OBS, Reaper, VSCode, entre otras.

## Características

- **Mapeo de Teclas MIDI:** Asigna teclas de tu controlador MIDI a atajos de teclado.
- **Control de Sliders y Pads:** Utiliza los sliders y pads de tu controlador MIDI para ejecutar comandos.
- **Soporte para Control de Volumen y Scroll Vertical:** Configura controles especiales en los sliders para manejar el volumen del sistema y el desplazamiento vertical.

## Requisitos

- **Python 3.x**

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/emmanuelmmontesinos/MIDIKeymap.git
    ```

2. Instala las dependencias necesarias:

    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Ejecuta el programa desde la línea de comandos:

    ```bash
    python midikeymap.py
    ```

2. Selecciona una de las opciones disponibles en el menú:

    - **1 - Asignar tecla/pad/slider a comando:** Permite asignar un comando específico a una tecla, pad o slider de tu controlador MIDI.
    - **2 - Activar MIDIKeymap:** Inicia el programa para escuchar las entradas MIDI y ejecutar los comandos mapeados.
    - **3 - Salir:** Cierra el programa.

### Asignación de Comandos

Para asignar un comando a una tecla/pad/slider, sigue estos pasos:

1. Selecciona la opción "1 - Asignar tecla/pad/slider a comando".
2. Presiona la tecla, pad o slider en tu controlador MIDI que deseas asignar.
3. Introduce el comando deseado siguiendo la sintaxis: 

   - Para un comando simple: `f11`
   - Para combinaciones de teclas: `ctrl,c` (esto simularía Ctrl+C)

### Activar MIDIKeymap

Una vez que hayas asignado los comandos a tus controles MIDI, selecciona la opción "2 - Activar MIDIKeymap" para comenzar a escuchar las entradas MIDI. El programa ejecutará automáticamente los comandos mapeados cuando detecte una entrada MIDI.

### Opciones Especiales para Sliders (CC)

Actualmente, puedes asignar las siguientes funciones a los sliders (CC) de tu controlador MIDI usando estas palabras clave:

- **Control de Volumen:** Usa la palabra clave `volumen` para asignar un slider a la función de control de volumen del sistema.
- **Scroll Vertical:** Usa la palabra clave `scroll` para asignar un slider a la función de desplazamiento vertical.

> **Nota:** Estas son las únicas funciones disponibles para los sliders en esta versión. Se planean más opciones en futuras actualizaciones.

## API

En esta sección se detallan las teclas especiales que puedes usar para asignar comandos a tu controlador MIDI. Puedes combinarlas según sea necesario.

### Teclas de Control

- `ctrl`: Tecla Control
- `shift`: Tecla Shift
- `alt`: Tecla Alt
- `cmd` o `win`: Tecla Command (en macOS) o Tecla Windows (en Windows)

### Teclas Funcionales

- `f1` a `f24`: Teclas de función F1 a F24
- `esc`: Tecla Escape
- `tab`: Tecla Tabulador
- `capslock`: Tecla Bloq Mayús
- `enter`: Tecla Enter/Intro
- `backspace`: Tecla Retroceso
- `space`: Tecla Espacio
- `delete`: Tecla Supr
- `insert`: Tecla Insertar
- `home`: Tecla Inicio
- `end`: Tecla Fin
- `pageup`: Tecla AvPág
- `pagedown`: Tecla RePág

### Teclas de Navegación

- `up`: Flecha arriba
- `down`: Flecha abajo
- `left`: Flecha izquierda
- `right`: Flecha derecha

### Teclas de Modificación y Bloqueo

- `numlock`: Bloq Num
- `scrolllock`: Bloq Despl
- `pause`: Pausa/Inter

### Teclas del Teclado Numérico

- `num0` a `num9`: Números en el teclado numérico
- `numadd`: Tecla + en el teclado numérico
- `numsub`: Tecla - en el teclado numérico
- `nummul`: Tecla * en el teclado numérico
- `numdiv`: Tecla / en el teclado numérico
- `numdot`: Punto decimal en el teclado numérico
- `numenter`: Enter en el teclado numérico

### Teclas Misceláneas

- `printscreen`: Imprimir pantalla
- `menu`: Tecla Menú de contexto

Estas teclas pueden ser combinadas para crear comandos más complejos, como `ctrl,shift,a` para simular Ctrl+Shift+A.

## Próximas Funciones

Estamos trabajando en añadir las siguientes funciones a MIDIKeymap:

- **Moverse entre escritorios virtuales:** Navega fácilmente entre escritorios virtuales utilizando los controles de tu dispositivo MIDI.
- **Abrir archivos o programas:** Asigna comandos para abrir archivos o ejecutar programas directamente desde tu controlador MIDI.
- **GUI para facilitar la configuración:** Interfaz gráfica de usuario que hará más sencilla la configuración y asignación de comandos.
- **Guardar la configuración y cargarla automáticamente al iniciar:** Almacena tus configuraciones y cárgalas automáticamente cada vez que inicies el programa.

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún problema o tienes alguna sugerencia, por favor abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## Autor

Desarrollado por [@emmanuelmmontesinos](https://github.com/emmanuelmmontesinos)
