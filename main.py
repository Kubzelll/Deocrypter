from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import * 
from tkinter import PhotoImage, filedialog
from pystyle import Colors, Colorate
import os
from time import sleep
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





print(Colorate.Horizontal(Colors.blue_to_cyan,r"""


$$\   $$\          $$\                           $$\ 
$$ | $$  |         $$ |                          $$ |
$$ |$$  /$$\   $$\ $$$$$$$\  $$$$$$$$\  $$$$$$\  $$ |
$$$$$  / $$ |  $$ |$$  __$$\ \____$$  |$$  __$$\ $$ |
$$  $$<  $$ |  $$ |$$ |  $$ |  $$$$ _/ $$$$$$$$ |$$ |
$$ |\$$\ $$ |  $$ |$$ |  $$ | $$  _/   $$   ____|$$ |
$$ | \$$\\$$$$$$  |$$$$$$$  |$$$$$$$$\ \$$$$$$$\ $$ |
\__|  \__|\______/ \_______/ \________| \_______|\__|       
""",1))

print(Colorate.DiagonalBackwards(Colors.cyan_to_green,"Project made by Kubzel",1))





f = Fernet


def get_file_extension(file_name):
    last_dot_index = file_name.rfind(".")
    if last_dot_index != -1:
        return file_name[last_dot_index:]
    else:
        return None


def change_ext(file):
    file = file[:-4]
    ext = get_file_extension(file)
    file = file[:-len(ext)]
    file = file + ".dec" + ext
    return file




try:
#getting token to decrypt&encrypt
    with open("token.key", 'rb') as file:
        key = file.read()
except FileNotFoundError:
    print("No file found, create one!")

option = int(input("Choose option 1 to overwrite dec/enc file or select 2 to create a new file that will be enc/dec \n"))

newfile = False
if option == 2:
    newfile = True





def create():
    try:
        token = f.generate_key()
        #open text file
        with open("token.key", "wb") as file:
            file.write(token)
            file.close()

        print(token)
        print("Writed")
    except:
        print("ERROR")



def select_file():
    print('Opening file dialog...')
    fileselect = filedialog.askopenfilename(title='Select File',)
    global files 
    files = fileselect
    info_list.insert(END, f"File selected")
    info_list.insert(END, f"\n {files}")


    print(files)




def encrpyt():

    try:
        if newfile == False:
            with open(files, "rb") as encfile:
                contents = encfile.read()
                contents_encrypted = Fernet(key).encrypt(contents)
            
            with open(files, "wb") as decfile:
                decfile.write(contents_encrypted)
            print("[!]SUCCESSFULLY ENCRYPTED[!]")
        else:
            newfilename = files + '.enc'
            with open(files, "rb") as encfile:
                contents = encfile.read()
                contents_encrypted = Fernet(key).encrypt(contents)
            
            with open(newfilename, "wb") as decfile:
                decfile.write(contents_encrypted)
            print("[!]SUCCESSFULLY ENCRYPTED[!]")

        
    
    except Exception as e:
        print(files)
        print(f"First select file to encrypt {e}" )
        info_list.insert(END, f"[!]File not selected or not logged in [!] {e}" )

      

def decrypt():
    if newfile == False:
        try:
            with open(files, "rb") as decthefile:
                contentstodec = decthefile.read()
                contents_decrypt = Fernet(key).decrypt(contentstodec)
            
            with open(files, "wb") as writedecfile:
                writedecfile.write(contents_decrypt)
            print("[!]SUCCESSFULLY DECRYPTED[!]")
            info_list.insert(END, "[!]SUCCESSFULLY DECRYPTED[!]")

        
        except Exception as e:
            print(files)
            print(f"First select file to decrypt {e}")
            info_list.insert(END, f"No file selected or file is already decrypted {e}")
    else:
        try:
            newfilename = change_ext(files)

            with open(files, "rb") as decthefile:
                contentstodec = decthefile.read()
                contents_decrypt = Fernet(key).decrypt(contentstodec)
            
            with open(newfilename, "wb") as writedecfile:
                writedecfile.write(contents_decrypt)
            print("[!]SUCCESSFULLY DECRYPTED[!]")
            info_list.insert(END, "[!]SUCCESSFULLY DECRYPTED[!]")
        except Exception as e:
            print(files)
            print(f"First select file to decrypt {e}")
            info_list.insert(END, f"No file selected or file is already decrypted {e}")



def new_key():
    popup = askyesno("Are you sure?", "This will overwrite your enc/dec token and you will not be able to decrypt all encrypted files with this token. Click yes to continue")
    if popup == True:
        print("Generating new token...")
        info_list.insert(END, "Generating new token")
        create()
    






root = tk.Tk()
root.title('Deocrypter')
info_frame = Frame(root)
scroolbar = Scrollbar(info_frame)
info_list = Listbox(info_frame, height=30, width=50, yscrollcommand=scroolbar.set)
scroolbar.pack(side=RIGHT, fill=Y)
info_list.pack(side=LEFT, fill=BOTH)
info_list.pack()
info_frame.pack()


openfile = tk.Button(root, text='Open files', padx=4, 
                        pady=4, fg='white', bg='#263D42', command=select_file)
openfile.pack()


encrpyt = tk.Button(root, text='Encrpyt files', padx=4,
                         pady=4, fg='white', bg='#263D42', command=encrpyt)
encrpyt.pack()

decrypt = tk.Button(root, text='Decrypt Files', padx=4, pady=4, fg='white', bg='#263D42', command=decrypt)

decrypt.pack()

createkey = tk.Button(root, text='Create new token', padx=4, pady=4, fg='white', bg='#263D42', command=new_key)
createkey.pack()


root.mainloop()