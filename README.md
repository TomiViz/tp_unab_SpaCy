# unab_pa_tp_3
# Chatbot para Asistencia en Funciones Básicas del Celular

Este proyecto es un chatbot desarrollado en Python que utiliza SpaCy para procesar el lenguaje natural. El chatbot está diseñado para ayudar a personas mayores a utilizar las funciones básicas de un celular, como enviar mensajes, hacer llamadas, tomar fotos, grabar videos, entre otras.

## Estructura del Proyecto

El proyecto está organizado en la siguiente estructura de archivos:

tp_unab_SpaCy/
├── chatbot/
│ ├── init.py
│ ├── bot.py
│ ├── intents.py
│ └── responses.py
└── main.py

### Descripción de Archivos

- **`chatbot/__init__.py`**: Archivo vacío o que incluye la inicialización del paquete.
- **`chatbot/intents.py`**: Contiene las palabras clave asociadas a cada intención del usuario.
- **`chatbot/responses.py`**: Contiene las respuestas predefinidas para cada intención del usuario.
- **`chatbot/bot.py`**: Define la clase `ChatBot` que maneja la lógica del procesamiento de lenguaje natural y la generación de respuestas.
- **`main.py`**: Archivo principal que ejecuta el chatbot.

## Instalación

### Prerrequisitos

- Python 3.x
- pip (gestor de paquetes de Python)
- Virtualenv (opcional pero recomendado)

### Paso a Paso

1. Clona este repositorio o descarga los archivos.

```bash
git clone https://github.com/TomiViz/tp_unab_SpaCy.git
cd tp_unab_SpaCy
