# from tkinter import *
import tkinter as Tk
from tkinter import Listbox
from tkinter import messagebox



def MainMenuToControlStructures(frame1):
    frame1.destroy()
    ControlStructures()

def ifstateToMain(frame1,frame2,frame3,frame4,frame5,frame6):
    frame1.destroy()
    frame2.destroy()
    frame3.destroy()
    frame4.destroy()
    frame5.destroy()
    frame6.destroy()
    MainMenu()

def ifstateToWhile(frame1,frame2,frame3,frame4,frame5,frame6):
    frame1.destroy()
    frame2.destroy()
    frame3.destroy()
    frame4.destroy()
    frame5.destroy()
    frame6.destroy()
    WhilePage()


def ifstateToNested(frame1,frame2,frame3,frame4,frame5,frame6):
    frame1.destroy()
    frame2.destroy()
    frame3.destroy()
    frame4.destroy()
    frame5.destroy()
    frame6.destroy()
    NestedPage()

def MainMenuToIteration(frame1):
    frame1.destroy()
    IterationPage()

def ifstateToNestedFor(frame1,frame2,frame3,frame4,frame5,frame6):
    frame1.destroy()
    frame2.destroy()
    frame3.destroy()
    frame4.destroy()
    frame5.destroy()
    frame6.destroy()
    NestedForPage()

def MainMenuToClasses(frame1):
    frame1.destroy()
    ClassPage()


def MainMenuToInheritance(frame1):
    frame1.destroy()
    InheritancePage()


def RunProgram1(entry1, entry2):
    x = entry1.get()
    y = entry2.get()

    print(x)
    print(y)

    if x == "3" and y == "2":
        print("Great Job")
        messagebox.showinfo("You Did It", "Great Job")

    elif x == "6" and y == "4":
        print("Go Big Or Go Home")
        messagebox.showinfo("That's Big!", "Steady On, Let's Divide That By Two")

    else:
        print("That wasn't quite right. Try again")
        messagebox.showerror("Not Quite", "That wasn't quite right. Try again")





def RunProgram2(entry1, entry2):

    X = entry1.get()
    Y = entry2.get()
    X = int(X)
    Y = int(Y)


    Xrise = int(0)
    YFall = int(0)
    while X <= 6 and Y >=5:
        X +=1
        Y -= 1
        Xrise +=1
        YFall+=1

    print(X)
    print(Y)
    print(Xrise)
    print(YFall)
    Xrise = str(Xrise)
    YFall = str(YFall)
    if Xrise == "5" and YFall == "5":

        messagebox.showinfo("Great Job", "You did it!, X increased by " + Xrise + " And Y Fell by "+ YFall)

    else:
        messagebox.showerror("Not Quite", "Almost, X increased by " + Xrise + " And Y fell by " + YFall)




def RunProgram3(entry1):


    X = entry1.get()
    X = int(X)
    if X > 10:
        if X >= 100:
            messagebox.showerror("Bad News", "Not Quite, Try a Smaller Number")
        else:
            messagebox.showinfo("Nice!", "Good Job, Your number is between 100 and 10")
    else:
        messagebox.showerror("Bad News", "Not Quite, That number is abit small")



def RunProgram4(entry1):

    X = entry1.get()
    i =12
    i = int(i)
    X = int(X)

    for x in range(X):
        i-=2

    if i == 0:
        messagebox.showinfo("Nice!", "Good job!")

    elif i > 0:
        messagebox.showerror("That Wasn't Right","Not Quite, Try a Larger Number")

    else:
        messagebox.showerror("That Wasn't right","Try A Smaller Number")



def RunProgram5(entry1, entry2):


   X = entry1.get()
   Y = entry2.get()
   i = 0
   b = 0
   X = int(X)
   Y = int(Y)


   for x in range(X):
       for y in range(Y):
           i +=1
       b +=1


   if (i + b) > 20 and (i + b) < 100:
       messagebox.showinfo("NICE", "Great Job!")

   elif (i + b) < 20:
       messagebox.showerror("Oh no", "Try Bigger Variables")

   else:
       messagebox.showerror("Oh no", "Try Some Smaller Variables")



class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def introduction(self):
        messagebox.showinfo("Hello", "My name is " + self.name)

def RunProgram6(entry1, entry2, entry3):
    x = entry1.get()
    y = entry2.get()
    z = entry3.get()

    x = str(x)
    y = str(y)
    z = int(z)


    p1 = Person(x, y, z)

    p1.introduction()

