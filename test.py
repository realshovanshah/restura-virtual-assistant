import io
from gtts import gTTS          
import io
from pydub import AudioSegment
from pydub.playback import play
import speech_recognition as sr


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening')
        audio = r.listen(source)
        print('haha')
        spoken = ""

        try:
            spoken = r.recognize_google(audio)
            print(spoken)
        except Exception as e:
            print("Exception: " + str(e))
    return spoken

print('called')
get_audio()


# def speak(my_text):
#     with io.BytesIO() as f:
#         print("Init gTTS...")
#         gTTS(text=my_text, lang='en').write_to_fp(f)
#         f.seek(0)
#         return Audio(data=f, autoplay=True)


# To play audio text-to-speech during execution
# def speak(my_text):
#     with io.BytesIO() as f:
#         gTTS(text=my_text, lang='en').write_to_fp(f)
#         f.seek(0)
#         song = AudioSegment.from_file(f, format="mp3")
#         play(song)

# count = 0

# def speak(data):
#     global count

#     tts = gTTS(text=data, lang='en')
#     tts.save(f'speech{count%2}.mp3')
#     mixer.init()
#     mixer.music.load(f'speech{count%2}.mp3')
#     mixer.music.play()
#     count += 1