import os
import yt_dlp
from flask import Flask, request, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/convert', methods=['POST'])
def convert():
    data = request.json
    youtube_url = data.get('url')
    
    # Define file paths
    output_filename = 'downloaded_audio'
    final_file = f"{output_filename}.mp3"

    # Remove old files if they exist to avoid errors
    if os.path.exists(final_file):
        os.remove(final_file)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_filename,
        'cookiefile': 'cookies.txt',  # Ensure this file is in your GitHub
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'ffmpeg_location': './', 
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
        
        return send_file(final_file, as_attachment=True)
    except Exception as e:
        print(f"Error: {str(e)}")
        return {"error": str(e)}, 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