class Hero(Person):

    def __init__(self, name, gender, age, superpower):
        Person.__init__(self, name, gender, age)
        self.power = superpower

    def GetHero(self):
        messagebox.showinfo("Hello Hero", "Hello, my name is " + self.name + " and my power is " + self.power)


def RunProgram7(entry1, entry2, entry3, entry4):
    x = entry1.get()
    y = entry2.get()
    z = entry3.get()
    P = entry4.get()

    x = str(x)
    y = str(y)
    z = int(z)
    P = str(P)



    p2 = Hero(x, y, z, P)

    p2.GetHero()







def StartSys():
    global window
    window = Tk.Tk()
    window.title("Project 1")
    window.geometry("800x800+0+0")
    window.configure(background="#76dd54")
    window.resizable(width=False, height=False)

def MainMenu():

    frame1 = Tk.Frame(window)
    frame1.pack()
    frame1.config(bg="#76dd54")

    MainMenuHeader = Tk.Label(frame1, padx=80, background="#76dd54", text="Python Learning Program",
                              font=("Helvetica", 40, "bold"), fg="black").grid(row=1, column=1)
    MainMenuSubHeader = Tk.Label(frame1, padx=80, background="#76dd54", text="Let's Get Learning!""\n",
                                 font=("Helvetica", 20), fg="black").grid(row=2, column=1)
    button2 = Tk.Button(frame1, text="Control Structures", font = (12), height=5, width=50,
                        command=lambda: MainMenuToControlStructures(frame1)).grid(row=4, column=1)
    button3 = Tk.Button(frame1, text="Iteration", font = (12), height=5, width=50,
                        command=lambda: MainMenuToIteration(frame1)).grid(row=5, column=1)
    button4 = Tk.Button(frame1, text="Classes",font = (12), height=5, width=50,
                        command=lambda: MainMenuToClasses(frame1)).grid(row=6, column=1)
    button5 = Tk.Button(frame1, text="Inheritance",font = (12), height=5, width=50,
                        command=lambda: MainMenuToInheritance(frame1)).grid(row=7, column=1)

    window.mainloop()


def ControlStructures():
    frame1 = Tk.Frame(window)
    frame1.pack()
    frame1.config(bg="#76dd54")

    MainMenuHeader = Tk.Label(frame1, padx=80, background="#76dd54", text="Control Structures",
                              font=("Helvetica", 40, "bold"), fg="black").grid(row=1, column=1)
    MainMenuSubHeader = Tk.Label(frame1, padx=80, background="#76dd54", text="If/elif/else Statements""\n""\n",
                                 font=("Helvetica", 20), fg="black").grid(row=2, column=1)
    label2 = Tk.Label(frame1, background="#76dd54", font=("Helvetica", 13), fg="black",
                      text="An If statement is the most common control structure used in Python. ""\n" "An If statement examines one or more boolean expressions "
                           "to determine whether or not that are true.""\n" "The outcome of this examination determines what code will be executed").grid(
        row=4, column=1)

    frame2 = Tk.Frame(window)
    frame2.pack()
    frame2.config(bg="#76dd54")
    listbox1 = Tk.Listbox(frame2, width=40, height=10)
    listbox1.grid(row=1, column=1)
    listbox1.insert(1, "X = (Your input here)")
    listbox1.insert(2, "Y = (Your input here)")
    listbox1.insert(3, " ")
    listbox1.insert(4, "if X == 3 and Y == 2:")
    listbox1.insert(5, "    print(Great Job)")
    listbox1.insert(6, " ")
    listbox1.insert(7, "else:")
    listbox1.insert(8, "    print(That wasn't quite right. Try again)")

    frame3 = Tk.Frame(window)
    frame3.pack()
    frame3.config(bg="#76dd54")

    label3 = Tk.Label(frame3, background="#76dd54", font=("Helvetica", 13), fg="black",
                      text="Let's try and get the output (Great Job)").grid(row=1, column=1)

    frame4 = Tk.Frame(window)
    frame4.pack()
    frame4.config(bg="#76dd54")

    label4 = Tk.Label(frame4, background="#76dd54", font=("Helvetica", 9), fg="black", text="X = ").grid(row=2,
                                                                                                         column=1,
                                                                                                         sticky=Tk.E)
    entry1 = Tk.Entry(frame4)
    entry1.grid(row=2, column=2, sticky=Tk.W)

    label5 = Tk.Label(frame4, background="#76dd54", font=("Helvetica", 9), fg="black", text="Y = ").grid(row=3,
                                                                                                         column=1,
                                                                                                         sticky=Tk.E)
    entry2 = Tk.Entry(frame4)
    entry2.grid(row=3, column=2, sticky=Tk.W)

    frame5 = Tk.Frame(window)
    frame5.pack()
    frame5.config(bg="#76dd54")

    button1 = Tk.Button(frame5, text="Run Code!", height=3, width=40, command=lambda: RunProgram1(entry1, entry2)).grid(
        row=1, column=1)

    frame6 = Tk.Frame(window)
    frame6.pack()
    frame6.config(bg="#76dd54")

    button2 = Tk.Button(frame6, text = "Next Page", height = 2, width = 30, command = lambda: ifstateToWhile(frame1,frame2,frame3,frame4,frame5,frame6))
    button2.grid(row=1,column=2, sticky = Tk.S)
    button3 = Tk.Button(frame6, text = "Return Home", height = 2, width = 30, command = lambda: ifstateToMain(frame1, frame2, frame3, frame4, frame5, frame6))
    button3.grid(row=1,column=1, sticky = Tk.S)






