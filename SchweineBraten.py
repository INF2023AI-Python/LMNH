import RPi.GPIO as GPIO
import turtle
import random

# GPIO-Setup
GPIO.setmode(GPIO.BCM)
GREEN_LED_PIN = 24
RED_LED_PIN = 23
GPIO.setup(GREEN_LED_PIN, GPIO.OUT)
GPIO.setup(RED_LED_PIN, GPIO.OUT)

# Spielvariablen
words = ["raspberry", "python", "turtle", "gpio"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6  # Anzahl der erlaubten Fehler

# Turtle Setup
wn = turtle.Screen()
wn.title("Galgenmännchen")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def draw_guessed():
    t.clear()
    t.penup()
    t.goto(-150, -50)
    t.write(" ".join(guessed), font=("Arial", 24, "normal"))

def update_game_state():
    if "_" not in guessed:
        GPIO.output(GREEN_LED_PIN, GPIO.HIGH)  # Spieler hat gewonnen
        t.goto(-150, -100)
        t.write("Gewonnen!", font=("Arial", 24, "normal"))
        return True
    elif attempts == 0:
        GPIO.output(RED_LED_PIN, GPIO.HIGH)  # Spieler hat verloren
        t.goto(-150, -100)
        t.write("Verloren!", font=("Arial", 24, "normal"))
        t.goto(-150, -130)
        t.write(f"Das Wort war: {word}", font=("Arial", 24, "normal"))
        return True
    return False

def guess(letter):
    global attempts
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
    else:
        attempts -= 1
    draw_guessed()
    return update_game_state()

def main():
    draw_guessed()
    while True:
        user_guess = input("Rate einen Buchstaben: ").lower()
        if len(user_guess) != 1 or not user_guess.isalpha():
            print("Bitte gib genau einen Buchstaben ein.")
            continue
        if guess(user_guess):
            print("Spiel beendet.")
            break

if __name__ == "__main__":
    try:
        main()
    finally:
        wn.mainloop()
        GPIO.cleanup()  # Stelle sicher, dass die GPIO-Pins freigegeben werden
