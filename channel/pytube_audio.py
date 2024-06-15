from pytube import Channel, YouTube
import os
import sys

def download_audio_from_channel(channel_url, download_path='downloads'):
    # Create the download directory if it does not exist
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    # Initialize the Channel object
    channel = Channel(channel_url)

    print(f'Downloading audio from channel: {channel.channel_name}')

    # Loop through all videos in the channel
    for video_url in channel.video_urls:
        try:
            # Initialize the YouTube object
            yt = YouTube(video_url)
            # Get the audio stream with the highest bitrate
            audio_stream = yt.streams.filter(only_audio=True).first()

            print(f'Downloading audio from: {yt.title}')
            
            # Download the audio stream
            audio_stream.download(output_path=download_path)
            
            print(f'Finished downloading: {yt.title}')
        except Exception as e:
            print(f'Error downloading {video_url}: {e}')

if __name__ == '__main__':
    # Example channel URL
    # 'https://www.youtube.com/c/YourChannelName'
    channel_url = sys.argv[1]
    download_audio_from_channel(channel_url)