def WhilePage():
    frame1 = Tk.Frame(window)
    frame1.pack()
    frame1.config(bg="#76dd54")

    MainMenuHeader = Tk.Label(frame1, padx=80, background="#76dd54", text="Control Structures",
                              font=("Helvetica", 40, "bold"), fg="black").grid(row=1, column=1)
    MainMenuSubHeader = Tk.Label(frame1, padx=80, background="#76dd54", text="While Loops""\n""\n",
                                 font=("Helvetica", 20), fg="black").grid(row=2, column=1)

    label2 = Tk.Label(frame1, background="#76dd54", font=("Helvetica", 13), fg="black",
                      text="A While loop is one of the most simple forms of itterating through code""\n"
                      "A while Loop allows certain code to be ran multiple times while""\n"
                      "a certain condition is being met.").grid(row=4, column=1)

    frame2 = Tk.Frame(window)
    frame2.pack()
    frame2.config(bg="#76dd54")
    listbox1 = Tk.Listbox(frame2, width=40, height=15)
    listbox1.grid(row=1, column=1)
    listbox1.insert(1, "X = (Your input here)")
    listbox1.insert(2, "Y = (Your input here)")
    listbox1.insert(3, "Xrise = 0")
    listbox1.insert(4, "YFall = 0")
    listbox1.insert(5, " ")
    listbox1.insert(6, "while X <= 6 and Y >=5:")
    listbox1.insert(7, "    X +=1")
    listbox1.insert(8, "    Y -= 1")
    listbox1.insert(9, "    Xrise +=1")
    listbox1.insert(10, "   YFall +=1")
    listbox1.insert(11, " ")
    listbox1.insert(12, "if Xrise == 5 and YFall == 5:")
    listbox1.insert(13, "   Print(Great Job!)")
    listbox1.insert(14, "else: ")
    listbox1.insert(15, "   Print(Not Quite)")

    frame3 = Tk.Frame(window)
    frame3.pack()
    frame3.config(bg="#76dd54")

    label3 = Tk.Label(frame3, background="#76dd54", font=("Helvetica", 13), fg="black",
                      text="Let's try and get the output (Great Job)").grid(row=1, column=1)

    frame4 = Tk.Frame(window)
    frame4.pack()
    frame4.config(bg="#76dd54")

    label4 = Tk.Label(frame4, background="#76dd54", font=("Helvetica", 9), fg="black", text="X = ").grid(row=2,
                                                                                                         column=1,
                                                                                                         sticky=Tk.E)
    entry1 = Tk.Entry(frame4)
    entry1.grid(row=2, column=2, sticky=Tk.W)

    label5 = Tk.Label(frame4, background="#76dd54", font=("Helvetica", 9), fg="black", text="Y = ").grid(row=3,
                                                                                                         column=1,
                                                                                                         sticky=Tk.E)
    entry2 = Tk.Entry(frame4)
    entry2.grid(row=3, column=2, sticky=Tk.W)

    frame5 = Tk.Frame(window)
    frame5.pack()
    frame5.config(bg="#76dd54")

    button1 = Tk.Button(frame5, text="Run Code!", height=3, width=40, command=lambda: RunProgram2(entry1, entry2)).grid(
        row=1, column=1)

    frame6 = Tk.Frame(window)
    frame6.pack()
    frame6.config(bg="#76dd54")

    button2 = Tk.Button(frame6, text="Next Page", height=2, width=30,
                        command=lambda: ifstateToNested(frame1, frame2, frame3, frame4, frame5, frame6))
    button2.grid(row=1, column=2, sticky=Tk.S)
    button3 = Tk.Button(frame6, text="Return Home", height=2, width=30,
                        command=lambda: ifstateToMain(frame1, frame2, frame3, frame4, frame5, frame6))
    button3.grid(row=1, column=1, sticky=Tk.S)



