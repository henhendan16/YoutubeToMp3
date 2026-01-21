#!/usr/bin/env bash
# Exit on error
set -o errexit

pip install -r requirements.txt

# Download ffmpeg binary if not present
if [ ! -f ./ffmpeg ]; then
  curl -L https://github.com/yt-dlp/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-linux64-gpl.tar.xz | tar xJ --strip-components=1
fi
