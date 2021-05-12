import io, random
from gtts import gTTS

#requies ffmeg
from pydub import AudioSegment
from pydub.playback import play
import speech_recognition as sr

from  restura_api import ResturaApi 
from helper import toStr



class ResturaAssistant:

    all_items = ResturaApi.items
    top_items = random.sample(all_items, k=4)
    categories = ResturaApi.categories

    @staticmethod
    def get_audio():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('listening')
            audio = r.listen(source)
            spokenText = ""

            try:
                spokenText = r.recognize_google(audio)
            except Exception as e:
                print("Exception: " + str(e))
        return spokenText

    @staticmethod
    def speak(my_text):
        with io.BytesIO() as f:
            gTTS(text=my_text, lang='en').write_to_fp(f)
            f.seek(0)
            song = AudioSegment.from_file(f, format="mp3")
            play(song)


    @classmethod
    def executeAction(cls, items):
        for item in items:
            print('running')
            ResturaApi.orders.append(item)
        
    @classmethod
    def getData(cls, action):
        if action == 'getOrder':
            orders = ResturaApi.orders
            if len(orders)>0:
                print(f'You have ordered {toStr(ResturaApi.orders)}')
            else:
                print('Your order is empty!')

        if action == 'item':
            print(f'Some of the items we offer are {toStr(cls.top_items)}')

        if action == 'category':
            print(f'we have {toStr(cls.categories)} categories.')
