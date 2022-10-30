"""
Создайте программу «Голосовой помощник». Программа должна работать в
цикле и после каждой команды должна повторно
слушать пользователя и обрабатывать его команды.
Среди команд должны быть следующие:

«Write File»: Если пользователь произнесет эту команду, то программа считывает текст
с изображения и весь текст помещает в файл "image_text.txt";
«Read File»: Если пользователь произнесет эту команду, то программа считывает текст
из файла "image_text.txt" и выводит текст в консоли;
«Exit»: при произношении этой команды программа должна завершать свою работу.

Библиотеки распознавания и воспроизведения голоса:
pip install pywin32 - библиотека для Windows
pip install pypiwin32 - windows
pip install pyttsx3 - проговаривание текста
pip install SpeechRecognition - распознавание голоса
pip install pyaudio - для windows

Библиотеки для работы с текстом на изображении:
pip install pillow
pip install pytesseract
pip install tesseract
"""

from PIL import Image
from pytesseract import image_to_string
import pytesseract

import pyttsx3
import speech_recognition as sr

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
engine = pyttsx3.init()


def sayIt(talk):
    engine.say(talk)
    engine.runAndWait()


sayIt('Работаем, все системы в норме.')

while True:
    try:
        sayIt('Слушаю')
        record = sr.Recognizer()
        with sr.Microphone(device_index=0) as source:
            print('Listening..')

            audio = record.listen(source)
            result = record.recognize_google(audio, language='en-EN')
            result = result.lower()
            print(result)

            if result == 'write file':
                photo_text = image_to_string(Image.open('images/img.png'), lang='eng')
                with open('image_text.txt', 'w') as file:
                    file.write(photo_text)

            elif result == 'read file':
                try:
                    with open('image_text.txt', 'r') as file:
                        text = file.read()
                        print(f'Your text: \n {text}')
                except FileNotFoundError:
                    sayIt('Файла нет, сначала давай добудем данные')

            elif result == 'exit':
                print('Bye-Bye')
                break
    except sr.UnknownValueError:
        print('I don`t understand you')
        sayIt('Ошибочка вышла')
    except sr.RequestError:
        print('Something going wrong!')
        sayIt('Ошибочка вышла')
