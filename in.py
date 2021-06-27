import subprocess
import sys
import tkinter

lists = []


"""def getClipboardData():
 p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
 retcode = p.wait()
 data = p.stdout.read()
 lists.append(data)

def setClipboardData(data):
 p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
 p.stdin.write(data)
 p.stdin.close()
 retcode = p.wait()"""

# Creating the GUI Application
from tkinter import *
class frame:
    def __init__(self):
        master = Tk()
        # listbox
        self.listbox = Listbox(master,xscrollcommand=True,yscrollcommand=True,height=20,width=40)
        self.top_frame = tkinter.Frame()
        # Button for application
        self.listboxbutton = tkinter.Button(self.top_frame,text="add",command = self.getClipboardData)
        self.copybutton = tkinter.Button(self.top_frame,text="copy",command = self.setClipboardData)
        self.removeButton = tkinter.Button(self.top_frame,text="remove",command = self.remove)
        self.clearButton = tkinter.Button(self.top_frame,text="clear",command = self.clear)
        
        # Displaying what in the list
        for item in lists:
            self.listbox.insert(END, item)
        self.listboxbutton.pack(side='left')
        self.copybutton.pack(side='left')
        self.clearButton.pack(side='left')
        self.removeButton.pack(side='left')
        self.top_frame.pack()
        self.listbox.pack()
    
        mainloop()
    # Adding to ClipBoard    
    def getClipboardData(self):
        p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
        retcode = p.wait()
        data = p.stdout.read()
        value = -20
        count = 0
        try:
            # Making sure that the list doesnt add duplicates
            while(count != len(lists) and lists[count] != data):
                if lists[count] == data:
                    break
                else:
                    count += 1
            value = lists.index(data)
        except (ValueError,TypeError) as Error:
            lists.append(data)
            self.listbox.delete(0, END)
            for item in lists:
                self.listbox.insert(END, item)

    # Remove selection from Clipboard
    def remove(self):
        try:
            
            option =list(self.listbox.curselection())
            lists.pop(option[0])
            self.listbox.delete(0, END)
            for item in lists:
                self.listbox.insert(END, item)
        except (AttributeError,IndexError) as Error:
            option =list(self.listbox.curselection())
            lists.pop(option[0])
            self.listbox.delete(0, END)
            for item in lists:
                self.listbox.insert(END, item)
            
            
    # Clear the smartBoard completely
    def clear(self):
        while len(lists) != 0:
              lists.pop()
        self.listbox.delete(0, END)
        for item in lists:
            self.listbox.insert(END, item)
        
        
    # Copying to clipboard
    def setClipboardData(self):
        option = []
        option =list(self.listbox.curselection())
        if len(option) == 0:
            option = []
        else:
            index = option[0]    
            string = str(lists[index])
            string = string.replace('b',"")
            string = str(string)
            p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
            data = p.stdin.write(bytes(string,"utf-8"))
            p.stdin.close()
            retcode = p.wait()

frame()





