from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pygame import mixer
from tkinter import messagebox
from time import strftime
from mutagen.mp3 import MP3
import os
from time import gmtime
from tkinter import ttk,font
# hel =font.Font(family="Android 101",size=14,weight="bold")
mixer.init()
import getpass
smw=os.getlogin()
List_ = None
filename = None
erw=open("last.txt","a")
erw.write("")
erw.close()
m2=[]
m4=[]
co=0
theme=""
global lel   
le1=len(m2)

root =Tk()
root.config(bg="#FBC1C1")
pc = "play"
from tkinter import  filedialog 
en=Entry (root,width=42,bg="white",bd=2,relief=GROOVE)
en.place(x=130,y=190)
l=Listbox(root,width=80,height=5)
l.config(relief=FLAT,bd=0,highlightthickness=0,bg="#FBC1C1",fg="black",activestyle="none")
l.place(x=130,y=221)
   # Adjust the coordinates as needed


def pop():
    global gana
    try:
        df=filedialog.askdirectory(title="Select a music Directory",initialdir="C:/Users/"+smw+"/Music")
    except:
        gana=os.listdir("C:/Users/"+smw+"/Music")
        import pyautogui as py
        py.alert(title="IM Player UI ",text=" No Directory has been selected \n\n C:/Users/"+smw+"/Music has been selected to Default Directory ",)
        pass

    try:
        gana=os.listdir(df)
    except:
        gana=os.listdir("C:/Users/"+smw+"/Music")
        import pyautogui as py
        py.alert(title="IM Player UI ",text=" No Directory has been selected \n\n  C:/Users/"+smw+"/Music has been selected to Default Directory ")
        pass

play_= False
def play_time():
    global currentsong, consonglen, songlength

    if "C:/" in currentsong:
        pass
    else:
        try:
            currentsong = gana + {currentsong} + ".mp3"
        except:
            currentsong = "C:/Users/" + smw + "/Music/+currentsong+.mp3"

    current = mixer.music.get_pos() / 1000
    converted = strftime("%H:%M:%S", gmtime(current))
    songmut = MP3(currentsong)
    songlength = songmut.info.length
    consonglen = strftime("%H:%M:%S", gmtime(songlength))

    # Update the progress bar
    progress = (current / songlength) * 100
    progress_bar["value"] = progress

    sliderlbl.config(text=f"{converted} / {consonglen}")
    sliderlbl.after(1000, play_time)


def no():
    defau=root.cget('bg')
    lbl4.config(text="")
    lbl3.config(text="")
    defau11=red_frame.cget('bg')
    global currentsong
    stop()
    po=en.get()
    pt="C:/Users/"+smw+"/Music/"+po
    mixer.music.load(pt)
    currentsong = pt
    play_ = True
    pc = "pause"
    if defau=="#FBC1C1" or defau=="#f6ead4" :
        lbl4.config(text=po.replace(".mp3",""),justify = CENTER,wraplength=500, font = ("cool jazz", 13),fg="black",bg=defau11)
        lbl4.place(x=105.8, y=328)  
    else:
        lbl4.config(text=po.replace(".mp3",""),justify = CENTER,wraplength=500, font = ("cool jazz", 13),fg="white",bg=defau11)
        lbl4.place(x=105.8, y=328)
    btn3.config(text = pc)
    play()
en1=Button(root,text="Play",bg="white",command=no)
en1.place(x=450,y=190)

def load(n):
    rt7=open("recently played1.txt",'a',encoding='utf-8')
    string = strftime('%I:%M %p')
    rt7.write(n+string+'\n')
    rt7.close()
    mixer.music.load(str(n))
    
def play():
    global play_, consonglen
    mixer.music.play()
    play_ = True

    # Set the initial progress bar value
    progress_bar["value"] = 0

    # Start updating the progress bar
    play_time()

rt=0
pt=0

