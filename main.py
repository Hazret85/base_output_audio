import speech_recognition as sr
from gtts import gTTS
import pygame
import os


def speak(text):
    tts = gTTS(text=text, lang='ru')
    filename = "voice.mp3"
    tts.save(filename)

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue

    pygame.mixer.quit()

    if os.path.exists(filename):
        os.remove(filename)


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Скажи что-нибудь...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio, language='ru-RU')
            print(f"Вы сказали: {command}")
            return command
        except sr.UnknownValueError:
            print("Не понял, повторите...")
            return ""
        except sr.RequestError:
            print("Ошибка соединения")
            return ""


def handle_command(command):
    if "привет" in command.lower():
        response = "Привет! Как я могу помочь?"
    elif "как тебя зовут" in command.lower():
        response = "Меня зовут Пятница!"
    else:
        response = "Извините, я не понимаю эту команду."

    speak(response)


if __name__ == "__main__":
    command = listen()
    if command:
        handle_command(command)
