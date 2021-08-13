import speech_recognition as sr 
def SpeechToText():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        i=1
        k=0
        length_of_text=0
        with open('Speak1.txt','a') as f:
            f.truncate(0)
            while(i == 1):
                x='n'
                while(x=='n' or x=='N'):
                    print("Speak what you want to be typed in your file::::")
                    audio=r.listen(source)   #
                    # any audio file
                    try:
                        text=r.recognize_google(audio)
                        print('Is this you want to write ? ',format(text))
                        x=input("Y.Yes N. NO  ")
                    except:
                        print("Sorry Could not recognise")
                    if x=='y' or x=='Y':   
                        count = len(text) #2
                        f.seek(length_of_text) #6
                        length_of_text=length_of_text+count #8
                        f.write(text)
                        f.write(" ") 
                i=int(input("If you want to speak ? 1.Yes 0. No  "))
        k=int(input("If You want to print Content of your file ? 1.Yes 0.No "))
        if k==1:
            with open('Speak1.txt','r') as f1:
                print(f1.read())
def main():
    SpeechToText()
if __name__=='__main__':
    main()