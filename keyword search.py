import speech_recognition as sr
import sys, os
from pocketsphinx import *
from sphinxbase import *


r = sr.Recognizer()

PATH = 'audio_file_only_5mins.wav'

modeldir = "C:\SyncFiles\Programming\Python Audio Processing\Sphinx Models\cmusphinx-en-us-8khz-5.2"

# Create a decoder with certain model
config = Decoder.default_config()
config.set_string('-hmm', os.path.join(modeldir, 'en-us/en-us'))
config.set_string('-dict', os.path.join(modeldir, 'en-us/cmudict-en-us.dict'))
config.set_string('-keyphrase', 'hello')


# Open file to read the data
stream = open(PATH, "rb")

# Process audio chunk by chunk. On keyphrase detected perform action and restart search
decoder = Decoder(config)
decoder.start_utt()
while True:
    buf = stream.read(1024)
    if buf:
         decoder.process_raw(buf, False, False)
    else:
         break
    if decoder.hyp() != None:
        print ([(seg.word, seg.prob, seg.start_frame, seg.end_frame) for seg in decoder.seg()])
        print ("Detected keyphrase, restarting search")
        decoder.end_utt()
        decoder.start_utt()