def lblm2():
        defau=root.cget('bg')
        defau11=red_frame.cget('bg')
        global List_,filename, value,lbl3,currentsong
       
    
        lbl3.config(text="")
        lbl4.config(text="")
        stop()
        
        we=filename.split("/")
      
        ee=we[4]
        ty=ee.replace(".mp3","")
        if defau=="#FBC1C1" or defau=="#f6ead4" :
            lbl4.config(text=ty,justify = CENTER,wraplength=500, font = ("cool jazz", 13),fg="black",bg=defau11)
            lbl4.place(x=105.8, y=328)  
        else:
            lbl4.config(text=ty,justify = CENTER,wraplength=500, font = ("cool jazz", 13),fg="white",bg=defau11)
            lbl4.place(x=105.8, y=328)
        mixer.music.load(filename)
        rt6=open("recently played(np1).txt",'a',encoding='utf-8')
        rt7=open("recently played(history).txt",'a',encoding='utf-8')
        string = strftime('%Y-%m-%d-%I:%M:%A')
        rt7.write(filename+",."+string+'\n')
        rt7.close()
        rt6.write(filename+'\n')
        rt6.close()

def lbl():
    
        defau=root.cget('bg')
        defau11=red_frame.cget('bg')
        global List_,filename, value,lbl3,currentsong
     
        if List_== None:
            lbl3.config(text="")
            lbl4.config(text="")
            stop()
            
            we=filename.split("/")
     
            ee=we[4]
            ty=ee.replace(".mp3","")
            if defau=="#FBC1C1" or defau=="#f6ead4" :
                lbl4.config(text=ty,justify = CENTER,wraplength=500, font = ("cool jazz", 13),fg="black",bg=defau11)
                lbl4.place(x=105.8, y=328)  
            else:
                lbl4.config(text=ty,justify = CENTER,wraplength=500, font = ("cool jazz", 13),fg="white",bg=defau11)
                lbl4.place(x=105.8, y=328)
            mixer.music.load(filename)
            rt6=open("recently played(np1).txt",'a',encoding='utf-8')
            rt7=open("recently played(history).txt",'a',encoding='utf-8')
            string = strftime('%Y-%m-%d-%I:%M:%A')
            rt7.write(filename+",."+string+'\n')
            rt7.close()
            rt6.write(filename+'\n')
            rt6.close()
        
        for i in list(l23):
            stop()
            load(i)
            currentsong=i
            # lbl2.config(text="")
            lbl3.config(text="")
            lbl4.config(text="")
            value = l23.index(i)
            string = str(i)
            we=string.split("/")
            
            ee=we[4]
            ty=ee.replace(".mp3","")
            
            if defau=="#FBC1C1" or defau=="#f6ead4" :
                lbl3 = Label(text=ty,justify = CENTER,wraplength=500,font = ("cool jazz", 13,),fg="black",bg=defau11)
                lbl3.place(x=105.5, y=328)
            else:
                lbl3 = Label(text=ty,justify = CENTER,wraplength=500,font = ("cool jazz", 13,),fg="white",bg=defau11)
                lbl3.place(x=105.5, y=328)
            global rt,pt
            rt=value-1
            
def slide(x):
    g = myslider.get()
    con = time.strftime("%H:%M:%S",time.gmtime(g))
    sliderlbl.config(text = f"{con} / --:--:--") 

def next1():
    lbl4.config(text="")
    lbl3.config(text="")
    try:
        global List_,rt,currentsong
      
        ft=list(l23)[rt+2]
        currentsong = ft
        load(ft)
        rt2=open("recently played(np).txt",'a',encoding='utf-8')
        rt2.write(ft+'\n')
        rt2.close()
        mixer.music.play()

        rt=rt+1
        we=ft.split("/")
        
        ee=we[4]
        ty=ee.replace(".mp3","")
        btn3.config(text ="pause")
        lbl4.config(text=ty)
        lbl3.config(text=ty)
        root.title("Music Player")
    except IndexError:
        root.title("NO songs further")
