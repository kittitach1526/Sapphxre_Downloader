from yt_dlp import YoutubeDL
from pydub import AudioSegment
import os

def download_youtube_audio(url, output_path):
    """Download audio from YouTube using yt-dlp and convert it to MP3."""
    try:
        # กำหนดตัวเลือกในการดาวน์โหลดเฉพาะเสียง
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading URL: {url}")
            info_dict = ydl.extract_info(url, download=True)
            title = info_dict.get('title', None)
            print(f"Download Success! : {title}.mp3")

    except Exception as e:
        print(f'เกิดข้อผิดพลาด: {e}')

# ตัวอย่างการใช้งาน

print(r"""

   _____                   __                                                                    
  / ___/____ _____  ____  / /_  _  __________                                                    
  \__ \/ __ `/ __ \/ __ \/ __ \| |/_/ ___/ _ \                                                   
 ___/ / /_/ / /_/ / /_/ / / / />  </ /  /  __/                                                   
/____/\__,_/ .___/ .___/_/ /_/_/|_/_/   \___/                                                    
__  __    /_/   /_/_        __            ____                      __                __         
\ \/ /___  __  __/ /___  __/ /_  ___     / __ \____ _      ______  / /___  ____ _____/ /__  _____
 \  / __ \/ / / / __/ / / / __ \/ _ \   / / / / __ \ | /| / / __ \/ / __ \/ __ `/ __  / _ \/ ___/
 / / /_/ / /_/ / /_/ /_/ / /_/ /  __/  / /_/ / /_/ / |/ |/ / / / / / /_/ / /_/ / /_/ /  __/ /    
/_/\____/\__,_/\__/\__,_/_.___/\___/  /_____/\____/|__/|__/_/ /_/_/\____/\__,_/\__,_/\___/_/     
                                                                                                 

""")
# youtube_url = 'https://www.youtube.com/watch?v=IwtHOiB-CDI'
print("Can't insert playlist or list ")
youtube_url = str(input('Youtube URL : '))
print("URL : ",youtube_url)
output_path = r'music'  # เปลี่ยนเป็นตำแหน่งที่ต้องการบันทึกไฟล์
download_youtube_audio(youtube_url, output_path)
