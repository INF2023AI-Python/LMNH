import turtle
import RPi.GPIO as GPIO
import tkinter as tk
from tkinter import simpledialog

# GPIO Setup
LED_PIN = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)  # LED aus

# Initialisiere RGB LED
red = GPIO.PWM(LED_PIN, 100)  # Rot
green = GPIO.PWM(LED_PIN, 100)  # Grün

# Turtle Setup
window = turtle.Screen()
window.title("Galgenmännchen")

# Wortliste
word_list = ["beispiel", "raspberry", "python"]
secret_word = "raspberry"  # Kann zufällig aus der Liste gewählt werden
guessed_letters = []

# Turtle für die Darstellung des Galgenmännchens
t = turtle.Turtle()
t.hideturtle()

def setup():
    # Zeichne das Galgenmännchen-Grundgerüst
    pass

def update_display():
    # Aktualisiere die Darstellung für das Galgenmännchen und die erratenen Buchstaben
    pass

def check_win_loss():
    # Überprüfe, ob der Spieler gewonnen oder verloren hat
    pass

def guess_letter():
    # Lasse den Spieler einen Buchstaben eingeben und überprüfe diesen
    root = tk.Tk()
    root.withdraw()  # Verstecke das Tkinter-Hauptfenster
    letter = simpledialog.askstring("Input", "Gib einen Buchstaben ein:")
    root.destroy()
    if letter:
        guessed_letters.append(letter)
        update_display()
        check_win_loss()

def main():
    setup()
    while True:
        guess_letter()

if __name__ == "__main__":
    main()