def previus():
    lbl4.config(text="")
    
    try:
        global List_,rt,currentsong
      
        ft=list(l23)[rt]
        load(ft)
        rt4=open("recently played(np).txt",'a',encoding='utf-8')
        rt4.write(ft+'\n')
        rt4.close()
        currentsong = ft
        mixer.music.play()
        we=ft.split("/")
     
        ee=we[4]
        ty=ee.replace(".mp3","")
        lbl3.config(text=ty)
        lbl4.config(text=ty)
        rt=rt-1
        btn3.config(text = "pause")
        root.title("Music Player")
    except IndexError:
        root.title("NO songs further")

def playlist(e):
    global List_,filename
    global l23
    filename = filedialog.askdirectory(parent=root, title="select a file",filetypes=(('music files', '.mp3'), ('all files', '.*')))
    l23 = root.splitlist(filename)
    rt=[]
    List_ = list(l23)
    for i in List_:
        m2.append(i)
        we=i.split("/")
        ee=we[4]
        ty=ee.replace(".mp3","")
        rt.append(ty)
    com=ttk.Combobox(root,value=rt,width=20,state="readonly")
    com.current(0)    
    com.place(x=335,y=10)
    btn2.config(state = NORMAL)
    btn4.config(state = NORMAL)
    lbl()
def stop():
    global play_
    mixer.music.stop()
    play_ = False
    btn3.config(text = "play")

    sliderlbl.config(text="--:--:-- / --:--:--")
def pandc(e):
    global pc
    if play_:
        if pc == "pause":
            pc = "resume"
            btn3.config(text = pc)
            mixer.music.pause()
        else:
            pc = "pause"
            btn3.config(text= pc)
            mixer.music.unpause()
    else:
        pc = "pause"
        btn3.config(text=pc)
        play()
def file(e):
    global filename , play_,pc,currentsong
    lbl4.config(text="")
    lbl3.config(text="")
    stop()
    filename = filedialog.askopenfilename(parent = root,title = "select a file",filetypes =(('music files', '.mp3'),('all files', '.*')))
    lblm2()

    currentsong = filename

    play_ = True
    pc = "pause"
    btn3.config(text = pc)
    play()
def volume(n):

    try:
        if n=="10":
            
            ll.config(text="  Max \nVolume")
            ll.place(x=586,y=135)
        elif n=="2"or n=="1":
            ll.config(text="  Min \nVolume",)
            ll.place(x=586,y=135)
        elif n=="0":
            ll.config(text="Mute",)
            ll.place(x=594,y=136)
        else:
            ll.config(text="Volume")
            ll.place(x=587,y=136)
        mixer.music.set_volume(float(slider.get()/10))
    except:
        mixer.music.set_volume(0)
def button_():
    global root,btn3,slider,btn4,btn2,btn5,slider
    btn2 = Button(root, text="◄◄", font = ("cool jazz", 11, "bold"), bg = "#F9A0A3", state = DISABLED, command = previus,relief=RAISED,borderwidth=2)
    btn3 = Button(root,text = pc,command = lambda:pandc("e"),padx = 10, font = ("cool jazz", 11, "bold"),bg = "#F9A0A3",relief=RAISED)
    btn4 = Button(root, text="►►", font = ("cool jazz", 11, "bold"),bg = "#F9A0A3",state = DISABLED, command = next1,relief=RAISED,borderwidth=2)
    btn5 = Button(root, text="stop", command = stop, font = ("cool jazz", 11, "bold"),bg = "#F9A0A3",relief=RAISED)
    btn6 = Button(root, text = "playlist", command = lambda:playlist("e"), font = ("cool jazz", 11, "bold"),bg = "#F9A0A3",relief=RAISED)
    
    
    # btn6.place(x=200)
    btn5.place(x=520,y=398)
    btn2.place(x=200,y=398)
    btn3.place(x=300,y=398)
    btn4.place(x=420, y=398)
    volume(1)
    slider = Scale(root,from_ = 10, to = 0,font = ("cool jazz", 11, "bold"), bg = "#F9A0A3", command = volume,showvalue=5,relief=FLAT)
    slider.set(5)
    
    slider.place(x = 590,y =25)
