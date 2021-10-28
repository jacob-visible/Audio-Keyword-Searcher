import speech_recognition as sr

r = sr.Recognizer()

PATH = 'audio_file_only_5mins.wav'

with sr.AudioFile(PATH) as source:
    audio = r.record(source)

    print(r.recognize_sphinx(audio))
