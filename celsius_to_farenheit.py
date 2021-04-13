# Andrew Hein
# Advanced Programming - Week 10
# 2021/3/29
# celsius_to_farenheit.py

import tkinter as tk


def convert(celsiusTemp):  # Conversion Function
    return round((9/5)*celsiusTemp + 32, 1)


def convert_clicked():  # Onclick event
    value = inputBox.get()
    try:
        temp = float(value)
        fhOutput.set(convert(temp))
    except:
        fhOutput.set("Conversion Error!")


# TK Window
window = tk.Tk()
window.geometry("400x100")

# Modifiable String Vars
celsInput = tk.StringVar(None)
fhOutput = tk.StringVar(None)

# Labels
label1 = tk.Label(window, text="Enter the Celsius temperature:")
label1.grid(row=0, column=0)

label2 = tk.Label(window, text="Farenheit temperature:")
label2.grid(row=1, column=0)

# IO boxes
inputBox = tk.Entry(window, textvariable=celsInput,
                    width=15)
inputBox.grid(row=0, column=1)

outputBox = tk.Label(window, textvariable=fhOutput)
outputBox.grid(row=1, column=1)

# Buttons
btnConvert = tk.Button(
    window, text="Convert to Farenheit", command=convert_clicked)
btnConvert.grid(row=2, column=0)

btnQuit = tk.Button(window, text="Quit", command=quit)
btnQuit.grid(row=2, column=1)

# Begin
window.mainloop()