def button():
    global root,btn1,l1
    btn1 = Button(root,text="open",command=lambda:file("e"), font = ("cool jazz", 11, "bold"),bg = "#F9A0A3",relief=RAISED)
    btn1.place(x=100,y=398)
    
    # btnexit = Button(root,text="exit",command=root.destroy, font = ("cool jazz", 11, "bold"),bg = "#FBC1C1")
    # btnexit.place(x=315,y=110)
def default():
        root.config(bg="#FBC1C1")
        red_frame.config(bg="#F68E92",relief=FLAT,bd=2)
        slider.config(bg="#F9A0A3",fg="black",relief=FLAT,bd=1)
        try:
            l1.config(bg="#FBC1C1")
        except:
            pass
        try:
            lbl4.config(bg="#F68E92",fg="black")   
        except:
            pass
        
        lbl9.config(bg="#FBC1C1",fg="black")
        lbl91.config(bg="#FBC1C1",fg="black")
        lbl2.config(bg="#F68E92",fg="black")
        l.config(relief=FLAT,bd=0,highlightthickness=0,bg="#FBC1C1",fg="black")
        en.config(relief=GROOVE,bd=2,bg="white",fg="black")
        btn1.config(bg = "#F9A0A3",fg="black",bd=1)
        btn2.config(bg = "#F9A0A3",fg="black",bd=1)
        btn3.config(bg = "#F9A0A3",fg="black",bd=1)
        btn4.config(bg = "#F9A0A3",fg="black",bd=1)
        btn5.config(bg = "#F9A0A3",fg="black",bd=1)
        sliderlbl.config(bg = "#FBC1C1",fg="black")
        ll.config(bg="#FBC1C1",fg="black")
        try:
            b1.config(bg="#FBC1C1",fg="black",relief=GROOVE,bd=2)
            b2.config(bg="#FBC1C1",fg="black",relief=GROOVE,bd=2)
            b3.config(bg="#FBC1C1",fg="black",relief=GROOVE,bd=2)
        except:
            pass
        file1.config(bg="white",fg="black",activebackground="#3498DB")
        file2.config(bg="white",fg="black",activebackground="#3498DB")
        file3.config(bg="white",fg="black",activebackground="#3498DB")
        try:
            lbl4.config(bg="#F68E92")
        except:
            pass
        try:
            lbl3.config(bg="#F68E92")
        except:
            pass

def quiet():
        import pyautogui as py
        py.alert(title="IM Player UI",text="This theme is currently not supported on your device ")
        pass
        # root.config(bg="#D4B996")
        # red_frame.config(bg="#D4B996",relief=FLAT,highlightthickness=1,highlightcolor="#A07855",highlightbackground="#A07855")
        # slider.config(bg="#A07855",fg="black",relief=RAISED,bd=3)
        # try:
        #     lbl4.config(bg="#D4B996",fg="black")   
        # except:
        #     pass
        # lbl3.config(bg="#A07855",fg="black")
        # lbl9.config(bg="#D4B996",fg="black")
        # lbl91.config(bg="#D4B996",fg="black")
        # lbl2.config(bg="#D4B996",fg="black")
        # l.configure(activestyle="none",fg="black",bg="#D4B996",relief=FLAT,bd=0,highlightthickness=0)
        # en.config(relief=RAISED,bd=4,bg="white",fg="black")
        # btn1.config(bg = "#A07855",fg="black",bd=4,relief=RAISED)
        # btn2.config(bg = "#A07855",fg="black",bd=4,relief=RAISED)
        # btn3.config(bg = "#A07855",fg="black",bd=4,relief=RAISED)
        # btn4.config(bg = "#A07855",fg="black",bd=4,relief=RAISED)
        # btn5.config(bg = "#A07855",fg="black",bd=4,relief=RAISED)
        # sliderlbl.config(bg = "#D4B996",fg="black")
        # ll.config(bg="#D4B996",fg="black")
        # try:
        #     b1.config(bg="#D4B996",fg="black",relief=FLAT,highlightthickness=1,highlightcolor="#A07855",highlightbackground="#A07855")
        #     b2.config(bg="#D4B996",fg="black",relief=FLAT,highlightthickness=1,highlightcolor="#A07855",highlightbackground="#A07855")
        #     b3.config(bg="#D4B996",fg="black",relief=FLAT,highlightthickness=1,highlightcolor="#A07855",highlightbackground="#A07855")
        # except:
        
        #     pass
        # file1.config(bg="white",fg="black",activebackground="#3498DB")
        # file2.config(bg="white",fg="black",activebackground="#3498DB")
        # file3.config(bg="white",fg="black",activebackground="#3498DB")
        # try:
        #     lbl4.config("#A07855")
        # except:
        #     pass
        # try:
        #     lbl3.config("#A07855")
        # except:
        #     pass

