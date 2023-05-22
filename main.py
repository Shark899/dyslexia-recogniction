import simpleaudio as sa
from quiz import quiz,other_quiz
from PIL import Image

image1 = Image.open(r"./beer.png")
image1.show()

choice = 0
score = 0
words = ["tavolo", "lavandino", "torta"]
description = "Ti presenterò 3 parole avrai un tempo limite di 10 secondi a parola per riscriverla e premere Enter"

print("Ciao! Mi chiamo " + "Età" + ".")
print("Sono stato creato nel " + "2023" + ".")
print("Per favore, ricordami il tuo nome.")
print("Welcome to dyslexia recogniction")
print("1) Text Test ")
print("2) Speech Test ")
print("3) Dyslexia Quiz ")
print("4) Assete Presente")

choice = int(input("Select a test:(1,2,3 o 4)"))
if choice == 1:
    for i in range(0, len(words)):
        print(words[i])
        my_word = input("Inserisci la parola scritta sopra: ")
        if words[i] == my_word:
            score += 1
    if score == 3:
        print(f"Your score is: {score}/{len(words)}")
        print("You are not dyslexic")
    else:
        print(f"Your score is: {score}/{len(words)}")
        print("You are dyslexic")
if choice == 2:
    for i in range(0, len(words)):
        wave_obj = sa.WaveObject.from_wave_file(f"./{words[i]}.wav")
        play_obj = wave_obj.play()
        my_word = input("Inserisci la parola sentita: ")
        if words[i] == my_word:
            score += 1
    if score == 3:
        print(f"Your score is: {score}/{len(words)}")
        print("You are not dyslexic")
    else:
        print(f"Your score is: {score}/{len(words)}")
        print("You are dyslexic")
if choice == 3:
    answer = ""
    for i in quiz:
        print("Rispondi si o no")
        answer = input(f"{i}")
        if answer == "si":
            score += 1
    if score > 5 and score < 9:
        print(f"il tuo punteggio è:{score}/{len(quiz)}")
        print("Probabilmente sei dislessico")
    elif score > 9:
        print(f"il tuo punteggio è:{score}/{len(quiz)}")
        print("Sei sicuramente dislessico")
    else:
        print(f"il tuo punteggio è:{score}/{len(quiz)}")
        print("Non sei dislessico")
if choice == 4:
    answer = ""
    for i in other_quiz:
        print(f"{i}")
        answer = input("Assente  Presente  Molto Presente")
        answer = answer.lower()
        if answer == "assente":
            score += 1
    if score > 5 and score < 9:
        print(f"il tuo punteggio è:{score}/{len(other_quiz)}")
        print("Probabilmente sei dislessico")
    elif score > 9:
        print(f"il tuo punteggio è:{score}/{len(other_quiz)}")
        print("Sei sicuramente dislessico")
    else:
        print(f"il tuo punteggio è:{score}/{len(other_quiz)}")
        print("Non sei dislessico")