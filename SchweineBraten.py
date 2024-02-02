import turtle

def draw_hangman(step):
    if step == 1:
        turtle.forward(100)
    elif step == 2:
        turtle.right(180)
        turtle.forward(50)
    elif step == 3:
        turtle.right(90)
        turtle.forward(100)
    elif step == 4:
        turtle.right(90)
        turtle.forward(50)
    elif step == 5:
        turtle.right(90)
        turtle.forward(20)
    elif step == 6:
        turtle.right(90)
        turtle.circle(10)
    elif step == 7:
        turtle.right(180)
        turtle.circle(-10)
    elif step == 8:
        turtle.right(180)
        turtle.forward(30)
    elif step == 9:
        turtle.right(180)
        turtle.forward(15)
        turtle.right(60)
        turtle.forward(20)
    elif step == 10:
        turtle.right(180)
        turtle.forward(20)
        turtle.right(60)
        turtle.forward(15)
    elif step == 11:
        turtle.right(180)
        turtle.forward(15)
        turtle.right(240)
        turtle.forward(20)
    elif step == 12:
        turtle.right(180)
        turtle.forward(20)
        turtle.right(60)
        turtle.forward(15)
        turtle.right(120)
        turtle.forward(20)

def play_hangman(word):
    turtle.speed(1)
    turtle.penup()
    turtle.goto(-50, -50)
    turtle.pendown()

    guessed_letters = []
    attempts = 12

    while attempts > 0:
        guess = turtle.textinput("Galgenmännchen", "Rate einen Buchstaben: ")

        if guess in guessed_letters:
            turtle.write("Du hast diesen Buchstaben bereits geraten.\l", move=False, align="left", font=("Arial", 16, "normal"))
        elif guess in word:
            guessed_letters.append(guess)
            turtle.write("Gut geraten!", move=False, align="left", font=("Arial", 16, "normal"))
        else:
            attempts -= 1
            draw_hangman(12 - attempts + 1)

        if set(guessed_letters) == set(word):
            turtle.write("Du hast gewonnen!", move=False, align="left", font=("Arial", 16, "normal"))
            return

    turtle.write("Du hast verloren. Das Wort war: " + word, move=False, align="left", font=("Arial", 16, "normal"))

play_hangman("python")
turtle.done()