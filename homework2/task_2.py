""" Разработать игру «Обратные крестики-нолики» на поле 10 x 10 с правилом «Пять в ряд» – проигрывает тот, у кого получился вертикальный, горизонтальный или диагональный ряд из пяти своих фигур (крестиков/ноликов).
Игра должна работать в режиме «человек против компьютера». """

from tkinter import *


window = Tk()

window.title("Reverce X-O")
window.geometry('240x270')

for i in range(10):
    for j in range(10):
        frame = Frame(
            master = window,
            relief = RAISED,
            borderwidth = 1
        )
        frame.grid(row=i, column=j, padx=1, pady=1)
        label = Label(master=frame, width=2, height=1)
        label.pack(padx=1, pady=1)

window.mainloop()

