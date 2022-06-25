from tkinter import *

window = Tk()
window.minsize(height=100, width=200)
window.config(padx=20, pady=20)

window.title("Mile to Km Converter")
input = Entry()
input.grid(column=1, row=0)

label4 = Label(text=0)
label4.grid(row=1, column=1)


def miles_to_kilometer():
    km = float(input.get()) * 1.6
    label4['text'] = round(km, 2)






label = Label(text='is equal to')
label.grid(column=0, row=1)

label2 = Label(text='Miles')
label2.grid(row=0, column=2)

label3 = Label(text='Km')
label3.grid(row=1, column=2)

button= Button(text='Calculate', command=miles_to_kilometer)
button.grid(row=2, column=1)












window.mainloop()