def light12():
   
        root.config(bg="#f6ead4")
        red_frame.config(bg="#f6ead4",bd=1,highlightthickness=2,relief=FLAT,highlightcolor="#b4a284",highlightbackground="#b4a284")
        slider.config(bg="#b4a284",fg="black",relief=RAISED,bd=3)
        try:
            l1.config(bg="#f6ead4")
        except:
            pass
        try:
            lbl4.config(bg="#f6ead4",fg="black")   
        except:
            pass
        lbl4.config(bg="#f6ead4",fg="black")   
        lbl3.config(bg="#f6ead4",fg="black")
        en.config(relief=RAISED,bd=3,bg="white",fg="black")
        l.config(relief=FLAT,bg="#f6ead4",fg="black",bd=0,highlightthickness=0)
        lbl9.config(bg="#f6ead4",fg="black")
        lbl91.config(bg="#f6ead4",fg="black")
        lbl2.config(bg="#f6ead4",fg="black")
        btn1.config(bg = "#f6ead4",fg="black",bd=3)
        btn2.config(bg = "#f6ead4",fg="black",bd=3)
        btn3.config(bg = "#f6ead4",fg="black",bd=3)
        btn4.config(bg = "#f6ead4",fg="black",bd=3)
        btn5.config(bg = "#f6ead4",fg="black",bd=3)
        sliderlbl.config(bg = "#f6ead4",fg="black")
        ll.config(bg="#f6ead4",fg="black")
        try:
            b1.config(bg="#a2a595",fg="white",relief=RAISED,bd=6)
            b2.config(bg="#a2a595",fg="white",relief=RAISED,bd=6)
            b3.config(bg="#a2a595",fg="white",relief=RAISED,bd=6)
        except:
            pass
        file1.config(bg="white",fg="black",activebackground="#b4a284")
        file2.config(bg="white",fg="black",activebackground="#b4a284")
        file3.config(bg="white",fg="black",activebackground="#b4a284")
        try:
            lbl4.config(bg="#f6ead4",fg="black")
        except:
            pass
        try:
            lbl3.config(bg="#f6ead4",fg="black")
        except:
            pass

def light():
   
        root.config(bg="#FBC1C1")
        red_frame.config(bg="#F68E92",relief=RAISED,bd=5,highlightthickness=0)
        slider.config(bg="#F9A0A3",fg="black",relief=RAISED,bd=5)
        try:
            l1.config(bg="#FBC1C1")
        except:
            pass
        try:
            lbl4.config(bg="#F68E92",fg="black")   
        except:
            pass
        lbl4.config(bg="#F68E92",fg="black")   
        en.config(relief=RAISED,bd=3,bg="white",fg="black")
        l.config(relief=FLAT,bd=0,highlightthickness=0,bg="#FBC1C1",fg="black")
        lbl9.config(bg="#FBC1C1",fg="black")
        lbl91.config(bg="#FBC1C1",fg="black")
        lbl2.config(bg="#F68E92",fg="black")
        btn1.config(bg = "#F9A0A3",fg="black",bd=2)
        btn2.config(bg = "#F9A0A3",fg="black",bd=2)
        btn3.config(bg = "#F9A0A3",fg="black",bd=2)
        btn4.config(bg = "#F9A0A3",fg="black",bd=2)
        btn5.config(bg = "#F9A0A3",fg="black",bd=2)
        sliderlbl.config(bg = "#F9A0A3",fg="black")
        ll.config(bg="#FBC1C1",fg="black")
        lbl3.config(bg="#F68E92")
        try:
            b1.config(bg="#F9A0A3",fg="black",relief=RAISED,bd=5)
            b2.config(bg="#F9A0A3",fg="black",relief=RAISED,bd=5)
            b3.config(bg="#F9A0A3",fg="black",relief=RAISED,bd=5)
        except:
            pass
        file1.config(bg="white",fg="black",activebackground="#F9A0A3")
        file2.config(bg="white",fg="black",activebackground="#F9A0A3")
        file3.config(bg="white",fg="black",activebackground="#F9A0A3")
        try:
            lbl4.config(bg="#F68E92",fg="black")
        except:
            pass
        try:
            lbl3.config(bg="#F68E92")
        except:
            pass

