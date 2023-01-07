#Import Libraries
from tkinter import *

# Making Fonts
font1 = ("Comic Sans MS", 24)
font2 = ("Comic Sans MS", 18)
font3 = ("Arial", 14)

# Make 1st GUI Frame
root = Tk()
root.geometry("250x170")
root.title("Big Family 100")

# List of questions and their answers
Q = [
    "Makanan Khas Indonesia?",
    "Perabotan Rumah?",
    "Game Digital Sebelum Tahun 2000?",
    "Jurusan Perguruan Tinggi?",
    "Kata yang sering disingkat?"
]

A = {
    "A1": ["Rendang", "Gudeg", "Tempe Mendoan", "Kerak Telor", "Jalangkote", "Papeda", 
           "Pempek", "Pedak","Lapet", "Rawon"],
    "A2": ["Spatula", "Lemari", "Mesin Cuci", "Meja Makan", "Tempat Tidur", "Gayung",
           "Kloset", "Penanak Nasi", "Talenan", "Cobek"],
    "A3": ["Tekken", "Sonic the Hedgehog", "Super Mario", "Tetris", "Mega Man",
           "Pepsiman", "Crash Bandicoot", "Pac Man"],
    "A4": ["Aktuaria", "Sastra Prancis", "Teknik Elektro", "Metalurgi", "Ilmu Perpustakaan",
           "Ilmu Politik", "Kedokteran", "Akuntansi", "Teologi", "Matematika Terapan"],
    "A5": ["Yang", "On The Way", "Sebentar", "Pulang Pergi", "Deadline", "Tetap",
           "Dan Lain-lain", "By The Way", "Malas", "Tidak Apa-apa"]
}

# Count number of rows (for grid)
a, b, c, d, e = 0, 0, 0, 0, 0

############################################################################
# Basic Display
def display1():
    return [
        Label(root, text="1", font=font3).grid(row=1, column=0),
        Label(root, text="2", font=font3).grid(row=2, column=0),
        Label(root, text="3", font=font3).grid(row=3, column=0),
        Label(root, text="4", font=font3).grid(row=4, column=0),
        Label(root, text="5", font=font3).grid(row=5, column=0),
        Label(root, text="6", font=font3).grid(row=6, column=0),
        Label(root, text="7", font=font3).grid(row=7, column=0),
        Label(root, text="8", font=font3).grid(row=8, column=0),
        Label(root, text="9", font=font3).grid(row=9, column=0),
        Label(root, text="10", font=font3).grid(row=10, column=0),
        Label(root, text=None, font=font2).grid(row=11, column=0)
    ]

def display2():
    return [
        Label(root, text="1", font=font3).grid(row=1, column=0),
        Label(root, text="2", font=font3).grid(row=2, column=0),
        Label(root, text="3", font=font3).grid(row=3, column=0),
        Label(root, text="4", font=font3).grid(row=4, column=0),
        Label(root, text="5", font=font3).grid(row=5, column=0),
        Label(root, text="6", font=font3).grid(row=6, column=0),
        Label(root, text="7", font=font3).grid(row=7, column=0),
        Label(root, text="8", font=font3).grid(row=8, column=0),
        Label(root, text=None, font=font2).grid(row=9, column=0)
    ]

############################################################################
# Check your answer
def check1():
    global a
    if answer1.get() in A["A1"]:
        a+=1
        ans1 = answer1.get()
        A["A1"].remove(ans1)
        return Label(root, text=ans1, font=font3).grid(row=a, column=1)

def check2():
    global b
    if answer2.get() in A["A2"]:
        b+=1
        ans2 = answer2.get()
        A["A2"].remove(ans2)
        return Label(root, text=ans2, font=font3).grid(row=b, column=1)

def check3():
    global c
    if answer3.get() in A["A3"]:
        c+=1
        ans3 = answer3.get()
        A["A3"].remove(ans3)
        return Label(root, text=ans3, font=font3).grid(row=c, column=1)

def check4():
    global d
    if answer4.get() in A["A4"]:
        d+=1
        ans4 = answer4.get()
        A["A4"].remove(ans4)
        return Label(root, text=ans4, font=font3).grid(row=d, column=1)

def check5():
    global e
    if answer5.get() in A["A5"]:
        e+=1
        ans5 = answer5.get()
        A["A5"].remove(ans5)
        return Label(root, text=ans5, font=font3).grid(row=e, column=1)

############################################################################
# Show All
def showans1():
    global a
    a += 1
    if len(A["A1"]) != 0:
        ans1 = A["A1"].pop(0)
        return Label(root, text=ans1, font=font3).grid(row=a, column=1)
    else:
        return Button(root, text="Next Question", command=q2, font=font3).grid(row=15, column=1)

