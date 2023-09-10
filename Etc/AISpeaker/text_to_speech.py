from gtts import gTTS
from playsound import playsound

text = '안녕하세요. 샤갈입니다.'
file_name = 'sample.mp3'
tts_ko = gTTS(text=text, lang="ko")
tts_ko.save(file_name)
playsound(file_name)
