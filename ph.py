#-------------Library import---------------------
from __future__ import unicode_literals
import youtube_dl
from tkinter import*
import webbrowser
import tkinter.filedialog as fd
import os
import pornhub
#----------element initialization----------------
class Application(Frame):
    def __init__(self,info):
        super(Application, self).__init__(info)
        self.grid()
        self.widget()
#---------------create function------------------
    def ch_dir(self):
        directory = fd.askdirectory(title="Открыть папку", initialdir="/")
        dirctry = str(directory)
        self.path.insert(0, dirctry)
    def download(self):
        def my_hook(d):
            if d['status'] == 'finished':
                print('Done downloading, now converting ...')

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': '%(id)s',
            'noplaylist': True,
            'progress_hooks': [my_hook],
            'preferredcodec': 'mp4',
        }
        os.chdir(self.path.get())
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            url = self.url.get()
            ydl.download([url])
    def search(self):
        search_keywords = []
        search_keywords.append(self.genre.get())
        client = pornhub.PornHub(search_keywords)
        for video in client.getVideos(10, page=2):
            #print(video['name'])
            #print(video['url'])
            #print('-------------------')
            self.lst.insert(0.0,f'\n{video["name"]}\n{video["url"]}\n')
#------------------GUI create--------------------
    def widget(self):
        self.sqr = LabelFrame(self,text='Buttons')
        self.sqr.grid(row=2,columns=7,sticky=E)
    #-------------------------------------------
        self.sqr1 = LabelFrame(self,text='PornDowloader')
        self.sqr1.grid(row=2,columns=4)
    #--------------------------------------------
        self.sqr2 = LabelFrame(self, text='PornSearch')
        self.sqr2.grid(row=5, columns=7)
    #--------------------------------------------
        self.btn = Button(self.sqr)
        self.btn["text"] = "Download"
        self.btn["command"] = self.download
        self.btn["width"] = 8
        self.btn["height"] = 1
        self.btn["bg"] = "black"
        self.btn["fg"] = "white"
        self.btn.grid(row=1,column=1)
#--------------------------------------------------
        self.btn = Button(self.sqr)
        self.btn["text"] = "browse"
        self.btn["command"] = self.ch_dir
        self.btn["width"] = 8
        self.btn["height"] = 1
        self.btn["bg"] = "black"
        self.btn["fg"] = "white"
        self.btn.grid(row=1, column=2)
#------------------------------------------------------------
        self.lbl = Label(self.sqr1, text="Enter path:")
        self.lbl.grid(row=2,column=0)
        self.path = Entry(self.sqr1,width=50)
        self.path.grid(row=3,column=0)
#------------------------------------------------------------
        self.lbl1 = Label(self.sqr1, text="Enter url:")
        self.lbl1.grid(row=4, column=0)
        self.url = Entry(self.sqr1, width=50)
        self.url.grid(row=5, column=0)
#------------------------------------------------------------
        self.lbl2 =  Label(self.sqr2, text="Enter genre:")
        self.lbl2.grid(row=4, column=1)
        self.genre = Entry(self.sqr2, width=50)
        self.genre.grid(row=5, column=1)
        #----------------------------------------------------
        self.lst = Text(self.sqr2,width=80,height=10)
        self.lst.grid(row=6,column=1)
#------------------------------------------------------------
        self.btn = Button(self.sqr2)
        self.btn["text"] = "search"
        self.btn["command"] = self.search
        self.btn["width"] = 8
        self.btn["height"] = 1
        self.btn["bg"] = "black"
        self.btn["fg"] = "white"
        self.btn.grid(row=7, column=1,sticky=E)
root=Tk()
root.title('Infoitem Dark Souls 3')
root.geometry( "1190x309")
app = Application(root)
root.mainloop()