def NestedPage():
    frame1 = Tk.Frame(window)
    frame1.pack()
    frame1.config(bg="#76dd54")

    MainMenuHeader = Tk.Label(frame1, padx=80, background="#76dd54", text="Control Structures",
                              font=("Helvetica", 40, "bold"), fg="black").grid(row=1, column=1)
    MainMenuSubHeader = Tk.Label(frame1, padx=80, background="#76dd54", text="Nested If Statements""\n""\n",
                                 font=("Helvetica", 20), fg="black").grid(row=2, column=1)

    label2 = Tk.Label(frame1, background="#76dd54", font=("Helvetica", 13), fg="black",
                      text="A nested IF statement is a IF statement inside another IF statement.").grid(row=4, column=1)

    frame2 = Tk.Frame(window)
    frame2.pack()
    frame2.config(bg="#76dd54")
    listbox1 = Tk.Listbox(frame2, width=40, height=15)
    listbox1.grid(row=1, column=1)
    listbox1.insert(1, "X = (Your input here)")
    listbox1.insert(2, "if X > 10:")
    listbox1.insert(3, "    if X >= 100:")
    listbox1.insert(4, "        Print(Bad News)")
    listbox1.insert(5, "    else:")
    listbox1.insert(6, "        Print(Great Job)")
    listbox1.insert(7, "else:")
    listbox1.insert(8, "    print(Bad News)")

    frame3 = Tk.Frame(window)
    frame3.pack()
    frame3.config(bg="#76dd54")

    label3 = Tk.Label(frame3, background="#76dd54", font=("Helvetica", 13), fg="black",
                      text="Let's try and get the output (Great Job)").grid(row=1, column=1)

    label3 = Tk.Label(frame3, background="#76dd54", font=("Helvetica", 13), fg="black",
                      text="Let's try and get the output (Great Job)").grid(row=1, column=1)

    frame4 = Tk.Frame(window)
    frame4.pack()
    frame4.config(bg="#76dd54")

    label4 = Tk.Label(frame4, background="#76dd54", font=("Helvetica", 9), fg="black", text="X = ").grid(row=2,
                                                                                                         column=1,
                                                                                                         sticky=Tk.E)
    entry1 = Tk.Entry(frame4)
    entry1.grid(row=2, column=2, sticky=Tk.W)

    frame5 = Tk.Frame(window)
    frame5.pack()
    frame5.config(bg="#76dd54")

    button1 = Tk.Button(frame5, text="Run Code!", height=3, width=40, command=lambda: RunProgram3(entry1)).grid(
        row=1, column=1)

    frame6 = Tk.Frame(window)
    frame6.pack()
    frame6.config(bg="#76dd54")

    button3 = Tk.Button(frame6, text="Return Home", height=2, width=30,
                        command=lambda: ifstateToMain(frame1, frame2, frame3, frame4, frame5, frame6))
    button3.grid(row=1, column=1, sticky=Tk.S)




