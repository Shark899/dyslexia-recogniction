from tkinter import *
from tkinter import ttk
import requests
from random import randint
from PIL import Image, ImageTk

im = Image.open("MARTI.jpg")
image1 = im.resize((500, 500))
list1 = ["nonno", "pollo", "masso", "notte", "pala", "rosa", "cane", "collo", "tonno", "panni"]
list2 = []
list3 = []
list4 = []


def submit(value):
    score = 0
    if len(list2) < 10:
        list2.append(value)
        insert.delete(0,END)
        print(list2)
    else:
        for i in range(0, len(list1)):
            if list1[i] == list2[i]:
                score += 1
        if score >= 8 and score <= 10:
           lab = Label(root, text=f"Your score is {score}/{len(list2)}. No DSA")
           lab.grid(row=5,column=0)
        elif score >= 5 and score <= 7:
            lab = Label(root, text=f"Your score is {score}/{len(list2)}. Probabilmente sei un ragazzo dislessico")
            lab.grid(row=5, column=0)
        else:
            lab =Label(root, text=f"Your score is {score}/{len(list2)}. Sei un ragazzo con DSA")
            lab.grid(row=5, column=0)


def get_random_name():
    r = requests.get('https://svnweb.freebsd.org/csrg/share/dict/propernames?revision=61766&view=co')
    text = r.text
    individual_word = text.split()
    random_number = randint(0, len(individual_word))
    return individual_word[random_number]


root = Tk()
root.title("Dislessia")

firstText = Label(root, text=f"Ciao {get_random_name()} sono chat bot come posso aiutarti ?")
firstText.grid(row=0, column=0)

secondText = Label(root, text="Devo completare una scheda formativa")
secondText.grid(row=1, column=0)

test = ImageTk.PhotoImage(image1)
label1 = Label(image=test)
label1.image = test
label1.grid(row=2, column=0)

insert = Entry(root)
insert.grid(row=3, column=0)

buttonInsert = Button(root, text="Entry", command=lambda: submit(insert.get()))
buttonInsert.grid(row=4, column=0)

root.mainloop()
