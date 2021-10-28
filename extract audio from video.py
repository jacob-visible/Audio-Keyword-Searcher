import moviepy.editor

my_clip = moviepy.editor.VideoFileClip(r"1045724829_1080p60.mp4")
my_clip.audio.write_audiofile(r"audio_file_only.wav")