def IterationPage():
    frame1 = Tk.Frame(window)
    frame1.pack()
    frame1.config(bg="#76dd54")

    MainMenuHeader = Tk.Label(frame1, padx=80, background="#76dd54", text="Iteration",
                              font=("Helvetica", 40, "bold"), fg="black").grid(row=1, column=1)
    MainMenuSubHeader = Tk.Label(frame1, padx=80, background="#76dd54", text="For Statement""\n""\n",
                                 font=("Helvetica", 20), fg="black").grid(row=2, column=1)

    label2 = Tk.Label(frame1, background="#76dd54", font=("Helvetica", 13), fg="black",
                      text="A for loop will iterate through a given data structure until""\n"
                      "a criteria is met").grid(row=4, column=1)
    frame2 = Tk.Frame(window)
    frame2.pack()
    frame2.config(bg="#76dd54")
    listbox1 = Tk.Listbox(frame2, width=40, height=15)
    listbox1.grid(row=1, column=1)
    listbox1.grid(row=1, column=1)
    listbox1.insert(1, "X = (Your input here)")
    listbox1.insert(2, "i = 12")
    listbox1.insert(3, "for x in range(X):")
    listbox1.insert(4, "    i-=2")
    listbox1.insert(5, "  ")
    listbox1.insert(6, "if i == 0:")
    listbox1.insert(7, "    print(Good Job)")
    listbox1.insert(8, "  ")
    listbox1.insert(9, "elif i > 0:  ")
    listbox1.insert(10, "   print(Try a Larger Number)")
    listbox1.insert(11, "  ")
    listbox1.insert(12, "else:")
    listbox1.insert(13, "   print(That number is too small)")

    frame3 = Tk.Frame(window)
    frame3.pack()
    frame3.config(bg="#76dd54")

    label3 = Tk.Label(frame3, background="#76dd54", font=("Helvetica", 13), fg="black",
                      text="Let's try and get the output (Great Job)").grid(row=1, column=1)

    frame4 = Tk.Frame(window)
    frame4.pack()
    frame4.config(bg="#76dd54")

    label4 = Tk.Label(frame4, background="#76dd54", font=("Helvetica", 9), fg="black", text="X = ").grid(row=2,
                                                                                                         column=1,
                                                                                                         sticky=Tk.E)
    entry1 = Tk.Entry(frame4)
    entry1.grid(row=2, column=2, sticky=Tk.W)

    frame5 = Tk.Frame(window)
    frame5.pack()
    frame5.config(bg="#76dd54")

    button1 = Tk.Button(frame5, text="Run Code!", height=3, width=40, command=lambda: RunProgram4(entry1)).grid(
        row=1, column=1)


    frame6 = Tk.Frame(window)
    frame6.pack()
    frame6.config(bg="#76dd54")

    button2 = Tk.Button(frame6, text="Next Page", height=2, width=30,
                        command=lambda: ifstateToNestedFor(frame1, frame2, frame3, frame4, frame5, frame6))
    button2.grid(row=1, column=2, sticky=Tk.S)
    button3 = Tk.Button(frame6, text="Return Home", height=2, width=30,
                        command=lambda: ifstateToMain(frame1, frame2, frame3, frame4, frame5, frame6))
    button3.grid(row=1, column=1, sticky=Tk.S)




def NestedForPage():
    frame1 = Tk.Frame(window)
    frame1.pack()
    frame1.config(bg="#76dd54")

    MainMenuHeader = Tk.Label(frame1, padx=80, background="#76dd54", text="Iteration",
                              font=("Helvetica", 40, "bold"), fg="black").grid(row=1, column=1)
    MainMenuSubHeader = Tk.Label(frame1, padx=80, background="#76dd54", text="For Statement""\n""\n",
                                 font=("Helvetica", 20), fg="black").grid(row=2, column=1)

    label2 = Tk.Label(frame1, background="#76dd54", font=("Helvetica", 13), fg="black",
                      text="A Nested For Loop is a For Loop inside of another""\n"
                      "for loop").grid(row=4, column=1)
    frame2 = Tk.Frame(window)
    frame2.pack()
    frame2.config(bg="#76dd54")
    listbox1 = Tk.Listbox(frame2, width=40, height=18)
    listbox1.grid(row=1, column=1)
    listbox1.grid(row=1, column=1)
    listbox1.insert(1, "X = (Your input here)")
    listbox1.insert(2, "Y = (Your input here)")
    listbox1.insert(3, "i = 0")
    listbox1.insert(4, "b = 0")
    listbox1.insert(5, "  ")
    listbox1.insert(6, "for x in range(X):")
    listbox1.insert(7, "    for y in range(Y):")
    listbox1.insert(8, "        i +=1")
    listbox1.insert(9, "    b+=1")
    listbox1.insert(10, "  ")
    listbox1.insert(11, "if (i+b) > 20 and (i+b) < 100:  ")
    listbox1.insert(12, "   print(Great Job)")
    listbox1.insert(13, "elif (i + b) < 20:  ")
    listbox1.insert(14, "   print(Try Bigger Variables)")
    listbox1.insert(15, "  ")
    listbox1.insert(17, "else:")
    listbox1.insert(18, "   Print(Try Some Smaller Variables)")

    frame3 = Tk.Frame(window)
    frame3.pack()
    frame3.config(bg="#76dd54")

    label3 = Tk.Label(frame3, background="#76dd54", font=("Helvetica", 13), fg="black",
                      text="Let's try and get the output (Great Job)").grid(row=1, column=1)

    frame4 = Tk.Frame(window)
    frame4.pack()
    frame4.config(bg="#76dd54")

    label4 = Tk.Label(frame4, background="#76dd54", font=("Helvetica", 9), fg="black", text="X = ").grid(row=2,
                                                                                                         column=1,
                                                                                                         sticky=Tk.E)

    label5 = Tk.Label(frame4, background="#76dd54", font=("Helvetica", 9), fg="black", text="Y = ").grid(row=3,
                                                                                                         column=1,
                                                                                                         sticky=Tk.E)

    entry1 = Tk.Entry(frame4)
    entry1.grid(row=2, column=2, sticky=Tk.W)

    entry2 = Tk.Entry(frame4)
    entry2.grid(row=3, column=2, sticky=Tk.W)

    frame5 = Tk.Frame(window)
    frame5.pack()
    frame5.config(bg="#76dd54")

    button1 = Tk.Button(frame5, text="Run Code!", height=3, width=40, command=lambda: RunProgram5(entry1, entry2)).grid(
        row=1, column=1)

    frame6 = Tk.Frame(window)
    frame6.pack()
    frame6.config(bg="#76dd54")

    button3 = Tk.Button(frame6, text="Return Home", height=2, width=30,
                        command=lambda: ifstateToMain(frame1, frame2, frame3, frame4, frame5, frame6))
    button3.grid(row=1, column=1, sticky=Tk.S)

