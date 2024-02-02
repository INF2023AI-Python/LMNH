import RPi.GPIO as GPIO
import turtle
import random

# Setze die Pin-Nummerierung auf die GPIO-Bezeichnungen
GPIO.setmode(GPIO.BCM)
# Pin für die LED (Annahme: zweifarbige LED mit gemeinsamer Kathode)
GREEN_LED_PIN = 24  # Grünes LED
RED_LED_PIN = 23    # Rotes LED

# Setze die LED-Pins als Ausgang
GPIO.setup(GREEN_LED_PIN, GPIO.OUT)
GPIO.setup(RED_LED_PIN, GPIO.OUT)

# Wörter für das Spiel
words = ["raspberry", "python", "turtle", "gpio"]
# Wähle ein zufälliges Wort
word = random.choice(words)
# Erratene Buchstaben
guessed = ["_"] * len(word)

# Initialisiere Turtle
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

def guess(letter):
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
        draw_guessed()
        # Überprüfe, ob das Wort vollständig erraten wurde
        if "_" not in guessed:
            GPIO.output(GREEN_LED_PIN, GPIO.HIGH)  # Grünes Licht
            t.goto(-150, -100)
            t.write("Gewonnen!", font=("Arial", 24, "normal"))
    else:
        # Falscher Buchstabe, aktualisiere die Darstellung
        # Implementiere hier die Logik, um den Hangman zu zeichnen
        pass
    # Überprüfe, ob das Spiel verloren ist
    if "_" not in guessed:
        return
    # Hier könntest du zählen, wie viele Versuche noch übrig sind und entsprechend handeln
    # z.B. wenn keine Versuche mehr übrig sind:
    # GPIO.output(RED_LED_PIN, GPIO.HIGH)  # Rotes Licht

def main():
    draw_guessed()
    # Hier könntest du eine Schleife einbauen, die Benutzereingaben annimmt
    # Zum Beispiel (ohne tatsächliche Eingabeaufforderung):
    # guess("e")
    # Um es interaktiv zu machen, müsstest du eine Methode finden, die Eingaben über die Konsole oder
    # eine andere Schnittstelle liest, da turtle selbst keine direkte Methode für Texteingaben hat.

if __name__ == "__main__":
    main()
    wn.mainloop()

# Vergiss nicht, am Ende die GPIO-Pins freizugeben
GPIO.cleanup()
