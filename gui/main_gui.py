from tkinter import *
from tkinter import filedialog #for Python 3
from tkinter import ttk
import webbrowser


#=======FUNCTIONS===========
#===========================
def OpenLink(url):
    #Function to open the hyperlink
    webbrowser.open_new(url)

def SelectDirectory():
    #Function to open a window to select the folder

    directory = filedialog.askdirectory(title="Select folder to save the .docx file")
    global address
    address = str(directory)

def SelectFile():
    #Function to open a window to select the .csv file

    directory = filedialog.askopenfilename(title="Select the .CSV file exported from Zotero")
    global file_address
    file_address = str(directory)
    lbl = Label(window, text="CSV file: "+str(file_address))
    lbl.place(x=5, y=72.5)


#===========================
#===========================
    
    
#=======MAIN WINDOW=========
#===========================

window = Tk()

# Window parameters
window.title("NoteToDoc v2.0")
window.geometry('331x170')

# Menu bar
menubar = Menu(window)
aboutmenu = Menu(menubar, tearoff=0)
aboutmenu.add_command(label="Documentation", command=lambda *args:OpenLink("http://www.github.com/nestor-rdgz/notetodoc"))
menubar.add_cascade(label="Help", menu=aboutmenu)

# Some introductory label text
lbl1 = Label(window, text="Welcome to NoteToDoc v2.0   (GPL-3.0 License)", justify=LEFT)
lbl1.place(x=5, y=3)
lbl2 = Label(window, text="Source code repository:", justify=LEFT)
lbl2.place(x=5, y=20)


link1 = Label(window, text="github.com/nestor-rdgz/notetodoc", fg="blue", cursor="hand2")
link1.bind("<Button-1>", lambda e: OpenLink("http://www.github.com/nestor-rdgz/notetodoc"))
link1.place(x=130, y=20)

lbl = Label(window, text="Name of the output .docx file:")
lbl.place(x=5, y=97)


# Select folder
#btn1 = Button(window, text="Select folder", command=SelectDirectory, activebackground="#fff8b2", bg="#ffffff")
#btn1.place(x=150, y=245)

# Select csv file
btn = Button(window, text="Select .csv file", command=SelectFile, activebackground="#fff8b2", bg="#ffffff", cursor="hand2")
btn.place(x=120, y=45)

# Start conversion
btn2 = Button(window, text="Convert notes to .docx!", bg="#ffffff", cursor="hand2")
btn2.place(x=97, y=132)

csv_entry = Entry(window, bd=5)
csv_entry.insert(END, "notes.docx")
csv_entry.place(x=170, y=95)


window.config(menu=menubar)
window.mainloop()