import simpleaudio as sa


choice = 0
score = 0
words = ["tavolo", "lavandino", "torta"]
description = "Ti presenterò 3 parole avrai un tempo limite di 10 secondi a parola per riscriverla e premere Enter"
print("Welcome to dyslexia recogniction")
print("1) Text Test ")
print("2) Speech Test ")
choice = int(input("Select a test:(1 or 2)"))
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
    for i in range(0,len(words)):
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