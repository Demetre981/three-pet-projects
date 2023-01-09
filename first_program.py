import moviepy.editor
from pathlib import Path

video_file = Path('my_video2.mp4')# first or second video))

video = moviepy.editor.VideoFileClip(f"{video_file}")
audio = video.audio
audio.write_audiofile(f"{video_file.stem}.mp3")
