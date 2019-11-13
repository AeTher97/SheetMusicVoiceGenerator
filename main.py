from generate import generate
import os
import time
from visualize import vizualize

# !/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class
import speech_recognition as sr

r = sr.Recognizer()
sr.Microphone.list_microphone_names()
notes = ["c", "d", "e", "f", "g", "a", "h"]
notesLong = ["celina", "dorota", "edward", "filip", "gustaw", "adam", "henryk"]
lengths = {"cała nuta": 1, "półnuta": 2, "ćwierćnuta": 4, "ósemka": 8}
operators = {"razy": 1}
content = []
wait = False

title = input("Podaj tytuł: ")

composer = input("Podaj imię: ")
tagline = input("Podaj tekst copyright: ")

os.system("clear")
while (1):
    print("Czekam")
    os.system("clear")
    vizualize(content)

    print("Slucham nutki")
    mic = sr.Microphone(device_index=0)
    with mic as source:
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source, phrase_time_limit=4)
            v = r.recognize_google(audio, language="pl")
        except sr.UnknownValueError:
            print("Nie zrozumiałem")
            continue

        print(v)
        v = v.lower()
        result = v.split(" ")
        print(result)

        time.sleep(1)

        if result[0] == "koniec":
            break

        if result[0] == "cała" and result[1] == "nuta":
            result[0] = "cała nuta"
            result[1] = result[2]
            del result[2]

        if result[0] == "cofnij":
            if len(content) > 0 and len(content) >= multiplier:
                content = content[:len(content) - multiplier]

        multiplier = 1

        if len(result) < 2:
            print("Za mala ilosc argumentów")
            wait = False
            continue

        if (result[1] == "the"):
            result[1] = "d"

        if (len(result[1]) > 1):
            if result[1][1] == "x":
                resultsInner = result[1].split("x")
                result[1] = resultsInner[0]
                result.insert(2, resultsInner[1])
                multiplier = int(resultsInner[1])

        if len(result) > 2:
            if result[2] == "razy":
                try:
                    multiplier = int(result[3])
                except ValueError:
                    wait = False
                    "Niepoprawny współczynnik mnożący"

        if result[1] in notesLong:
            letter = result[1][0]
            result[1] = ""
            result[1] = letter

        if result[1] in notes and result[0] in lengths:
            for i in range(multiplier):
                content.append(result[1] + str(lengths[result[0]]))
            print("Dodaje nute " + result[1] + " razy " + str(multiplier))
            wait = True
            time.sleep(3)

contentToGenerate = []
for note in content:
    contentToGenerate.append(note.replace("h","b"))

generate(title, composer, tagline, contentToGenerate)
