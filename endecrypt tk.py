from Tkinter import *
import time

root = Tk()
root.title('EnDecrypt')

LUT_encryption = dict()

LUT_decryption = dict()

def encrypt_message():
    e = int(evalue.get())
    n = int(nvalue.get())
    message = mssg.get("1.0", END)
    encrypted_msg = ""
    for i in message:
        if i in LUT_encryption:
            encrypted_msg += LUT_encryption[i]
        else:
            numerize = int(ord(i))
            encrypt = pow(numerize, e, n)
            LUT_encryption[i] = unichr(encrypt)
            encrypted_msg += unichr(encrypt)
    mssg.delete("1.0", END)
    
        
        
        
def decrypt_message(msg):
    decrypted_msg = ""
    for i in msg:
        if i in LUT_decryption:
            decrypted_msg += LUT_decryption[i]
        else:
            numerize = ord(i)
            decrypt = pow(numerize, d, n)
            LUT_decryption[i] = unichr(decrypt)
            decrypted_msg += unichr(decrypt)       

def clear():
    mssg.delete('1.0', END)
    
def printtest():
    print "hello"


Encrypt = Label(root, text = "Encryption")
Encrypt.grid(row = 0, sticky = EW)

n = Label(root, text = "n =")
n.grid(row = 2, column = 0, sticky = EW)

nvalue = Entry(root)
nvalue.grid(row = 2, column = 1, columnspan = 2)


e = Label(root, text = "e =")
e.grid(row = 2, column = 3)


evalue = Entry(root)
evalue.grid(row = 2, column = 4, columnspan = 2,)


enbutton = Button(root, text = "Encrypt", command=printtest)
enbutton.grid(row = 3, column = 1)



de = Button(root, text = "Decrypt")
de.grid(row = 3, column = 3)

mssg = Text(root)
mssg.grid(row = 10, column = 5, columnspan = 2)


mssg2 = Text(root)
mssg2.grid(row = 10, columnspan = 2)


root.mainloop()