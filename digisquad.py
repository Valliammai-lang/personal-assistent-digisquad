import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from time import ctime
import random
import requests
import smtplib
from ecapture import ecapture as ec



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

class person:
    name = ""
    def setName(name):
        name = name


def there_exists(terms):
    for term in terms:
        if term in query:
            return True
def WishMe():

    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        return speak("good morning")
    elif hour >= 12 and hour < 18:
        return speak("good afternoon")
    else:
        return speak("good evening")
    return speak("hii valli,i am your personal assistent.how can i help you?")


def takeCommand(ask=False):

    r = sr.Recognizer()
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        print("listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")
    except Exception as e:
        print("say again please...")
        return "None"
    except sr.RequestError:
        print('sorry,my speech service is down')
    return query.lower()

WishMe()
while True:

        query = takeCommand().lower()

        if there_exists(['hey','hai','hello']):
            greeting = [f"hey,how can i help you {person_name}",f"hey,what's up {person_name}",f"i'm listening {person_name}",f"hello {person_name}"]
            greet = greeting[random.randint(0,len(greeting)-1)]
            speak(greet)
            print(greet)

        if there_exists(["what is your name","what's your name","tell me your name"]):
            if person.name:
                 print('my name is digitsquad')
                 speak('my name is digitsquad')
            else:
                print('my name is digitsquad,what is your name?')
                speak('my name is digitsquad,what is your name?')

        if there_exists(["my name is"]):
            person_name = query.split("is")[-1].strip()
            speak(f"okey,i will remember that {person_name}")
            print(f"okey,i will remember that {person_name}")
            person.setName(name = person_name)
        if 'who are you' in query or 'what can you do' in query:
            print('I am digitsqad version 1 point O your virtual assistant. I am programmed to do minor tasks like'
                  'opening youtube,google chrome,send email and open facebook ,predict time,take a photo,search wikipedia, predict weather'
                  'in different cities , get top headline news from CNN and you can ask me computational or geographical questions too!')
            speak('I am digitsqad version 1 point O your virtual assistant. I am programmed to do minor tasks like'
                  'opening youtube,google chrome,send email and open facebook ,predict time,take a photo,search wikipedia, predict weather'
                  'in different cities , get top headline news from CNN and you can ask me computational or geographical questions too!')
        elif "who made you" in query or "who created you" in query or "who discovered you" in query:
            print("I was built by Adrijan")
            speak("I was built by Adrijan")
        if  'what time is it' in query:
            print(ctime())
            speak(ctime())

        if there_exists(["how are you","how are you doing"]):
            speak(f"im very well,thanks for asking {person_name}")
            print(f"im very well,thanks for asking {person_name}")

        elif 'wikipedia' in query:
            try:
                speak('Searching Wikipedia...')
                query= query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=3)
                print("According to Wikipedia")
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                s = random.choice(e.options)
                print(s)
                speak(s)
            except wikipedia.exceptions.WikipediaException as e:
                print('Search not include, try again wikipedia and your search')
            else:
                continue

        if 'search' in query:
            search = takeCommand('what do you want to search {person.name}?')
            url = 'https://google.com/search?q=' + search
            webbrowser.get().open(url)
            print('here is what i found for/t' + search)

        if 'find location for' in query:
            location = takeCommand('what is the location')
            url = 'https://www.google.com/maps/place/'+ location + '/&amp;'
            webbrowser.get().open(url)
            print(f"here is the location of/t" + location)

        elif "open facebook" in query:
            webbrowser.open_new_tab("https://sl-si.facebook.com/")
            print("Facebook is open now")
            speak("Facebook is open now")


        elif 'news' in query:
            news = webbrowser.open_new_tab("https://edition.cnn.com/")
            print('Here are some headlines from the CNN,Happy reading')
            speak('Here are some headlines from the CNN,Happy reading')

        elif "weather" in query:
            api_key = "394d4ebf0a7de20604147666d665d2d0"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            print("Whats the city name")
            speak("whats the city name")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(city_name + " Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))
                speak(city_name + " Temperature in kelvin unit is" +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
            else:
                print(" City Not Found\n")
                speak(" City Not Found ")

        if there_exists(["game"]):
            query = takeCommand("choose among rock paper or scissor")
            moves = ["rock", "paper", "scissor"]

            cmove = random.choice(moves)
            pmove = query

            speak("The computer chose " + cmove)
            print("The computer chose " + cmove)
            speak("You chose " + pmove)
            print("You chose " + pmove)
            # engine_speak("hi")
            if pmove == cmove:
                speak("the match is draw")
                print("the match is draw")
            elif pmove == "rock" and cmove == "scissor":
                speak("Player wins")
                print("Player wins")
            elif pmove == "rock" and cmove == "paper":
                speak("Computer wins")
                print("Computer wins")
            elif pmove == "paper" and cmove == "rock":
                speak("Player wins")
                print("Player wins")
            elif pmove == "paper" and cmove == "scissor":
                speak("Computer wins")
                print("Computer wins")
            elif pmove == "scissor" and cmove == "paper":
                speak("Player wins")
                print("Player wins")
            elif pmove == "scissor" and cmove == "rock":
                speak("Computer wins")
                print("Computer wins")

        if there_exists(["plus", "minus", "multiply", "divide", "power", "+", "-", "*", "/"]):
            opr = query.split()[1]

            if opr == '+':
                result = int(query.split()[0]) + int(query.split()[2])
                speak(result)
                print(result)
            elif opr == '-':
                result = int(query.split()[0]) - int(query.split()[2])
                speak(result)
                print(result)
            elif opr == 'multiply' or 'x':
                result = (int(query.split()[0]) * int(query.split()[2]))
                speak(result)
                print(result)
            elif opr == 'divide':
                result = (int(query.split()[0]) / int(query.split()[2]))
                speak(result)
                print(result)
            elif opr == 'power':
                result = (int(query.split()[0]) ** int(query.split()[2]))
                speak(result)
                print(result)
            else:
                speak("Wrong Operator")
                print("Wrong Operator")

        if there_exists(["where am i"]):
            Ip_info = requests.get('https://api.ipdata.co?api-key=test').json()
            loc = Ip_info['region']
            speak(f"You must be somewhere in {loc}")

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "robo camera", "img.jpg")
            print('Here is your photo')
            speak('Here is your photo')

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open gmail' in query:
            webbrowser.open_new_tab("https://bit.ly/3iOcR5z")
            print("Google Mail open now")
            speak("Google Mail open now")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\svais\\OneDrive\\Desktop\\song'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[2]))
        elif "joke" in query:
            with open("jokes.txt", "r") as m:
                sents = m.read().split("\n\n")
                se = random.choice(sents)
                print(se)
                speak(se)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Mam, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\kishancjx\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif there_exists(["exit", "quit", "goodbye"]):
                speak("bye")
                print("bye")
                exit()
            # you should enter your path here




if __name__ == "__main__":
    app.run()
