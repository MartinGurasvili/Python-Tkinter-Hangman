import tkinter
from tkinter import *
from PIL import ImageTk,Image
import random



guess = str()

wrong = 0

wordlist = ["dog","cat","bookkeeper","ant","phone","laptop","trainers","bottle","clock","speaker","keyboard","fortnight"]

word = wordlist[random.randint(0,len(wordlist)-1)]
displayword = "_ " * len(word)
print(word)


def check_guess():
    global img,wrong,title,display,displayword,word
    if(wrong <= 6-1):
            if(amount.get() in word):
                while amount.get() in word:
                    x = list(displayword)
                    x[int(word.index(amount.get()))*2] =amount.get()
                    displayword="".join(x)

                    x = list(word)
                    x[word.index(amount.get())] = "0"
                    word = "".join(x)   
               
                display.configure(text=displayword)
                if("_" not in displayword):
                    title.configure( text='You Won')
            else:
                wrong +=1
                img = ImageTk.PhotoImage(Image.open("{}.png".format(wrong)))
                canvas.create_image(20, 20, anchor=NW, image=img)
                
    else:
        display.configure( text='You lose')
        title.configure( text='You Killed Him! :(')

root = Tk()
root.title("Hangman")
root.minsize(width=450, height=450)
root.attributes("-alpha", 0.90)
root.configure(background="#282828")


title = Label(root, text='Guess The Letter', fg="red",font="Geneva 30",bg="#282828")
title.pack()

display = Label(root, text=displayword, fg="white",font="Geneva 40",bg="#282828")
display.pack()

canvas = Canvas(root, width = 250, height = 250,background="#282828",bd=0, highlightthickness=0)  
canvas.place(relx=0.37, rely=0.5, anchor=CENTER)

img = ImageTk.PhotoImage(Image.open("{}.png".format(wrong)))
canvas.create_image(20, 20, anchor=NW, image=img)


amount = Entry(root,textvariable=guess, fg="white", font="Geneva 25 bold",bg="#282828",justify=CENTER)
amount.place(relx=0.44, rely=0.9, anchor=CENTER)

enter = Button(root,text ="Guess", fg="#282828", font="Geneva 30 bold",bg='#54FA9B',activebackground='#282828',justify=CENTER,command = check_guess)
enter.configure(bg='#54FA9B')
enter.place(relx=0.85, rely=0.9, anchor=CENTER)


root.mainloop()