def ClassPage():
    frame1 = Tk.Frame(window)
    frame1.pack()
    frame1.config(bg="#76dd54")

    MainMenuHeader = Tk.Label(frame1, padx=80, background="#76dd54", text="Classes",
            font=("Helvetica", 40, "bold"), fg="black").grid(row=1, column=1)
    MainMenuSubHeader = Tk.Label(frame1, padx=80, background="#76dd54", text="For Statement""\n""\n",
                    font=("Helvetica", 20), fg="black").grid(row=2, column=1)

    label2 = Tk.Label(frame1, background="#76dd54", font=("Helvetica", 13), fg="black",
                          text="Classes allow us to create a blue print that objects""\n"
                               "can be created with. This feature is very""\n"
                      "useful in large programs").grid(row=4, column=1)
    frame2 = Tk.Frame(window)
    frame2.pack()
    frame2.config(bg="#76dd54")
    listbox1 = Tk.Listbox(frame2, width=40, height=15)
    listbox1.grid(row=1, column=1)
    listbox1.insert(1, "class Person:")
    listbox1.insert(2, "    def __init__(self, name, gender, age):")
    listbox1.insert(3, "        self.name = name")
    listbox1.insert(4, "        self.gender = gender")
    listbox1.insert(5, "        self.age = age")
    listbox1.insert(6, " ")
    listbox1.insert(7, "    def introduction(self):")
    listbox1.insert(8, "        Print(My name is + self.name)")
    listbox1.insert(9, "  ")
    listbox1.insert(10, "x = (Your Input Here)")
    listbox1.insert(11, "y = (Your Input Here)")
    listbox1.insert(12, "z = (Your Input Here)")
    listbox1.insert(13, " ")
    listbox1.insert(14, "p1 = Person(x, y, z)")
    listbox1.insert(15, "p1.introduction.self()")

    frame3 = Tk.Frame(window)
    frame3.pack()
    frame3.config(bg="#76dd54")

    label3 = Tk.Label(frame3, background="#76dd54", font=("Helvetica", 13), fg="black",
                      text="Let's try and get the output (Great Job)").grid(row=1, column=1)

    frame4 = Tk.Frame(window)
    frame4.pack()
    frame4.config(bg="#76dd54")

    label4 = Tk.Label(frame4, background="#76dd54", font=("Helvetica", 9), fg="black", text="Name(X) = ").grid(row=2,
                                                                                                         column=1,
                                                                                                         sticky=Tk.E)

    label5 = Tk.Label(frame4, background="#76dd54", font=("Helvetica", 9), fg="black", text="Gender(Y) = ").grid(row=3,
                                                                                                         column=1,
                                                                                                         sticky=Tk.E)

    label6 = Tk.Label(frame4, background="#76dd54", font=("Helvetica", 9), fg="black", text="Age(Z) = ").grid(row=4,
                                                                                                         column=1,
                                                                                                         sticky=Tk.E)

    entry1 = Tk.Entry(frame4)
    entry1.grid(row=2, column=2, sticky=Tk.W)

    entry2 = Tk.Entry(frame4)
    entry2.grid(row=3, column=2, sticky=Tk.W)

    entry3 = Tk.Entry(frame4)
    entry3.grid(row=4, column=2, sticky=Tk.W)
    frame5 = Tk.Frame(window)
    frame5.pack()
    frame5.config(bg="#76dd54")

    button1 = Tk.Button(frame5, text="Run Code!", height=3, width=40, command=lambda: RunProgram6(entry1, entry2, entry3)).grid(
        row=1, column=1)

    frame6 = Tk.Frame(window)
    frame6.pack()
    frame6.config(bg="#76dd54")

    button3 = Tk.Button(frame6, text="Return Home", height=2, width=30,
                        command=lambda: ifstateToMain(frame1, frame2, frame3, frame4, frame5, frame6))
    button3.grid(row=1, column=1, sticky=Tk.S)







