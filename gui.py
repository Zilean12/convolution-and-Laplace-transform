#Library
import cv2
import PIL.Image
import PIL.ImageTk
#from matplotlib import pyplot as plt
from tkinter import *
from tkinter import filedialog
#import io

#Class for Image Processor
class ImageProcessor:
    def __init__(self):
        self.image=0
    def ReadImage(self,filename):
        self.image=cv2.imread(filename)
        self.image=cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
    def GrayScale(self):
        self.temp=self.image
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
    def Save(self,title):
        try:
            cv2.imwrite(title,self.imagetemp)
        except:
            cv2.imwrite(title,self.image)
    def Smooth(self,value):
        self.imagetemp=self.image
        self.imagetemp = cv2.medianBlur(self.image, value)
    def Recolor(self):
        self.temp=cv2.cvtColor(self.temp, cv2.COLOR_BGR2RGB)
        self.image=self.temp
        

#Window & Canvas Initiation 
wn=Tk()
wn.geometry("700x700")
wn.title("Image Editor v1.0")
canvas = Canvas(wn,bg = "royal blue",height = "700",width ="570")
canvas.pack(side="left")
textin=StringVar()

#Function for Buttons
def New():
    global canvas,buf,wn,textin,im,photo,resized
    im=ImageProcessor()
    filename=filedialog.askopenfilename()
    #print(filename)
    im.ReadImage(filename)
    photo = PIL.Image.fromarray(im.image)
    resized = photo.resize((450, 600),PIL.Image.ANTIALIAS)
    photo=PIL.ImageTk.PhotoImage(resized)
    panelA=Label(wn,image=photo)
    panelA.image=photo
    panelA.place(x=0,y=0)
def sv():
    global canvas,buf,wn,textin,im,photo,panelA
    try:
        im.image=cv2.cvtColor(im.image, cv2.COLOR_BGR2RGB)
        im.imagetemp=cv2.cvtColor(im.imagetemp, cv2.COLOR_BGR2RGB)
    except:
        im.image=cv2.cvtColor(im.image, cv2.COLOR_BGR2RGB)        
    title=filedialog.asksaveasfilename()
    im.Save(title)
def gs():
    global canvas,buf,wn,textin,photo,panelA,im
    im.GrayScale()
    im.image=cv2.cvtColor(im.image, cv2.COLOR_BGR2RGB)
    photo = PIL.Image.fromarray(im.image)
    resized = photo.resize((450, 600),PIL.Image.ANTIALIAS)
    photo=PIL.ImageTk.PhotoImage(resized)
    panelA=Label(wn,image=photo)
    panelA.image=photo
    panelA.place(x=0,y=0)
def smooth():
    global canvas,buf,wn,textin,im,photo,panelA,mtext
    value=mtext.get()
    im.image=cv2.cvtColor(im.image, cv2.COLOR_BGR2RGB)
    value=int(value)
    im.Smooth(value)
    im.imagetemp=cv2.cvtColor(im.imagetemp, cv2.COLOR_BGR2RGB)
    photo = PIL.Image.fromarray(im.imagetemp)
    resized = photo.resize((450, 600),PIL.Image.ANTIALIAS)
    photo=PIL.ImageTk.PhotoImage(resized)
    panelA=Label(wn,image=photo)
    panelA.image=photo
    panelA.place(x=0,y=0)
def undo():
    global canvas,buf,wn,textin,im,photo,panelA
    im.Recolor()
    im.image=cv2.cvtColor(im.image, cv2.COLOR_BGR2RGB)
    im.temp=cv2.cvtColor(im.temp, cv2.COLOR_BGR2RGB)
    photo = PIL.Image.fromarray(im.image)
    resized = photo.resize((450, 600),PIL.Image.ANTIALIAS)
    photo=PIL.ImageTk.PhotoImage(resized)
    panelA=Label(wn,image=photo)
    panelA.image=photo
    panelA.place(x=0,y=0)
    

#Menubar Creation
menubar = Menu(wn)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New",command=New)
filemenu.add_command(label="Save",command=sv)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=wn.destroy)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Gray Scale",command=gs)
editmenu.add_command(label="Undo",command=undo)
menubar.add_cascade(label="Edit", menu=editmenu)

#Button Placement
mtext=Entry(wn,font=("tempus sans itc",18,'bold'),width=7,bd=4,bg='powder blue')
mtext.place(x=570,y=156)
but_new=Button(wn,padx=2,pady=5,bd=4,bg='white',text="New File",font=("Courier New",16,'bold'),command=New)
but_new.place(x=570,y=0)
but_save=Button(wn,padx=28,pady=5,bd=4,bg='white',text="Save",font=("Courier New",16,'bold'),command=sv)
but_save.place(x=570,y=52)
but_gray=Button(wn,padx=28,pady=5,bd=4,bg='white',text="Gray",font=("Courier New",16,'bold'),command=gs)
but_gray.place(x=570,y=104)
but_sm=Button(wn,padx=2,pady=5,bd=4,bg='white',text="Smoothen",font=("Courier New",16,'bold'),command=smooth)
but_sm.place(x=570,y=196)
but_un=Button(wn,padx=28,pady=5,bd=4,bg='white',text="Undo",font=("Courier New",16,'bold'),command=undo)
but_un.place(x=570,y=248)
lab=Label(wn,text="*Odd Values Only*")
lab.place(x=580,y=300)


wn.config(menu=menubar)
wn.mainloop()