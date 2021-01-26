#this tool is v2 of my yotube video downloder tool
#thank you sami youare really noop


from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import pytube

"""
This GUI tool will download youtube
videos from given link. made by dz0ne (sami is noop)
"""

# Functions section
class File:
    ''' This function will set download path '''
    def des(self):
        fp = filedialog.askdirectory()
        return fp

def dload():
    '''
    This callback function will run when
    download button is clicked
    '''
    
    try:
        lb1.insert(END, 'Download started')
        dest = File()
        link = link_txt.get()
        yt = pytube.YouTube(link)
        stream = yt.streams.first()
        destination = dest.des()
        lb2.insert(END, destination)
        stream.download(destination)
        lb1.insert(END, 'Download Completed')
        return True
    except:
        lb1.insert(END, 'Download Interrupted')

def close():
    ''' This function will close the application '''
    window.destroy()



window = Tk()
window.title("YouTube Video Downloader")


# Labels
l1 = Label(window, text="Video Link")
l1.grid(row=0, column=0)

l2 = Label(window, text="Destination Folder")
l2.grid(row=1, column=0)


# Entry
link_txt = StringVar()
e1 = Entry(window, textvariable=link_txt)
e1.grid(row=0, column=1)


# Button
b1 = Button(window, text="Download", command=dload)
b1.grid(row=0, column=2)

closebtn = Button(window, text="Close", fg='red', command=close)
closebtn.grid(row=6, column=2)

f = File()
des = Button(text="Choose", command=f.des)
des.grid(row=1, column= 2)


# Seperator
s1 = ttk.Separator(window, orient=HORIZONTAL,).grid(row=2, columnspan=5, sticky="ew")


# Listbox
lb1 = Listbox(window, height=3, width=30)
lb1.grid(row=5, column=1)


lb2 = Listbox(window, height=1)
lb2.grid(row=1, column= 1)


window.mainloop()











