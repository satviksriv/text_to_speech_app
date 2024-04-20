import win32com.client

if __name__ == '__main__':
    speaker = win32com.client.Dispatch("SAPI.SpVoice")

    speaker.Speak("Hello. This is a text to speech application made by Satvik Srivastava using python.")
    speaker.Speak("Enter the command after the prompt and it will be converted into speech.")
    speaker.Speak("However, if you want to exit the application, just press q after the prompt")

    while True:
        x = input("Enter the command you want me to speak: ")
        if x == "q":
            speaker.Speak("Exiting the application, have a nice day!")
            break
        speaker.Speak(x)