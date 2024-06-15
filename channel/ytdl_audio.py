import yt_dlp
import os
import sys

def download_audio_from_channel(channel_url, download_path='downloads'):
    # Create the download directory if it does not exist
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    # Options for yt-dlp to download only audio
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Extract the playlist info (channel videos are treated as playlists)
        channel_info = ydl.extract_info(channel_url, download=False)
        
        for entry in channel_info.get('entries', []):
            # Extract the video URL
            video_url = entry.get('url')
            if video_url:
                try:
                    print(f'Downloading audio from: {video_url}')
                    # Download the audio
                    ydl.download([video_url])
                    print(f'Finished downloading: {video_url}')
                except Exception as e:
                    print(f'Error downloading {video_url}: {e}')

if __name__ == '__main__':
    # Example channel URL
    channel_url = sys.arv[1]
    download_audio_from_channel(channel_url)
