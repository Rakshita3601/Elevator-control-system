from tkinter import*
import pyttsx3
import datetime
import speech_recognition as sr

a=Tk()
a.geometry("400x250")
a.title("DETAILS")
a.configure(bg="black")

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
name=1


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("GOOD MORNING")
    elif hour>=12 and hour<18:
        speak("GOOD AFTERNOON")
    else:
        speak("GOOD EVENING")
    speak("HELLO I AM LIFT HOW MAY I HELP YOU")  

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognising..")
        query=r.recognize_google(audio,language="en-in")
        print(f"user said:{query}\n")

    except Exception as e:
        print("Say that again please")
        return takeCommand
    return query

btn0=Button(a,text="G",bg="white")
btn0.place(x=10,y=10)
btn1=Button(a,text="1",bg="white")
btn1.place(x=10,y=40)
btn2=Button(a,text="2",bg="white")
btn2.place(x=10,y=70)
btn3=Button(a,text="3",bg="white")
btn3.place(x=10,y=100)
btn4=Button(a,text="4",bg="white")
btn4.place(x=10,y=130)
btn5=Button(a,text="5",bg="white")
btn5.place(x=10,y=160)
btn6=Button(a,text="6",bg="white")
btn6.place(x=40,y=10)
btn7=Button(a,text="7",bg="white")
btn7.place(x=40,y=40)
btn8=Button(a,text="8",bg="white")
btn8.place(x=40,y=70)
btn9=Button(a,text="9",bg="white")
btn9.place(x=40,y=100)
btn10=Button(a,text="10",bg="white")
btn10.place(x=40,y=130)
btn11=Button(a,text="11",bg="white")
btn11.place(x=40,y=160)


if name==1:
    wishMe()
    b=takeCommand()
    b
    if b==("ground floor") or b==("G floor"):
            speak("Taking you to floor G")
            btn0.after(200)
            btn0.configure(bg="white")
            btn0.after(200)
            btn0.configure(bg="red")
            speak("thank you")
    
    elif b==("first floor") or b==("1st floor"):
            speak("Taking you to floor one")
            btn1.after(200)
            btn1.configure(bg="white")
            btn1.after(200)
            btn1.configure(bg="red")
            speak("thank you")
    elif b==("second floor") or b==("2nd floor"):
            speak("Taking you to floor two")
            btn2.after(200)
            btn2.configure(bg="white")
            btn2.after(200)
            btn2.configure(bg="green")
            speak("thank you")
    elif b==("third floor") or b==("3rd floor"):
            speak("Taking you to floor three")
            btn3.after(200)
            btn3.configure(bg="white")
            btn3.after(200)
            btn3.configure(bg="blue")
            speak("thank you")
    elif b==("fourth floor") or b==("4th floor"):
            speak("Taking you to floor four")
            btn4.after(200)
            btn4.configure(bg="white")
            btn4.after(200)
            btn4.configure(bg="pink")
            speak("thank you")
    elif b==("fifth floor") or b==("5th floor"):
            speak("Taking you to floor five")
            btn5.after(200)
            btn5.configure(bg="white")
            btn5.after(200)
            btn5.configure(bg="green")
            speak("thank you")
    elif b==("sixth floor") or b==("6th floor"):
            speak("Taking you to floor six")
            btn6.after(200)
            btn6.configure(bg="white")
            btn6.after(200)
            btn6.configure(bg="orange")
            speak("thank you")
    elif b==("seventh floor") or b==("7th floor"):
            speak("Taking you to floor seven")
            btn7.after(200)
            btn7.configure(bg="white")
            btn7.after(200)
            btn7.configure(bg="purple")
            speak("thank you")
    elif b==("eight floor") or b==("8th floor"):
            speak("Taking you to floor eight")
            btn8.after(200)
            btn8.configure(bg="white")
            btn8.after(200)
            btn8.configure(bg="red") 
            speak("thank you")
    elif b==("nineth floor") or b==("9th floor"):
            speak("Taking you to floor nine")
            btn9.after(200)
            btn9.configure(bg="white")
            btn9.after(200)
            btn9.configure(bg="green")
            speak("thank you")
    elif b==("tenth floor") or b==("10th floor"):
            speak("Taking you to floor ten")
            btn10.after(200)
            btn10.configure(bg="white")
            btn10.after(200)
            btn10.configure(bg="green")
            speak("thank you")
    elif b==("eleventh floor") or b==("11th floor"):
            speak("Taking you to floor eleven")
            btn11.after(200)
            btn11.configure(bg="white")
            btn11.after(200)
            btn11.configure(bg="blue")
            speak("thank you")
    else:
        speak("sorry not available")

a.mainloop()