def NestedForPage():
    frame1 = Tk.Frame(window)
    frame1.pack()
    frame1.config(bg="#76dd54")

    MainMenuHeader = Tk.Label(frame1, padx=80, background="#76dd54", text="Iteration",
                              font=("Helvetica", 40, "bold"), fg="black").grid(row=1, column=1)
    MainMenuSubHeader = Tk.Label(frame1, padx=80, background="#76dd54", text="For Statement""\n""\n",
                                 font=("Helvetica", 20), fg="black").grid(row=2, column=1)

    label2 = Tk.Label(frame1, background="#76dd54", font=("Helvetica", 13), fg="black",
                      text="A Nested For Loop is a For Loop inside of another""\n"
                      "for loop").grid(row=4, column=1)
    frame2 = Tk.Frame(window)
    frame2.pack()
    frame2.config(bg="#76dd54")
    listbox1 = Tk.Listbox(frame2, width=40, height=18)
    listbox1.grid(row=1, column=1)
    listbox1.grid(row=1, column=1)
    listbox1.insert(1, "X = (Your input here)")
    listbox1.insert(2, "Y = (Your input here)")
    listbox1.insert(3, "i = 0")
    listbox1.insert(4, "b = 0")
    listbox1.insert(5, "  ")
    listbox1.insert(6, "for x in range(X):")
    listbox1.insert(7, "    for y in range(Y):")
    listbox1.insert(8, "        i +=1")
    listbox1.insert(9, "    b+=1")
    listbox1.insert(10, "  ")
    listbox1.insert(11, "if (i+b) > 20 and (i+b) < 100:  ")
    listbox1.insert(12, "   print(Great Job)")
    listbox1.insert(13, "elif (i + b) < 20:  ")
    listbox1.insert(14, "   print(Try Bigger Variables)")
    listbox1.insert(15, "  ")
    listbox1.insert(17, "else:")
    listbox1.insert(18, "   Print(Try Some Smaller Variables)")

    frame3 = Tk.Frame(window)
    frame3.pack()
    frame3.config(bg="#76dd54")

    label3 = Tk.Label(frame3, background="#76dd54", font=("Helvetica", 13), fg="black",
                      text="Let's try and create a person").grid(row=1, column=1)

    frame4 = Tk.Frame(window)
    frame4.pack()
    frame4.config(bg="#76dd54")

    label4 = Tk.Label(frame4, background="#76dd54", font=("Helvetica", 9), fg="black", text="X = ").grid(row=2,
                                                                                                         column=1,
                                                                                                         sticky=Tk.E)

    label5 = Tk.Label(frame4, background="#76dd54", font=("Helvetica", 9), fg="black", text="Y = ").grid(row=3,
                                                                                                         column=1,
                                                                                                         sticky=Tk.E)

    entry1 = Tk.Entry(frame4)
    entry1.grid(row=2, column=2, sticky=Tk.W)

    entry2 = Tk.Entry(frame4)
    entry2.grid(row=3, column=2, sticky=Tk.W)

    frame5 = Tk.Frame(window)
    frame5.pack()
    frame5.config(bg="#76dd54")

    button1 = Tk.Button(frame5, text="Run Code!", height=3, width=40, command=lambda: RunProgram5(entry1, entry2)).grid(
        row=1, column=1)

    frame6 = Tk.Frame(window)
    frame6.pack()
    frame6.config(bg="#76dd54")

    button3 = Tk.Button(frame6, text="Return Home", height=2, width=30,
                        command=lambda: ifstateToMain(frame1, frame2, frame3, frame4, frame5, frame6))
    button3.grid(row=1, column=1, sticky=Tk.S)

