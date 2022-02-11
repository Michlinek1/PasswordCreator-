from tkinter import *
import os.path
import datetime
import csv
import secrets
import string
import keyboard


if os.path.exists("Hasla.csv"):
    pass
else:
    f = open("Hasla.csv", "w")

 

root = Tk()
root.title("Password Generator")
currenttime = datetime.datetime.now().replace(microsecond=0)
currenttimecsv = (f"Program opened at {currenttime}").split(",")
with open(r'Hasla.csv', "a") as f:
        writer = csv.writer(f)
        writer.writerow(currenttimecsv)
root.geometry("600x600")

e = Entry(root, width=600, borderwidth=2 )
e.pack()
e.insert(0, "Lenght of the password:")


def Clear():
    root.destroy()
r = StringVar()
Radiobutton(root, text= "Password without numbers", variable=r,value = "Pass without numbers").pack()
Radiobutton(root, text="Password without alphabet", variable=r, value = "Pass without alphabet").pack()
Radiobutton(root, text="Password without special characters", variable=r, value = "Pass without special characters").pack()
Radiobutton(root, text="Password with anything", variable=r, value = "Pass with everything").pack()
def Generate():
    Label(root, text = f"You choose the option: {str(r.get())}").pack()
    if str(r.get()) == "Pass without numbers":
            newWindow = Toplevel(root)
            newWindow.title("Pass")
            newWindow.geometry("200x200")
            for i in range(5):
                alphabet = string.ascii_letters + string.punctuation
                Pass = ''.join(secrets.choice(alphabet) for i in range(int(e.get())))
                label = Label(newWindow, text = f"Password:{Pass}")
                label.pack()


    elif str(r.get()) == "Pass without alphabet":
            newWindow = Toplevel(root)
            newWindow.title("Pass")
            newWindow.geometry("200x200")
            for i in range(5):
                alphabet = string.digits + string.punctuation
                Pass = ''.join(secrets.choice(alphabet) for i in range(int(e.get())))
                label = Label(newWindow, text = f"Password: {Pass}")
                label.pack()

    elif str(r.get()) =="Pass without special characters":
            newWindow = Toplevel(root)
            newWindow.title("Pass")
            newWindow.geometry("200x200")
            for i in range(5):
                alphabet = string.ascii_letters + string.digits 
                Pass = ''.join(secrets.choice(alphabet) for i in range(int(e.get())))
                label = Label(newWindow, text = f"Password: {Pass}")
                label.pack()

    elif str(r.get()) =="Pass with everything":
            newWindow = Toplevel(root)
            newWindow.title("Pass")
            newWindow.geometry("200x200")
            for i in range(5):
                alphabet = string.ascii_letters + string.digits + string.punctuation 
                Pass = ''.join(secrets.choice(alphabet) for i in range(int(e.get())))
                label = Label(newWindow, text = f"Password: {Pass}")
                label.pack()




def PassCheck():
    global newWindow
    global e1
    newWindow = Toplevel(root)
    newWindow.title("Pass Checker")
    newWindow.geometry("200x200")
    e1 = Entry(newWindow, width=600, borderwidth=2 )
    e1.pack()
    e1.insert(0, "Write down your pass:")
    Check = Button(newWindow,text = "Start checking!", padx = 100, pady = 20, command = Checker).pack()

def Checker(): 
        lenght = len(e1.get())
        label1 = label = Label(newWindow, text = f"Lenght of the pass: {lenght}")
        label.pack()
        if len(e1.get()) >= 20:
            label2 = Label(newWindow, text = "Overall grade: Excelent!")
            label2.pack()
      
        elif len(e1.get()) >= 15:
            label2 = Label(newWindow, text = "Overall grade: Great!")
            label2.pack()
        
        elif len(e1.get()) >= 10:
            label2 = Label(newWindow, text = "Overall grade: Good!")
            label2.pack()
         
        else:
            label2 = Label(newWindow, text = "Overall grade: Bad!")
            label2.pack()
       




Generate = Button(root, text="Generate Password",background = "RED", foreground="white", padx = 100, pady = 20, command=Generate).pack()
Clear = Button(root, text="Clear out!",background = "GREEN", foreground="white", padx = 125, pady = 20,  command=Clear).pack()
Checking = Button(root, text="Password checker",background = "ORANGE", foreground="white", padx = 104, pady = 20, command=PassCheck).pack()




root.mainloop()