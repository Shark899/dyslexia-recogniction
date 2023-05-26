from tkinter import *
import requests
from random import randint
from PIL import Image, ImageTk
import sys
import os

#loading images
im = Image.open("MARTI.jpg")
image1 = im.resize((500, 500))

im2 = Image.open("MARTI1.jpg")
image2 = im2.resize((500, 500))

#setting lists

list1 = ["nonno", "pollo", "masso", "notte", "pala", "rosa", "cane", "collo", "tonno", "panni"]
list2 = []
list3 = [[1, 7], [1, 3], [1, 6], [1, 3]]


def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

#prima scheda
def btn1Choose():
    button1Choose.destroy()
    button2Choose.destroy()
    firstText.destroy()
    secondText.destroy()
    test = ImageTk.PhotoImage(image1)
    label1 = Label(frame1,image=test)
    label1.image = test
    label1.grid(row=3, column=0)

    insert_label = Label(frame1, text=f"Inserisci la parola")
    insert_label.grid(row=4, column=0)

    insert = Entry(frame1,width=20,justify="center")
    insert.grid(row=5, column=0)

    buttonInsert = Button(frame1, text="Entry", command=lambda: submit(insert.get()))
    buttonInsert.grid(row=6, column=0)

    def submit(value):
        score = 0
        if len(list2) < 10:
            if insert.get() != "":
                list2.append(value)
                insert.delete(0, END)
                print(list2)
        else:
            for i in range(0, len(list1)):
                if list1[i] == list2[i]:
                    score += 1
            insert.destroy()
            insert_label.destroy()
            buttonInsert.destroy()
            buttonRestart = Button(frame1, text="Restart", command=lambda: restart_program())
            buttonRestart.grid(row=6, column=0)
            if score >= 8 and score <= 10:
                lab = Label(frame1, text=f"Your score is {score}/{len(list2)}. No DSA")
                lab.grid(row=5, column=0)
            elif score >= 5 and score <= 7:
                lab = Label(frame1, text=f"Your score is {score}/{len(list2)}. Probabilmente sei un ragazzo dislessico")
                lab.grid(row=5, column=0)
            else:
                lab = Label(frame1, text=f"Your score is {score}/{len(list2)}. Sei un ragazzo con DSA")
                lab.grid(row=5, column=0)


#seconda scheda
def btn2Choose():
    button1Choose.destroy()
    button2Choose.destroy()
    firstText.destroy()
    secondText.destroy()
    test = ImageTk.PhotoImage(image2)
    label1 = Label(frame1,image=test)
    label1.image = test
    label1.grid(row=3, column=0, columnspan=2)

    insertunit_label = Label(frame1, text="Unita")
    insertunit_label.grid(row=4, column=1)
    insertunit = Entry(frame1,justify="center")
    insertunit.grid(row=5, column=0)

    insertdec_label = Label(frame1, text="Decine")
    insertdec_label.grid(row=4, column=0)
    insertdec = Entry(frame1,justify="center")
    insertdec.grid(row=5, column=1)

    buttonInsert = Button(frame1, text="Entry", command=lambda: submit(insertunit.get(), insertdec.get()))
    buttonInsert.grid(row=6, column=0, columnspan=2)

    def submit(value, value1):
        score = 0
        if len(list2) < 4:
            if insertunit.get() and insertdec.get():
                list2.append([int(value), int(value1)])
                insertunit.delete(0, END)
                insertdec.delete(0, END)
                print(list2)
        else:
            for i in range(0, len(list3)):
                print(list3[i][0])
                print(list2[i][0])
                if list3[i][0] == list2[i][0] and list3[i][1] == list2[i][1]:
                    score += 1
            insertdec_label.destroy()
            insertunit_label.destroy()
            insertdec.destroy()
            insertunit.destroy()
            buttonInsert.destroy()
            buttonRestart = Button(frame1, text="Restart", command=lambda: restart_program())
            buttonRestart.grid(row=6, column=0)
            if score == 4:
                lab = Label(frame1, text=f"Your score is {score}/{len(list2)}. No DSA")
                lab.grid(row=5, column=0)
            else:
                lab = Label(frame1, text=f"Your score is {score}/{len(list2)}. DSA")
                lab.grid(row=5, column=0)


# richiedi il nome e randomizzalo dall'API
def get_random_name():
    r = requests.get('https://svnweb.freebsd.org/csrg/share/dict/propernames?revision=61766&view=co')
    text = r.text
    individual_word = text.split()
    random_number = randint(0, len(individual_word))
    return individual_word[random_number]

# INIZIO PROGRAMMA

root = Tk()
root.title("Dislessia")

frame1 = Frame(root)

frame1.grid(row=0,column=0,columnspan=2,padx=(10,10),pady=(10,10))

firstText = Label(frame1, text=f"Ciao {get_random_name()} sono chat bot come posso aiutarti ?")
firstText.grid(row=0, column=1)

secondText = Label(frame1, text="Devo completare una scheda formativa")
secondText.grid(row=1, column=1)

button1Choose = Button(frame1, text="Prima Scheda", command=btn1Choose)
button1Choose.grid(row=2, column=0)

button2Choose = Button(frame1, text="Seconda Scheda", command=btn2Choose)
button2Choose.grid(row=2, column=2)

root.mainloop()