def showans2():
    global b
    b += 1
    if len(A["A2"]) != 0:
        ans2 = A["A2"].pop(0)
        return Label(root, text=ans2, font=font3).grid(row=b, column=1)
    else:
        return Button(root, text="Next Question", command=q3, font=font3).grid(row=15, column=1)

def showans3():
    global c
    c += 1
    if len(A["A3"]) != 0:
        ans3 = A["A3"].pop(0)
        return Label(root, text=ans3, font=font3).grid(row=c, column=1)
    else:
        return Button(root, text="Next Question", command=q4, font=font3).grid(row=15, column=1)

def showans4():
    global d
    d += 1
    if len(A["A4"]) != 0:
        ans4 = A["A4"].pop(0)
        return Label(root, text=ans4, font=font3).grid(row=d, column=1)
    else:
        return Button(root, text="Next Question", command=q5, font=font3).grid(row=15, column=1)

def showans5():
    global e
    e += 1
    if len(A["A5"]) != 0:
        ans5 = A["A5"].pop(0)
        return Label(root, text=ans5, font=font3).grid(row=e, column=1)
    else:
        return Button(root, text="Next Question", command=q6, font=font3).grid(row=15, column=1)

############################################################################
# 1st Question
def q1():
    global answer1, root

    root = Tk()
    root.title("EEN Night")
    root.geometry("385x520")

    answer1 = StringVar(root)
    Label(root, text=Q[0], font=font2).grid(row=0, column=1)
    display1()

    # Textbox to type answer & display answer
    Label(root, text=" Answer:", font=font3).grid(row=12, column=0)
    Entry(root, textvariable=answer1, font=font3).grid(row=12, column=1)
    Button(root, text="Check", command=check1, font=font3).grid(row=13, column=1)
    Button(root, text="Show Answers", command=showans1, font=font3).grid(row=14, column=1)

# 2nd Question
def q2():
    global answer2, root

    root = Tk()
    root.title("EEN Night")
    root.geometry("340x520")

    answer2 = StringVar(root)
    Label(root, text=Q[1], font=font2).grid(row=0, column=1)
    display1()

    # Textbox to type answer & display answer
    Label(root, text=" Answer:", font=font3).grid(row=12, column=0)
    Entry(root, textvariable=answer2, font=font3).grid(row=12, column=1)
    Button(root, text="Check", command=check2, font=font3).grid(row=13, column=1)
    Button(root, text="Show Answers", command=showans2, font=font3).grid(row=14, column=1)

# 3rd Question
def q3():
    global answer3, root

    root = Tk()
    root.title("EEN Night")
    root.geometry("490x465")

    answer3 = StringVar(root)
    Label(root, text=Q[2], font=font2).grid(row=0, column=1)
    display2()

    # Textbox to type answer & display answer
    Label(root, text=" Answer:", font=font3).grid(row=10, column=0)
    Entry(root, textvariable=answer3, font=font3).grid(row=10, column=1)
    Button(root, text="Check", command=check3, font=font3).grid(row=11, column=1)
    Button(root, text="Show Answers", command=showans3, font=font3).grid(row=12, column=1)

def q4():
    global answer4, root

    root = Tk()
    root.title("EEN Night")
    root.geometry("395x520")

    answer4 = StringVar(root)
    Label(root, text=Q[3], font=font2).grid(row=0, column=1)
    display1()

    # Textbox to type answer & display answer
    Label(root, text=" Answer:", font=font3).grid(row=12, column=0)
    Entry(root, textvariable=answer4, font=font3).grid(row=12, column=1)
    Button(root, text="Check", command=check4, font=font3).grid(row=13, column=1)
    Button(root, text="Show Answers", command=showans4, font=font3).grid(row=14, column=1)

def q5():
    global answer5, root

    root = Tk()
    root.title("EEN Night")
    root.geometry("400x520")

    answer5 = StringVar(root)
    Label(root, text=Q[4], font=font2).grid(row=0, column=1)
    display1()

    # Textbox to type answer & display answer
    Label(root, text=" Answer:", font=font3).grid(row=12, column=0)
    Entry(root, textvariable=answer5, font=font3).grid(row=12, column=1)
    Button(root, text="Check", command=check5, font=font3).grid(row=13, column=1)
    Button(root, text="Show Answers", command=showans5, font=font3).grid(row=14, column=1)

def q6():
    root = Tk()
    root.title("EEN Night")
    root.geometry("225x110")

    Label(root, text="EEN Night", font=font1).grid(row=0, column=0)
    Label(root, text="Thanks for Playing", font=font2).grid(row=1, column=0)

############################################################################
# Basic GUI Lookout
Label(root, text="EEN Night", font=font1).grid(row=0, column=0)
Label(root, text="December 18th, 2021", font=font2).grid(row=1, column=0)
Label(root, text=None).grid(row=2, column=0)
Button(root, text="Start the game?", font=font3, command=q1).grid(row=3, column=0)

root.mainloop()