def dark():
    
        root.config(bg= "grey20")
        red_frame.config(bg="grey30",relief=RAISED,bd=5,highlightthickness=0)
        slider.config(bg="black",fg="white",relief=RAISED,bd=5,highlightthickness=0)
        btn1.config(bg = "black",fg="white",bd=4)
        try:
            l1.config(bg="grey20")
        except:
            pass
        try:
            lbl4.config(bg="grey30",fg="white")
        except:
            pass
        try:
            lbl3.config(bg="grey30",fg="white")
        except:
            pass
        lbl3.config(bg="grey30",fg="white")
        lbl4.config(bg="grey30",fg="white")
        en.config(relief=RAISED,bd=4,bg="grey30",fg="white")
        l.config(relief=FLAT,bg="grey20",fg="white",bd=0,highlightthickness=0,)
        lbl9.config(bg="grey20",fg="#EC407A")
        lbl91.config(bg="grey20",fg="#EC407A")
        lbl2.config(bg="grey30",fg="black")
        btn2.config(bg = "black",fg="white",bd=4)
        btn3.config(bg = "black",fg="white",bd=4)
        btn4.config(bg = "black",fg="white",bd=4)
        btn5.config(bg= "black",fg="white",bd=4)
        try:
            b1.config(bg= "grey30",fg="white",relief=RAISED,bd=6)
            b2.config(bg= "grey30",fg="white",relief=RAISED,bd=6)
            b3.config(bg= "grey30",fg="white",relief=RAISED,bd=6)
        except:
            pass
        sliderlbl.config(bg= "grey20",fg="white")
        file1.config(bg="grey10",fg="white",activebackground="grey30")
        file2.config(bg="grey10",fg="white",activebackground="grey30")
        file3.config(bg="grey10",fg="white",activebackground="grey30")
        ll.config(bg="grey20",fg="white")

def dark1():
    root.attributes("-alpha",0.05)
def light1():
    root.attributes("-alpha",0.95)
def menu_bar():
    global root,file1,file2,file3
    menu = Menu(root)
    file1 = Menu(menu, tearoff = 0,fg="black",bg="white",font=(' Helvetica bold','10'),bd=0)    
    file1.add_command(label = "open", command = lambda:file("e"))
    file1.add_command(label = "playlist", command = lambda:playlist("e"))
    menu.add_separator()
    file1.add_command(label="quit", command=root.destroy)
    menu.add_cascade(label="Options", menu=file1)
    file2 = Menu(menu, tearoff = 0,fg="black",bg="white",font=(' Helvetica bold','10'),bd=0)    
    file2.add_command(label = "Dark", command = dark)
    file2.add_command(label = "Light", command = light)
    file2.add_command(label = "Peach", command = light12)
    file2.add_command(label = "Quiet", command = quiet)
    file2.add_command(label = "Default", command = default)
    menu.add_cascade(label="Themes", menu=file2)
    file3 = Menu(menu, tearoff = 0,fg="black",bg="white",font=(' Helvetica bold','10'),bd=0)    
    file3.add_command(label = "Blend Mode", command = dark1)
    file3.add_command(label = "Normal Mode", command = light1)
    menu.add_cascade(label="Modes", menu=file3)
    menu.add_separator()
    root.config(menu=menu)

