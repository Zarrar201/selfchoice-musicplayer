from tkinter import *
from tkinter import filedialog
from pygame import mixer

class MusicPlayer:
    def __init__(self, window ):
        window.geometry('420x200'); window.title('Audio Player'); window.resizable(0,0)
        window.configure(bg="#a12d5c")
        Load = Button(window, text = 'Load',  width = 10, font = ('sans-serif', 10), command = self.load, bg="#ff99cc", fg="white", activebackground="#ff66b2")
        Play = Button(window, text = 'Play',  width = 10,font = ('sans-serif', 10), command = self.play, bg="#ff4da6", fg="white", activebackground="#ff1a8c")
        Pause = Button(window,text = 'Pause',  width = 10, font = ('sans-serif', 10), command = self.pause, bg="#ff3385", fg="white", activebackground="#e60073")
        Stop = Button(window ,text = 'Stop',  width = 10, font = ('sans-serif', 10), command = self.stop, bg="#cc0066", fg="white", activebackground="#b30059")
        Load.place(x=40,y=20);Play.place(x=170,y=20);Pause.place(x=300,y=20);Stop.place(x=170,y=60) 
        self.music_file = False
        self.playing_state = False
    def load(self):
        self.music_file = filedialog.askopenfilename()
    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state=True
        else:
            mixer.music.unpause()
            self.playing_state = False
    def stop(self):
        mixer.music.stop()
root = Tk()
app= MusicPlayer(root)
root.mainloop()