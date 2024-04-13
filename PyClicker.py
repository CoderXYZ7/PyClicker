#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 09:36:03 2024

@author: CoderXYZ7
"""

import tkinter as tk
import keyboard
import time

# Funzione per cambiare lo stato della variabile toggle
def toggle_variable():
    global toggle
    toggle = not toggle
    update_color()

# Funzione per aggiornare il colore del quadrato in base allo stato della variabile toggle
def update_color():
    if toggle:
        canvas.itemconfig(square, fill="blue")
    else:
        canvas.itemconfig(square, fill="red")

# Funzione per gestire l'input della tastiera
def key_pressed(event):
    global toggle, custom_delay
    if event.name == '0':
        toggle_variable()
    elif toggle and event.name == 'space':
        time.sleep(custom_delay)
        keyboard.press_and_release('c')

# Funzione per aggiornare il valore del ritardo personalizzato
def update_delay():
    global custom_delay
    try:
        custom_delay = float(delay_entry.get())
    except ValueError:
        # Se l'utente inserisce un valore non valido, mantieni il valore precedente
        delay_entry.delete(0, tk.END)
        delay_entry.insert(0, str(custom_delay))

# Creazione della finestra principale
root = tk.Tk()
root.title("Toggle Square")

# Creazione del canvas per disegnare il quadrato
canvas = tk.Canvas(root, width=100, height=100)
canvas.pack()

# Disegno del quadrato
square = canvas.create_rectangle(25, 25, 75, 75, fill="red")

# Inizializzazione della variabile toggle
toggle = False

# Inizializzazione del ritardo personalizzato
custom_delay = 0.5

# Aggiunta del binding per la pressione dei tasti
keyboard.on_press(key_pressed)

# Aggiunta del box di testo per il ritardo personalizzato
delay_label = tk.Label(root, text="Custom Delay:")
delay_label.pack()
delay_entry = tk.Entry(root)
delay_entry.pack()
delay_entry.insert(0, str(custom_delay))
delay_entry.bind("<Return>", lambda event: update_delay())

# Avvio del mainloop
root.mainloop()


