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




# richiedi il nome e randomizzalo dall'API
def get_random_name():
    r = requests.get('https://svnweb.freebsd.org/csrg/share/dict/propernames?revision=61766&view=co')
    text = r.text
    individual_word = text.split()
    random_number = randint(0, len(individual_word))
    return individual_word[random_number]








