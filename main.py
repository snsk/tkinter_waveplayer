import os.path
import time
import tkinter
import wave
from tkinter import filedialog, messagebox, ttk

import pygame.mixer

root = None #root window
edit_box = None #pass value beyond function

def play_music():
    global edit_box
    global root

    filename = edit_box.get()
    pygame.mixer.music.load(filename)
    wf = wave.open(filename , "r" )
    wf_time = float(wf.getnframes()) / wf.getframerate()
    pygame.mixer.music.play()
    root.mainloop()
    time.sleep(wf_time)
    pygame.mixer.music.stop()

def stop_music():
    pygame.mixer.music.stop()

def music_file_open():
    global edit_box
    file_type = [("","*.wav")]
    current_dir = os.path.abspath(os.path.dirname(__file__))
    filepath = filedialog.askopenfilename(filetypes = file_type, initialdir = current_dir)
    edit_box.delete(0, tkinter.END)
    edit_box.insert(tkinter.END, filepath)

def main():
    global root
    global edit_box

    #root window 作成
    root = tkinter.Tk()
    root.title("My First Application Title")
    root.geometry("400x200")

    #Label 生成
    static_label_greeding = ttk.Label(text=u'Enter  file name', foreground='#000000', background='#ffffff')
    static_label_greeding.pack()
    #位置を指定したい場合は static_label_greeding.place(x=0, y=0)

    #edit_box 生成
    edit_box = ttk.Entry(width=320)
    edit_box.insert(tkinter.END, "whistle.wav")
    edit_box.pack()

    play_button = ttk.Button(text=u'play music', command=play_music, width=50)
    play_button.pack()
    stop_button = ttk.Button(text=u'stop music', command=stop_music, width=50)
    stop_button.pack()
    music_file_openButton = ttk.Button(text=u'file open', command=music_file_open, width=50)
    music_file_openButton.pack()

    pygame.mixer.init()
    root.mainloop()

if __name__ == '__main__':
    main()
