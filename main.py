from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


def newFile():
    global file
    root.title('Untitled - Notepad')
    file = None
    TextArea.delete(1.0, END)


def openFile():
    global file
    file = askopenfilename(defaultextension='.txt', filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')])

    if file == " ":
        file = None
    else:
        root.title(os.path.basename(file) + ' - Notepad')
        TextArea.delete(1.0, END)
        f = open(file, 'r')
        TextArea.insert(1.0, f.read())
        f.close()


def saveFile():
    global file

    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension='.txt',
                                 filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')])
        if file == " ":
            file = None
        else:
            f = open(file, 'w')
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + ' -Notepad')
            print('File Saved')
    else:
        f = open(file, 'w')
        f.write(TextArea.get(1.0, END))
        f.close()


def quitApp():
    messagebox.warning('Notepad', 'Notepad by Kirru_9998')
    root.destroy()


def cut():
    TextArea.event_generate(("<<Cut>>"))


def copy():
    TextArea.event_generate(("<<Copy>>"))


def paste():
    TextArea.event_generate(("<<Paste>>"))


def about():
    showinfo('Notepad', 'Notepad by Kirru_9998')


if __name__ == '__main__':
    ''' Tkinter Window '''
    root = Tk()
    root.title('Untitled - Notepad')
    root.wm_iconbitmap('notepad_logo.ico')
    root.geometry('800x500')

    # text area
    TextArea = Text(root, font='lucida 13')
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    # MENU BAR
    MenuBar = Menu(root)
    FileMenu = Menu(MenuBar, tearoff=0)

    # to open new file
    FileMenu.add_command(label='New', command=newFile)

    # to open exiting file
    FileMenu.add_command(label='Open', command=openFile)

    # to save current file
    FileMenu.add_command(label='Save', command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label='Exit', command=quitApp)
    MenuBar.add_cascade(label='File', menu=FileMenu)

    EditMenu = Menu(MenuBar, tearoff=0)
    EditMenu.add_command(label='Cut', command=cut)
    EditMenu.add_command(label='Copy', command=copy)
    EditMenu.add_command(label='Paste', command=paste)

    MenuBar.add_cascade(label='Edit', menu=EditMenu)

    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label='About Notepad', command=about)
    MenuBar.add_cascade(label='Help', menu=HelpMenu)

    root.config(menu=MenuBar)

    root.mainloop()
