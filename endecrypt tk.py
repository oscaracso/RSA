from Tkinter import *
import time

root = Tk()
root.title('EnDecrypt')
menubar=Menu(root)

LUT_encryption = dict()

LUT_decryption = dict()

#e   = 47
#d   = 83
#n   = 4061
#r   = 3900
#e*d = 3901


def encrypt_message():
    e = int(evalue.get())
    n = int(nvalue.get())
    message = mssg.get(1.0, END)
    encrypted_msg = ""
    for i in message:
        if i in LUT_encryption:
            encrypted_msg += LUT_encryption[i]
        else:
            numerize = int(ord(i))
            encrypt = pow(numerize, n, e)
            LUT_encryption[i] = unichr(encrypt)
            encrypted_msg += unichr(encrypt)
    mssg.delete(1.0, END)
    mssg.insert(END, encrypted_msg)
    
        
def donothing():
   print "a"
        
def decrypt_message():
    n = int(nvalue.get())
    d = 83
    cipher = mssg.get(1.0, END)
    decrypted_msg = ""
    for i in cipher:
        if i in LUT_decryption:
            decrypted_msg += LUT_decryption[i]
        else:
            numerize = ord(i)
            decrypt = pow(numerize, d, n)
            LUT_decryption[i] = unichr(decrypt)
            decrypted_msg += unichr(decrypt)       
    mssg.delete(1.0, END)
    mssg.insert(END, decrypted_msg)

def savefileW():
    f = open("README.txt", "w")
    messages = mssg.get(0, END)
    for i in message:
        f.write(i + "\n")
        f.close()
    
def openfileR():
    f = open("README.txt", "r")
    for line in f:
        mssg.insert(END, line)
        
Encrypt = Label(root, text = "Encryption")
Encrypt.grid(row = 0)

e = Label(root, text = "e =")
e.grid(row = 2, column = 0)

evalue = Entry(root)
evalue.grid(row = 2, column = 1, columnspan = 4)


n = Label(root, text = "n =")
n.grid(row = 2, column = 6)


nvalue = Entry(root)
nvalue.grid(row = 2, column = 7, columnspan = 4)


enbutton = Button(root, text = "Encrypt", command=encrypt_message)
enbutton.grid(row = 3, column = 1)

de = Button(root, text = "Decrypt", command=decrypt_message)
de.grid(row = 3, column = 7)

mssg = Text(root)
mssg.grid(column = 0, columnspan = 8)
mssg.insert(END , "Message/Cipher")

filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=openfileR)
filemenu.add_command(label="Save", command=savefileW)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

editmenu=Menu(menubar,tearoff=0)
editmenu.add_command(label="Undo", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu=Menu(menubar,tearoff=0)
helpmenu.add_command(label="Help",command=donothing)
menubar.add_cascade(label="Help",menu=helpmenu)

root.config(menu = menubar)
root.mainloop()