def time(): 
    string = strftime('%I:%M %p')
    root.title("Music Player  -   "+string)
    root.after(1000, time)

deu=[]
default1=root.cget('bg')


def update(data):
    l.delete(0,END)
    for i in data:
        l.insert(END,i)
    
def fillout(e):
    en.delete(0,END)
    en.insert(0,l.get(ANCHOR))
    
def check(e):
    typ=en.get()
    if  typ == " " or typ=="":
        data=""
        
    else:
        data=[]
        for i in gana:
            i=i.strip()
            typ=typ.strip()
            if typ.lower() in i.lower():
                data.append(i)
    update(data)
try:
    ert=open("recently played(np1).txt")
    for i in ert:
        deu.append(i)
    le=len(deu)
    st=deu[le-1].split("/")

    st=st[4].replace("mp3","")
    st1=deu[le-2].split("/")
    st1=st1[4].replace("mp3","")
    st2=deu[le-3].split("/")
    st2=st2[4].replace("mp3","")
except:
    global l1
    l1=Label(root,text=" Recently Played songs will be visible here next time ",bg="#FBC1C1",height=2,relief=RAISED,font = ("cool jazz", 13))
    l1.place(x=55, y=65)
def pl():
    lbl4.config(text="")
    lbl3.config(text="")
    stop()
    global currentsong
    global play_,consonglen
    n=(deu[le-1].replace("/","//").replace("\n",""))
    load(n)
    mixer.music.play()
    currentsong=n
    play_ = True
    pc = "pause"
    btn3.config(text = pc)
    play_time() 
    defau2=root.cget('bg')
    lbl3.config(text="") 
    if defau2=="#FBC1C1" or defau2=="#f6ead4" :
        lbl4.config(text=st.replace("\n",""),justify = CENTER,wraplength=500, font = ("cool jazz", 13),fg="black")
    else:
        lbl4.config(text=st.replace("\n",""),justify = CENTER,wraplength=500, font = ("cool jazz", 13),fg="white")
    sliderlbl.after(int(songlength), play_time) 

def pl1():
    lbl4.config(text="")
    lbl3.config(text="")
    stop()
    global currentsong
    global play_,consonglen
    n=(deu[le-2].replace("/","//").replace("\n",""))
    load(n)
    mixer.music.play()
    currentsong=n
    play_ = True
    pc = "pause"
    btn3.config(text = pc)
    play_time()
    defau2=root.cget('bg')
    lbl3.config(text="")
    if defau2=="#FBC1C1" or defau2=="#f6ead4" :
        lbl4.config(text=st1.replace("\n",""),justify = CENTER,wraplength=500, font = ("cool jazz", 13),fg="black")
    else:
        lbl4.config(text=st1.replace("\n",""),justify = CENTER,wraplength=500, font = ("cool jazz", 13),fg="white")
    sliderlbl.after(int(songlength), play_time) 

def pl2():
    lbl4.config(text="")
    lbl3.config(text="")
    stop()
    global currentsong
    global play_,consonglen
    n=(deu[le-3].replace("/","//").replace("\n",""))
    load(n)
    mixer.music.play()
    currentsong=n
    play_ = True
    pc = "pause"
    btn3.config(text = pc)
    play_time()
    lbl3.config(text="")
    defau2=root.cget('bg')
    if defau2=="#FBC1C1" or defau2=="#f6ead4" :
        lbl4.config(text=st2.replace("\n",""),justify = CENTER,wraplength=500, font = ("cool jazz", 13),fg="black")
    else:
        lbl4.config(text=st2.replace("\n",""),justify = CENTER,wraplength=500, font = ("cool jazz", 13),fg="white")
    sliderlbl.after(int(songlength), play_time) 

