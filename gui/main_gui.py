'''
    Name: main_gui.py
    GitHub URL: https://github.com/nestor-rdgz/NoteToDoc
    License: GNU General Public License v3.0
'''
from tkinter import *
from tkinter import filedialog #for Python 3
from tkinter import ttk
import webbrowser
from ntdfunc import * 


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
    lbl = Label(window, text="File selected: "+str(file_address), fg="#0084f9")
    lbl.place(x=5, y=72.5)

def LincenseWin():
    #Function that opens a window to show the license

    linwin = Tk()
    linwin.title("License")
    linwin.geometry('225x60')


    lbl = Label(linwin, text="NoteToDoc is under the GPL-3.0 License")
    lbl.place(x=2, y=5)

    btn3 = Button(linwin, text="Return", bg="#ffffff", cursor="hand2", command=linwin.destroy)
    btn3.place(x=88, y=30)

def VersionWin():
    #Function that opens a window to show the version

    versionwin = Tk()
    versionwin.title("Version")
    versionwin.geometry('225x60')


    lbl = Label(versionwin, text="Current version of NoteToDoc is v2.0")
    lbl.place(x=10, y=5)

    btn3 = Button(versionwin, text="Return", bg="#ffffff", cursor="hand2", command=versionwin.destroy)
    btn3.place(x=88, y=30)

def Finalwin():
    #Function that opens a window to show the license

    finalwin = Tk()
    finalwin.title("Conversion completed")
    finalwin.geometry('220x70')


    lbl = Label(finalwin, text=str(csv_entry.get()+" "+"generated successfully!"))
    lbl.place(x=15, y=5)

    btn2 = Button(finalwin, text="Exit", bg="#ffffff", cursor="hand2", command=finalwin.destroy)
    btn2.place(x=90, y=30)

   

def StartConversion():
    #Function for the Start Conversion button

    SelectDirectory()
    Notetodoc(address,str(csv_entry.get()), file_address )
    Finalwin()

#===========================
#===========================
    
    
#=======MAIN WINDOW=========
#===========================

window = Tk()

# Window parameters
window.title("NoteToDoc v2.0")
window.geometry('331x200')
#window.iconbitmap('./icono.ico')
#window.iconphoto(False, PhotoImage(file='icono.png'))

# Menu bar ======================================================================================================
menubar = Menu(window)
# About
aboutmenu = Menu(menubar, tearoff=0)
aboutmenu.add_command(label="Version", command=VersionWin)
aboutmenu.add_command(label="License", command=LincenseWin)
menubar.add_cascade(label="About", menu=aboutmenu)
# Help
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Github Repository", command=lambda *args:OpenLink("http://www.github.com/nestor-rdgz/notetodoc"))
menubar.add_cascade(label="Help", menu=helpmenu)
# Exit
menubar.add_cascade(label="Exit", command=window.destroy)
#================================================================================================================

# Some introductory label text
lbl1 = Label(window, text="Welcome to NoteToDoc v2.0", justify=LEFT, font=("Trebuchet", 12))
lbl1.place(x=63, y=3)


lbl = Label(window, text="Name of the output .docx file:")
lbl.place(x=5, y=97)


# Select folder
#btn1 = Button(window, text="Select folder", command=SelectDirectory, activebackground="#fff8b2", bg="#ffffff")
#btn1.place(x=150, y=245)

# Select csv file
btn = Button(window, text="Select .csv file", command=SelectFile, activebackground="#fff8b2", bg="#ffffff", cursor="hand2", font=("Trebuchet", 9))
btn.place(x=120, y=45)

# Start conversion
btn2 = Button(window, text="Convert notes to .docx!", bg="#ffffff", cursor="hand2", command=StartConversion, font=("Trebuchet", 9))
btn2.place(x=97, y=132)

csv_entry = Entry(window, bd=5)
csv_entry.insert(END, "notes.docx")
csv_entry.place(x=170, y=95)



window.config(menu=menubar)
window.mainloop()