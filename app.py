import os
import yt_dlp
from flask import Flask, request, send_file

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert():
    data = request.json
    youtube_url = data.get('url')
    
    # Settings for yt-dlp to extract just the audio
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'downloaded_audio.%(ext)s',
        'cookiefile': 'cookies.txt',  # <--- ADD THIS LINE
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])
    
    # Send the converted file back to your phone
    return send_file('downloaded_audio.mp3', as_attachment=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
