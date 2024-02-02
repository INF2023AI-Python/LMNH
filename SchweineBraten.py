import RPi.GPIO as GPIO
import turtle
import random

# GPIO-Setup
GPIO.setmode(GPIO.BCM)
GREEN_LED_PIN = 24
RED_LED_PIN = 24  # Stelle sicher, dass du unterschiedliche Pins verwendest, falls du zwei LEDs hast.
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

# Initialisiere das Zeichnen des Galgens
def initialize_drawing():
    """Zeichnet das Grundgerüst des Galgens."""
    t.penup()
    t.goto(-75, -150)
    t.pendown()
    t.forward(150)  # Basis
    t.backward(75)
    t.left(90)
    t.forward(300)  # Stange
    t.right(90)
    t.forward(100)  # Querbalken
    t.right(90)
    t.forward(50)  # Kleine Stange

# Erratene Buchstaben anzeigen, ohne zu löschen
def draw_guessed():
    t.penup()
    t.goto(-200, -200)
    t.pendown()

# Update der Darstellung der erratenen Buchstaben
def update_guessed():
    t.clear()  # Lösche nur den Text der erratenen Buchstaben, nicht den Galgen
    draw_guessed()
    t.write(" ".join(guessed), font=("Arial", 24, "normal"))

# Hinzufügen der Teile des Galgenmännchens ohne Zurücksetzen
parts = [
    lambda: draw_head(),  # Kopf
    lambda: draw_body(),  # Körper
    lambda: draw_arm("left"),  # Linker Arm
    lambda: draw_arm("right"),  # Rechter Arm
    lambda: draw_leg("left"),  # Linkes Bein
    lambda: draw_leg("right"),  # Rechtes Bein
]

# Zeichnungsfunktionen für jedes Teil des Galgenmännchens
def draw_head():
    t.penup()
    t.goto(-25, 100)
    t.pendown()
    t.circle(20)

def draw_body():
    draw_line(-25, 80, -25, 40)

def draw_arm(side):
    if side == "left":
        draw_line(-25, 70, -55, 50)
    else:
        draw_line(-25, 70, 5, 50)

def draw_leg(side):
    if side == "left":
        draw_line(-25, 40, -45, 10)
    else:
        draw_line(-25, 40, -5, 10)

def draw_line(start_x, start_y, end_x, end_y):
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()
    t.goto(end_x, end_y)

# Update des Spielzustands ohne Zurücksetzen des Bildschirms
def update_game_state():
    global attempts
    update_guessed()
    if "_" not in guessed:
        GPIO.output(GREEN_LED_PIN, GPIO.HIGH)  # Spieler hat gewonnen
        return True
    elif attempts == 0:
        GPIO.output(RED_LED_PIN, GPIO.HIGH)  # Spieler hat verloren
        return True
    else:
        # Zeichne den nächsten Teil des Galgenmännchens
        part_index = 6 - attempts
        if part_index < len(parts):
            parts[part_index]()
    return False

# Spiellogik
def guess(letter):
    global attempts
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
    else:
        attempts -= 1
    return update_game_state()

def main():
    initialize_drawing()
    update_guessed()  # Initialisiere die Anzeige der erratenen Buchstaben
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
        GPIO.cleanup()
