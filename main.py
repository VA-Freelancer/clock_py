from tkinter import *
import time
from pathlib import Path

root = Tk()
root.iconbitmap(f'{Path.cwd()}/clock.ico')
def tick():
    watch.after(200, tick)
    watch['text'] = time.strftime("%H:%M:%S")

watch = Label(root, font="Arial 70")
watch.pack()

watch.after_idle(tick)

root.mainloop()