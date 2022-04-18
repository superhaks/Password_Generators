from tkinter import *
from random import randint
root = Tk()
root.title('Password Generator')
#root.iconphoto('H logo.jpg')
root.geometry("500x300")

#genrate random password
def rand_pass():
    pass_entry.delete(0,END) #clear entry field
    pass_len = int(no_entry.get()) #get password length
    password = ''
    for x in range(pass_len):
        password += chr(randint(33, 126))  # use ascii to make a character

    pass_entry.insert(0,password)
#generate code to copy entry to clipboard
def copier():
    root.clipboard_clear() #clear clipboard
    root.clipboard_append(pass_entry.get()) #copy entry to clipboard


#Label
lf = LabelFrame(root,text="Number of characters", font=("Helvetica",10))
lf.pack(pady= 20)
#entry
no_entry = Entry(lf,font=("Helvetica",20))
no_entry.pack(padx=20,pady=20)
#dummy entry field we use as label
pass_entry = Entry(root,text='', font=("Helvetica",20), bd=0, bg="systembuttonface")
pass_entry.pack(pady=20)
#main frame
mframe = Frame(root)
mframe.pack(pady=20)
#generate password button
mbutton = Button(mframe, text="Generate Password", command=rand_pass)
mbutton.grid(row=0,column=0,padx=10)
#copy password button
cbutton = Button(mframe, text="Copy to Clipboard", command=copier)
cbutton.grid(row=0,column=1,padx=10)

root.mainloop()