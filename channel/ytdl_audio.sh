#!/bin/bash

# URL del canal de YouTube
CHANNEL_URL=$1
# Directorio donde se guardarán las descargas
DOWNLOAD_PATH="downloads"

# Crear el directorio de descargas si no existe
mkdir -p "$DOWNLOAD_PATH"

# Comando yt-dlp para descargar solo el audio en formato mp3
yt-dlp -f bestaudio --extract-audio --audio-format mp3 --audio-quality 192K -o "$DOWNLOAD_PATH/%(title)s.%(ext)s" "$CHANNEL_URL"
