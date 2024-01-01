import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboAudio 1.1")
    engine = pyttsx3.init()
    while True:
        enter = input("What you want me to speak:")
        if enter == "exit":
            engine.say("Goodbye dear Friend")
            engine.runAndWait()
            break
        engine.say(enter)
        engine.runAndWait()
        
        
        