import os
import time
import playsound
from gtts import gTTS
import speech_recognition as sr

'''
pip install gtts
pip install pyaudio
pip install playsound
pip install speech_recognition
'''

language = 'vi'

from gtts import gTTS
import os
import ctypes

def close_sound():
    # Đóng alias nếu còn mở
    try:
        ctypes.windll.winmm.mciSendStringW('close mySound', None, 0, None)
    except:
        pass
    # Xóa file cũ nếu vẫn tồn tại
    if os.path.exists("sound.mp3"):
        os.remove("sound.mp3")

def speak(text):
    # 1) Đóng và xóa file cũ
    close_sound()
    # 2) Tạo file mới
    tts = gTTS(text, lang='vi')
    tts.save("sound.mp3")            # giờ sẽ không vướng permission
    # 3) Mở qua MCI với alias
    ctypes.windll.winmm.mciSendStringW('open "sound.mp3" alias mySound', None, 0, None)
    ctypes.windll.winmm.mciSendStringW('play mySound', None, 0, None)

speak("nghe bai trinh chua")
time.sleep(2)
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tôi: ", end='')
        audio = r.listen(source, phrase_time_limit=5)
        try:
            text = r.recognize_google(audio, language="vi-VN")
            print(text)
            return text
        except:
            print("...")
            return ""

while True:
    user_command = ""
    user_command = get_audio()
    if "mở cửa" in user_command:
        speak("Tôi đã mở cửa")
        time.sleep(5)
    if "nắm tay" in user_command:
        speak("Nắm tay luôn")
        time.sleep(5)
    if "thả tay" in user_command:
        speak("thả bàn tay luôn")
        time.sleep(5)
    if "phát nhạc" in user_command:
        speak("ối giời ôi là ối giời ôi, trình là gì mà trình")
        time.sleep(5)