def InheritancePage():
    frame1 = Tk.Frame(window)
    frame1.pack()
    frame1.config(bg="#76dd54")

    MainMenuHeader = Tk.Label(frame1, padx=80, background="#76dd54", text="Inheritance",
            font=("Helvetica", 40, "bold"), fg="black").grid(row=1, column=1)
    MainMenuSubHeader = Tk.Label(frame1, padx=80, background="#76dd54", text="Creating a Hero""\n""\n",
                    font=("Helvetica", 20), fg="black").grid(row=2, column=1)

    label2 = Tk.Label(frame1, background="#76dd54", font=("Helvetica", 13), fg="black",
                          text="Inheritance allows us to create an object from a class""\n"
                               "and add new attributes").grid(row=4, column=1)
    frame2 = Tk.Frame(window)
    frame2.pack()
    frame2.config(bg="#76dd54")
    listbox1 = Tk.Listbox(frame2, width=60, height=23)
    listbox1.grid(row=1, column=1)
    listbox1.insert(1, "class Person:")
    listbox1.insert(2, "    def __init__(self, name, gender, age):")
    listbox1.insert(3, "        self.name = name")
    listbox1.insert(4, "        self.gender = gender")
    listbox1.insert(5, "        self.age = age")
    listbox1.insert(6, " ")
    listbox1.insert(7, "    def introduction(self):")
    listbox1.insert(8, "        Print(My name is + self.name)")
    listbox1.insert(9, "class Hero(Person): ")
    listbox1.insert(10, "  ")
    listbox1.insert(11, "    def __init__(self, name, gender, age, superpower):")
    listbox1.insert(12, "        Person.__init__(self, name, gender, age)")
    listbox1.insert(13, "        self.power = superpower")
    listbox1.insert(14, "  ")
    listbox1.insert(15, "    def GetHero(self):")
    listbox1.insert(16, "        print(Hello, my name is self.name and my power is self.power)")
    listbox1.insert(17, "x = (Your Input Here)")
    listbox1.insert(18, "y = (Your Input Here)")
    listbox1.insert(19, "z = (Your Input Here)")
    listbox1.insert(20, "P = (Your Input Here) ")
    listbox1.insert(21, " ")
    listbox1.insert(22, "p2 = Hero(x, y, z)")
    listbox1.insert(23, "p2.GetHero()")

    frame3 = Tk.Frame(window)
    frame3.pack()
    frame3.config(bg="#76dd54")

    label3 = Tk.Label(frame3, background="#76dd54", font=("Helvetica", 13), fg="black",
                      text="Let's try and create a hero").grid(row=1, column=1)

    frame4 = Tk.Frame(window)
    frame4.pack()
    frame4.config(bg="#76dd54")

    label4 = Tk.Label(frame4, background="#76dd54", font=("Helvetica", 9), fg="black", text="Name(X) = ").grid(row=2,
                                                                                                         column=1,
                                                                                                         sticky=Tk.E)

    label5 = Tk.Label(frame4, background="#76dd54", font=("Helvetica", 9), fg="black", text="Gender(Y) = ").grid(row=3,
                                                                                                         column=1,
                                                                                                         sticky=Tk.E)
    label6 = Tk.Label(frame4, background="#76dd54", font=("Helvetica", 9), fg="black", text="Age(Z) = ").grid(row=4,
                                                                                                         column=1,
                                                                                                         sticky=Tk.E)
    label7 = Tk.Label(frame4, background="#76dd54", font=("Helvetica", 9), fg="black", text="Power(P) = ").grid(row=5,
                                                                                                         column=1,
                                                                                                         sticky=Tk.E)

    entry1 = Tk.Entry(frame4)
    entry1.grid(row=2, column=2, sticky=Tk.W)

    entry2 = Tk.Entry(frame4)
    entry2.grid(row=3, column=2, sticky=Tk.W)

    entry3 = Tk.Entry(frame4)
    entry3.grid(row=4, column=2, sticky=Tk.W)

    entry4 = Tk.Entry(frame4)
    entry4.grid(row=5, column=2, sticky=Tk.W)

    frame5 = Tk.Frame(window)
    frame5.pack()
    frame5.config(bg="#76dd54")

    button1 = Tk.Button(frame5, text="Run Code!", height=3, width=40, command=lambda: RunProgram7(entry1, entry2,entry3,entry4)).grid(
        row=1, column=1)

    frame6 = Tk.Frame(window)
    frame6.pack()
    frame6.config(bg="#76dd54")

    button3 = Tk.Button(frame6, text="Return Home", height=2, width=30,
                        command=lambda: ifstateToMain(frame1, frame2, frame3, frame4, frame5, frame6))
    button3.grid(row=1, column=1, sticky=Tk.S)




StartSys()
MainMenu()
