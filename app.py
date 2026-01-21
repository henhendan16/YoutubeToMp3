from flask import Flask, request, send_file
from flask_cors import CORS
import yt_dlp
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "YouTube to MP3 Backend is Running!"

@app.route('/download', methods=['GET'])
def download_mp3():
    video_url = request.args.get('url')
    if not video_url:
        return {"error": "No URL provided"}, 400

    # This is a very basic example; you'll expand this later
    return {"message": f"URL received: {video_url}. Backend is ready!"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
