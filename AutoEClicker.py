import tkinter as tk
import time
import threading
import keyboard

class SpamApp:
    def __init__(self, master):
        self.master = master
        master.title("Spamma E")

        self.delay_label = tk.Label(master, text="Ritardo (ms):")
        self.delay_label.pack()

        self.delay_entry = tk.Entry(master)
        self.delay_entry.insert(tk.END, "1000")  # Impostazione predefinita del ritardo a 1000 ms
        self.delay_entry.pack()

        self.spam_button = tk.Button(master, text="Spamm E", command=self.start_spamming)
        self.spam_button.pack()

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_spamming, state=tk.DISABLED)
        self.stop_button.pack()

        self.spamming_thread = None
        self.spamming = False

    def start_spamming(self):
        self.spam_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        delay = int(self.delay_entry.get()) / 1000.0  # Converti il ritardo da millisecondi a secondi
        self.spamming_thread = threading.Thread(target=self.spam_E, args=(delay,))
        self.spamming_thread.start()

    def stop_spamming(self):
        self.spamming = False
        self.spam_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def spam_E(self, delay):
        self.spamming = True
        while self.spamming:
            keyboard.press('e')
            time.sleep(0.1)  # Simula la pressione del tasto 'e'
            keyboard.release('e')
            time.sleep(delay)  # Aspetta il ritardo specificato

def main():
    root = tk.Tk()
    app = SpamApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
e
