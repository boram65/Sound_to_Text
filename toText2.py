from curses.textpad import Textbox
import speech_recognition as sr
import librosa
from tkinter import *
from tkinter import filedialog


r = sr.Recognizer()

whdth, height = 500 , 150

tk = Tk()
tk.title("음성파일 -> 문자열")
tk.geometry('{0}x{1}'.format(whdth, height))
tk.resizable(False, False)

def event():
    path = filedialog.askopenfilename(filetypes=[('Sound File', '.wav'),('Sound File', '.mp3')])
    path = path.replace('\\','/')
    button['text'] = '파일 선택됨!'
    korean_audio = sr.AudioFile(path)
    with korean_audio as source:
        audio = r.record(source)
    label['text'] = r.recognize_google(audio_data=audio, language='ko-KR')
    
label = Label(tk, text='파일을 선택하면 문자로 바꿔줘요~', font=25)
button = Button(tk,text='음성파일 찾기',command=event)

label.pack(side=TOP, pady=20)
button.pack(side=BOTTOM, pady=20) #side로 배치설정, padx로 좌우 여백설정, pady로 상하 여백설정 


tk.mainloop()