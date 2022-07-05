""" Разработать игру «Обратные крестики-нолики» на поле 10 x 10 с правилом «Пять в ряд» – проигрывает тот, у кого получился вертикальный, горизонтальный или диагональный ряд из пяти своих фигур (крестиков/ноликов).
Игра должна работать в режиме «человек против компьютера». """

from tkinter import *
import tkinter.messagebox as mb
from turtle import position


def show_warning():
    msg = "Сюда жать нельзя"
    mb.showwarning("Предупреждения", msg)

def update_label_text(event, label):
    if label['text'] == '':
        label['text'] = 'X'
        print(label.winfo_name())
        #label.nametowidget('01')["text"] = "O"
    else:
        show_warning()


window = Tk()

window.title("Reverce X-O")
window.geometry('220x230')



for i in range(10):
    for j in range(10):
        frame = Frame(
            master = window,
            relief = RAISED,
            borderwidth = 1
        )
        frame.grid(row=i, column=j)
        label = Label(master=frame, width=2, height=1, name=f"{i}-{j}")
        label.bind('<Button-1>', lambda event, label=label: update_label_text(event, label))
        label.pack()
window.mainloop()

