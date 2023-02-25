import time
import pyautogui as py

import tkinter as tk
import customtkinter as ctk

def takeScreenshot():
    
    name = f"C:\\Users\\Lenovo\\Desktop\\Python_Projects\\ScreenshotApp\\screenshots\\{round(time.time())}.png"
    time.sleep(5)
    image = py.screenshot(name)

# takeScreenshot()

root = ctk.CTk()
root.title('ScreenShot Application')

frame = ctk.CTkFrame(root)

btnclick = ctk.CTkButton(root, fg_color='blue', text='Take a Screenshot', command=takeScreenshot)
btnclick.pack()

btnquit = ctk.CTkButton(root, fg_color='red', text='Quit', command=quit)
btnquit.pack()

root.mainloop()