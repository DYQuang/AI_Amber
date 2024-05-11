# thư viện hỗ trợ
''' cài cách thư viện như: 
    pip install SpeechRecognition
    pip install pyttsx3
    pip install pyaudio
'''

import speech_recognition 
import pyttsx3
import subprocess
from datetime import date, datetime

# bắt đầu chương trình
engine = pyttsx3.init()
robot_ear = speech_recognition.Recognizer()
robot_brain = ""

while True:
    # mở mic và nghe nói cái gì
    with speech_recognition.Microphone() as mic:
        print('Amber đang nghe bạn hãy nói gì đó: ')
        audio = robot_ear.listen(mic)
    print("Amber :.........")

    # nhận dạng giọng nói
    try:
        you = robot_ear.recognize_google(audio, language="vi-VN")
        print("Bạn nói: " + you)
    except speech_recognition.UnknownValueError:
        print("Robot không hiểu bạn nói gì.")
    except speech_recognition.RequestError:
        print("Robot không thể kết nối tới dịch vụ nhận dạng giọng nói.")

    # bộ não của Amber chứa các data để sử lí và gửi thông tin đi
    if you == "":
        robot_brain = " I am can't listen "
    elif "Bạn tên gì" in you:
        robot_brain = "My name is Amber"
    elif "chào" in you:
        robot_brain = " Hello QUANG"
    elif "Tôi tên gì" in you:
        robot_brain = " you name is QUANG"
    elif "Hôm nay là ngày mấy" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d,%Y")
    elif "Mấy giờ rồi" in you:
        now = datetime.today()
        robot_brain = now.strftime("%H hours %M minutes %S seconds")
    elif "tạm biệt" in you:
        robot_brain = "Goodbye"
        print("Amber: " + robot_brain)
        engine.say(robot_brain)
        engine.runAndWait()
        break
    else:
        robot_brain = "I haven't database"
    # hiển thị lên serial và phát âm thanh hồi đáp
    print("Amber: " + robot_brain)
    engine.say(robot_brain)
    engine.runAndWait()