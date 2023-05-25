import simpleaudio as sa
from quiz import quiz, other_quiz
import requests
from random import randint


def get_random_name():
    r = requests.get('https://svnweb.freebsd.org/csrg/share/dict/propernames?revision=61766&view=co')
    text = r.text
    individual_word = text.split()
    random_number = randint(0, len(individual_word))
    return individual_word[random_number]



score = 0
name = get_random_name()
words = ["tavolo", "lavandino", "torta"]
description = "Ti presenterò 3 parole avrai un tempo limite di 10 secondi a parola per riscriverla e premere Enter"

print(f"Ciao {name}! Mi chiamo Bot , come posso aiutarti?")

print("1) Text Test ")
print("2) Speech Test ")
print("3) Dyslexia Quiz ")
print("4) Assente Presente")

choice = int(input("Select a test:(1,2,3 o 4)"))
if choice == 1:
    for i in range(0, len(words)):
        print(words[i])
        my_word = input("Inserisci la parola scritta sopra: ")
        if words[i] == my_word:
            score += 1
    if score == 3:
        print(f"Il tuo punteggio è: {score}/{len(words)}")
        print("Non sei dislessico")
    elif score == 2:
        print(f"Il tuo punteggio è: {score}/{len(words)}")
        print("C'è una probabilità che tu sia DSA ")
    else:
        print(f"Il tuo punteggio è: {score}/{len(words)}")
        print("Sei uno studente con disturbo DSA ")
if choice == 2:
    for i in range(0, len(words)):
        wave_obj = sa.WaveObject.from_wave_file(f"./{words[i]}.wav")
        play_obj = wave_obj.play()
        my_word = input("Inserisci la parola sentita: ")
        if words[i] == my_word:
            score += 1
    if score == 3:
        print(f"Il tuo punteggio è: {score}/{len(words)}")
        print("Non sei uno studente con disturbo DSA")
    elif score == 2:
        print(f"Il tuo punteggio è: {score}/{len(words)}")
        print("C'è una probabilità che tu sia DSA ")
    else:
        print(f"Il tuo punteggio è: {score}/{len(words)}")
        print("Sei uno studente con disturbo DSA ")
if choice == 3:
    answer = ""
    for i in quiz:
        print("Rispondi si o no")
        answer = input(f"{i}")
        if answer == "si":
            score += 1
    if score > 5 and score < 9:
        print(f"il tuo punteggio è:{score}/{len(quiz)}")
        print("Probabilmente sei uno studente con DSA")
    elif score > 9:
        print(f"il tuo punteggio è:{score}/{len(quiz)}")
        print("Sei uno studente con DSA")
    else:
        print(f"il tuo punteggio è:{score}/{len(quiz)}")
        print("Non sei uno studente DSA")
if choice == 4:
    answer = ""
    for i in other_quiz:
        print(f"{i}")
        answer = input("Assente  Presente  Molto Presente \n")
        answer = answer.lower()
        if answer == "presente":
            score += 0.5
        elif answer == "molto presente":
            score += 1
    if 5 < score < 9:
        print(f"il tuo punteggio è:{score}/{len(other_quiz)}")
        print("Probabilmente sei dislessico")
    elif score >= 9:
        print(f"il tuo punteggio è:{score}/{len(other_quiz)}")
        print("Sei sicuramente dislessico")
    else:
        print(f"il tuo punteggio è:{score}/{len(other_quiz)}")
        print("Non sei dislessico")
