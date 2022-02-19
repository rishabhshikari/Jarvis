import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import pyautogui
import os
import datef
import random
import wolframalpha
app = wolframalpha.Client('5WR4QT-WAQ3J493J8')

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talk('good morning sir i am your assistant Jarvis, what can i do for you?')
    elif hour>=12 and hour<18:
        talk('good afternoon sir  i am your assistant Jarvis, what can i do for you?')
    else:
        talk('good evening sir i am your assistant Jarvis, what can i do for you?')

def take_command():
    try:
        with sr.Microphone() as source:
            talk('listening sir.... ')
            print('listening sir....')
            voice = listener.listen(source)
            print('Recognising...')
            command = listener.recognize_google(voice, language='en-in')
            command = command.lower()


        if 'jarvis' in command:
            command = command.replace('jarvis','')
            print(command)
    except Exception:
        talk('error...')
        print('Network connection error')
        return 'none'

    return command
if __name__ == '__main__':
    wish()
    while True:
        command = take_command()
        print(command)

        if 'play' in command:
            song = command.replace('play','')
            talk('playing'+song)
            pywhatkit.playonyt(song)

        elif 'tell me the time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            talk('Current time is ' + time)

        elif 'wikipedia' in command:
            person = command.replace('wikipedia','')
            talk('sir...according to wikipedia..')
            info = wikipedia.summary(person, 2)
            print(info)
            talk(info)

        elif 'tell me about' in command:
            information = command.replace('tell me about','')
            info = wikipedia.summary(information, 3)
            print(info)
            talk(info)

        elif 'what is' in command:
            thing = command.replace('what is','')
            info = wikipedia.summary(thing, 2)
            talk(info)
            print(info)

        elif 'how many' in command:
            count = command.replace('how many','')
            info = wikipedia.summary(count, 2)
            talk(info)
            print(info)

        elif 'where is' in command:
            place = command.replace('where is','')
            info = wikipedia.summary(place, 2)
            talk(info)
            print(info)

        elif 'how' in command:
            process = command.replace('how','')
            info = wikipedia.summary(process,2)
            talk(info)
            print(info)

        elif 'when' in command:
            history = command.replace('when','')
            info = wikipedia.summary(history,2)
            talk(info)
            print(info)

        elif 'do you want to date' in command:
            talk('Sorry,I am better without it')

        elif 'are you single' in command:
            talk('I am in a relationship with Wifi')

        elif 'joke' in command:
            result = pyjokes.get_joke()
            talk(result)
            print(result)

        elif 'repeat' in command:
            command = command.replace('repeat','')
            talk(command)
            print(command)

        elif 'alarm' in command:
            command = command.replace('alarm','')
            talk('what is remainder sir')
            s = take_command()
            print(s)
            talk('alarm' +command)
            datef.alarm(command)
            talk(s)

        elif 'who the hell are you' in command:
            talk('JARVIS the name is jarvis')
            print('JARVIS the name is jarvis')

        elif  'introduce yourself' in command:
            talk('I am Jarvis an AI based virtual assistant. Always ready to help you sir')
            print('I am Jarvis an AI based virtual assistant. Always ready to help you sir')

        elif  'where do you live' in command:
            talk('I wander around the world on internet to collect information for you. I live in your device and probably in your heart sir.')
            print('I wander around the world on internet to collect information for you. I live in your device and probably in your heart sir')

        elif 'what can you do' in command:
            talk('My job is to follow your command and do whatever you ask...sir')
            print('My job is to follow your command and do whatever you ask...sir')

        elif 'thank you' in command:
            stMsgs= ['Welcome sir...', 'my pleasure sir...','happy to help sir...']
            ans_q = random.choice(stMsgs)
            talk(ans_q)
            print(ans_q)

        elif 'created' in command:
            talk('I am created by sir rishabh shikari, and i am very thankful to him for creating me')
            print('I am created by sir rishabh shikari, and i am very thankful to him for creating me')

        elif 'hello' in command:
            stMsgs = ['hello sir..', 'at your service sir...', 'how may i help you sir..', 'yes sir']
            ans_q = random.choice(stMsgs)
            talk(ans_q)
            print(ans_q)

        elif 'propose' in command:
            talk('I Love You So much. Will You be my girlfriend')

        elif 'open youtube' in command:
            webbrowser.open('www.youtube.com')
            talk('opening youtube')

        elif 'close youtube' in command:
            command = command.replace('close', '')
            pyautogui.hotkey('ctrl', 'w')
            talk('closing' + command)

        elif 'open myclass' in command:
            webbrowser.open('https://myclass.lpu.in/')
            talk('opening myclass')

        elif 'close myclass' in command:
            command = command.replace('close', '')
            pyautogui.hotkey('ctrl', 'w')
            talk('closing' + command)

        elif 'stop' in command:
            pyautogui.press('space')

        elif 'resume' in command:
            pyautogui.press('space')

        elif 'volume up' in command:
            pyautogui.hotkey('volumeup','10')

        elif 'volume down' in command:
            pyautogui.hotkey('volumedown','9')

        elif 'volume mute' in command:
            pyautogui.hotkey('volumemute')

        elif 'open github' in command:
            webbrowser.open('https://www.github.com')
            talk('opening github')

        elif 'open telegram' in command:
            webbrowser.open('https://web.telegram.org/z/')
            talk('opening telegram')

        elif 'close telegram' in command:
            command = command.replace('close', '')
            pyautogui.hotkey('ctrl', 'w')
            talk('closing' + command)

        elif 'close gituhub' in command:
            command = command.replace('close', '')
            pyautogui.hotkey('ctrl', 'w')
            talk('closing' + command)


        elif 'open facebook' in command:
            webbrowser.open('https://www.facebook.com')
            talk('opening facebook')

        elif 'close facebook' in command:
            command = command.replace('close', '')
            pyautogui.hotkey('ctrl', 'w')
            talk('closing' + command)

        elif 'open instagram' in command:
            webbrowser.open('https://www.instagram.com')
            talk('opening instagram')

        elif 'close instagram' in command:
            command = command.replace('close', '')
            pyautogui.hotkey('ctrl', 'w')
            talk('closing' + command)

        elif 'open whatsapp' in command:
            webbrowser.open('https://web.whatsapp.com/')
            talk('opening whatsapp')

        elif 'close whatsapp' in command:
            command = command.replace('close', '')
            pyautogui.hotkey('ctrl', 'w')
            talk('closing' + command)

        elif 'open google' in command:
            webbrowser.open('https://www.google.com')
            talk('opening google')

        elif 'close google' in command:
            command = command.replace('close', '')
            pyautogui.hotkey('alt', 'f4')
            talk('closing' + command)

        elif 'locate' in command:
            place = command.replace('locate','')
            webbrowser.open('https://www.google.com/maps/place/'+place)
            talk('locating' +place)

        elif 'open yahoo' in command:
            webbrowser.open('https://www.yahoo.com')
            talk('opening yahoo')

        elif 'close yahoo' in command:
            command = command.replace('close', '')
            pyautogui.hotkey('alt', 'f4')
            talk('closing' + command)

        elif 'open gmail' in command:
            webbrowser.open('https://mail.google.com')
            talk('opening google mail')

        elif 'close gmail' in command:
            command = command.replace('close', '')
            pyautogui.hotkey('ctrl', 'w')
            talk('closing' + command)

        elif 'open snapdeal' in command:
            webbrowser.open('https://www.snapdeal.com')
            talk('opening snapdeal')

        elif 'close snapdeal' in command:
            command = command.replace('close', '')
            pyautogui.hotkey('ctrl', 'w')
            talk('closing' + command)

        elif 'open code' in command:
            codepath = 'C:\\Users\\mahakal\\AppData\\Local\Programs\\Microsoft VS Code\\Code'
            os.startfile(codepath)
            talk('opening code')

        elif 'close' in command:
            command = command.replace('close', '')
            pyautogui.hotkey('alt', 'f4')
            talk('closing' + command)

        elif 'open sanfoundary' in command:
            webbrowser.open('https://www.sanfoundry.com/')
            talk('opening sanfoundary sir...')

        elif 'open geekforgeeks' in command:
            webbrowser.open('https://www.geeksforgeeks.org/')
            talk('opening geekforgeeks sir...')

        elif 'close geekforgeeks' in command:
            command = command.replace('close', '')
            pyautogui.hotkey('ctrl', 'w')
            talk('closing' + command)

        elif 'search' in command:
            result = command.replace('search','')
            g_url = 'https://www.google.com/search?q='
            results = webbrowser.open(g_url+result,2)
            talk('searching sir..')
            print(results)

        elif 'open amazon' in command:
            webbrowser.open('https://www.amazon.com')
            talk('opening amazon')

        elif 'close amazon' in command:
            command = command.replace('close', '')
            pyautogui.hotkey('ctrl', 'w')
            talk('closing' + command)

        elif 'open flipkart' in command:
            webbrowser.open('https://www.flipkart.com')
            talk('opening flipkart')

        elif 'close flipkart' in command:
            command = command.replace('close', '')
            pyautogui.hotkey('ctrl', 'w')
            talk('closing' + command)

        elif 'open ebay' in command:
            webbrowser.open('https://www.ebay.com')
            talk('opening ebay')

        elif 'close ebay' in command:
            command = command.replace('close', '')
            pyautogui.hotkey('ctrl', 'w')
            talk('closing' + command)

        elif 'open stackoverflow' in command:
            webbrowser.open('https://stackoverflow.com/')
            talk('opening stackoverflow sir...')

        elif 'close stackoverflow' in command:
            command = command.replace('close', '')
            pyautogui.hotkey('ctrl', 'w')
            talk('closing' + command)

        elif 'goodbye' in command:
            stMsgs = ['goodbye sir, have a nice day', 'goodbye sir, take care', 'goodbye sir..., see you soon']
            ans_q = random.choice(stMsgs)
            talk(ans_q)
            print(ans_q)
            exit()

        elif 'forecast weather' in command:
            res = app.query(command)
            results = (next(res.results).text)
            print("today's weather is:" +results)
            talk("today's weather is:" +results)

        elif 'solve' in command:
            res = app.query(command)
            results = (next(res.results).text)
            print('solution is:' +results)
            talk('solution is:' +results)

        elif 'tell me a story' in command:
            res = app.query(command)
            results = (next(res.results).text)
            wikipedia.summary(next(res.results).text,2)
            print(results)
            talk(results)

        elif "today world" in command:
            res = app.query(command)
            results = (next(res.results).text)
            print(results)
            talk(results)

        elif 'leader of ' in command:
            res = app.query(command)
            results = (next(res.results).text)
            print(results)
            talk(results)

        elif "earthquakes" in command:
             res = app.query(command)
             results = (next(res.results).text)
             print(results)
             talk(results)

        elif "today's date" in command:
            res = app.query(command)
            results = (next(res.results).text)
            print("todays date is:" + results)
            talk("todays date is" + results)

        elif 'convert' in command:
            res = app.query(command)
            results = (next(res.results).text)
            print("solution is:" + results)
            talk("solution is" + results)


        else:
            talk('please repeat command sir')