def callit1():
        import pyautogui as py
        py.alert(text="1) New Refreshed UI  \n\n2) Bugs Fix \n\n3) More Themes with 3D effects added \n\n4) New Ai autocomplete featue has been added \n\n5) From now you can jump back to the last song you've listened, just \n    tap the 3d label in the Recently Played pannel to listen \n\n6) New Blend overlay added ",title="See What's new ")
        erm=open("last.txt","a")
        erm.write("yes")
        erm.close()

def main():
    global root,lbl2,ll,lbl4,red_frame,lbl3,sliderlbl,lbl9,b1,b2,defaultblue,b3,lbl91,progress_bar
    root.attributes("-topmost",True)
    time()
    root.attributes("-alpha",.95)
    root.geometry("655x468+350+250")
    defaultblue=root.cget('bg')
    red_frame = Frame(root, highlightthickness=1, background="#F68E92",relief=FLAT)
    red_frame.place(x=9.8, y=315, relwidth=.97, relheight=.29)
    defaultb=red_frame.cget('bg')
    root.config(bg = "#FBC1C1")
    root.resizable(0,0)
    lbl2 = Label(text="Playing - ",justify = CENTER, font = ("calibrelight", 15,), bg="#F68E92",fg="black")
    lbl2.place(x=19, y=325) 
    lbl3=Label(root,bg=defaultb)
    lbl3.place(x=117.5, y=328)
    lbl4 = Label(text="No songs selected",justify = CENTER,wraplength=500, font = ("cool jazz", 14),fg="grey",bg="#F68E92")
    lbl4.place(x=117.5, y=328)
    lbl9 = Label(text="Recently Played ",justify = CENTER, font = ("calibri", 22,"bold"),fg="black",bg="#FBC1C1")
    lbl9.place(x=13, y=4)
    lbl91 = Label(text="Search",justify = CENTER, font = ("calibri", 18,),fg="black",bg="#FBC1C1")
    lbl91.place(x=36, y=180)
    try:
        b1=Button(root,text="\n\n"+st+'\n',wraplength=130,bg="#FBC1C1",height=6,relief=GROOVE,command=pl,bd=2)
        b2=Button(root,text="\n\n"+st1+'\n',wraplength=130,bg="#FBC1C1",height=6,relief=GROOVE,command=pl1,bd=2)
        b3=Button(root,text="\n\n"+st2+'\n',wraplength=130,bg="#FBC1C1",height=6,relief=GROOVE,command=pl2,bd=2)
        b1.place(x=22, y=56)
        b2.place(x=220, y=56)
        b3.place(x=418, y=56)
    except:
        pass
    sliderlbl = Label(root, text = "--:--:-- / --:--:--",bg=defaultb)
    sliderlbl.place(x = 531, y = 360)
    progress_bar = ttk.Progressbar(root, orient="horizontal", mode="determinate", length=400)
    progress_bar.place(x=126, y=360)  
    # myslider = ttk.Scale(root, from_=0, to = 100, orient= HORIZONTAL, command = slide, length = 360, value = 0)
    # myslider.place(x=70,y=125)
    ll=Label(root,text="Volume", font = ("cool jazz", 11, "bold"),bg="#FBC1C1")
    ll.place(x=584,y=215)
    button()
    button_()
    menu_bar()

    def foc(e):
        en.focus_set()
        

    # root.iconbitmap("c:\\er.ico")
    l.bind("<<ListboxSelect>>",fillout) 
    en.bind("<KeyRelease>",check) 
    root.bind("<space>",pandc)
    root.bind("<Control-p>",playlist)
    root.bind("<Control-s>",foc)
    root.bind("<Control-o>",file)
    import pyautogui as py
    root.update() 
    mr1=open("last.txt","r")
    ip=[]
    for i12 in mr1:
        
        ip.append(i12)
    if "yes"  in ip:
        pass  
    else:
        callit1()
    mr1.close()
    # confirm(text='', title='', buttons=['OK', 'Cancel'])

    pop()
    root.mainloop()
main()
 
