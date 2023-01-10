from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import * 
from tkinter import PhotoImage, filedialog
from termcolor import colored
from tkinter.messagebox import askyesno

'''
$$\   $$\          $$\                           $$\ 
$$ | $$  |         $$ |                          $$ |
$$ |$$  /$$\   $$\ $$$$$$$\  $$$$$$$$\  $$$$$$\  $$ |
$$$$$  / $$ |  $$ |$$  __$$\ \____$$  |$$  __$$\ $$ |
$$  $$<  $$ |  $$ |$$ |  $$ |  $$$$ _/ $$$$$$$$ |$$ |
$$ |\$$\ $$ |  $$ |$$ |  $$ | $$  _/   $$   ____|$$ |
$$ | \$$\\$$$$$$  |$$$$$$$  |$$$$$$$$\ \$$$$$$$\ $$ |
\__|  \__|\______/ \_______/ \________| \_______|\__|
'''

ascii_art = r"""\


$$\   $$\          $$\                           $$\ 
$$ | $$  |         $$ |                          $$ |
$$ |$$  /$$\   $$\ $$$$$$$\  $$$$$$$$\  $$$$$$\  $$ |
$$$$$  / $$ |  $$ |$$  __$$\ \____$$  |$$  __$$\ $$ |
$$  $$<  $$ |  $$ |$$ |  $$ |  $$$$ _/ $$$$$$$$ |$$ |
$$ |\$$\ $$ |  $$ |$$ |  $$ | $$  _/   $$   ____|$$ |
$$ | \$$\\$$$$$$  |$$$$$$$  |$$$$$$$$\ \$$$$$$$\ $$ |
\__|  \__|\______/ \_______/ \________| \_______|\__|                                            
        """

colored_ascii = colored(ascii_art, 'blue')


print(colored_ascii)

print(colored("PROJECT MADE BY KUBZEL", 'magenta'))
f = Fernet


#getting token to decrypt&encrypt
with open("token.key", 'rb') as file:
    key = file.read()



def create():
    try:
        token = f.generate_key()
        #open text file
        text_file = open("token.key", "wb")
        text_file.write(token)
        text_file.close()

        print(token)
        print("Writed")
    except:
        print("ERROR")



def select_file():
    print('Opening file dialog...')
    fileselect = filedialog.askopenfilename(title='Select File',)
    global files 
    files = fileselect


    print(files)


def encrpyt():
    try:
        with open(files, "rb") as encfile:
            contents = encfile.read()
            contents_encrypted = Fernet(key).encrypt(contents)
        
        with open(files, "wb") as decfile:
            decfile.write(contents_encrypted)
        print("[!]SUCCESSFULLY ENCRYPTED[!]")
    
    except Exception as e:
        print(files)
        print(f"First select file to encrypt {e}" )





def decrypt():

    try:

        with open(files, "rb") as decthefile:
            contentstodec = decthefile.read()
            contents_decrypt = Fernet(key).decrypt(contentstodec)
        
        with open(files, "wb") as writedecfile:
            writedecfile.write(contents_decrypt)
        print("[!]SUCCESSFULLY DECRYPTED[!]")
    
    except Exception as e:
        print(files)
        print(f"First select file to decrypt {e}")



def new_key():
    popup = askyesno("Are you sure?", "This will overwrite your enc/dec token and you will not be able to decrypt all encrypted files with this token. Click yes to continue")
    if popup == True:
        print("Generating new token...")
        create()
    






root = tk.Tk()
root.title('Deocrypter')


canvas = tk.Canvas(root, height=700, width=700, bg = '#263D42')
canvas.pack()

frame = tk.Frame(root, bg='white')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)


openfile = tk.Button(root, text='Open files', padx=10, 
                        pady=5, fg='white', bg='#263D42', command=select_file)
openfile.pack()


encrpyt = tk.Button(root, text='Encrpyt files', padx=10,
                         pady=5, fg='white', bg='#263D42', command=encrpyt)
encrpyt.pack()

decrypt = tk.Button(root, text='Decrypt Files', padx=10, pady=5, fg='white', bg='#263D42', command=decrypt)

decrypt.pack()

createkey = tk.Button(root, text='Create new token', padx=10, pady=5, fg='white', bg='#263D42', command=new_key)
createkey.pack()



root.mainloop()
    
    












