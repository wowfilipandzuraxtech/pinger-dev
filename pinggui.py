from tkinter import *
import config as conf
from tkinter import *
root = Tk()
import platform
if platform == "Windows":
  root.geometry("1600x860")

else:
    pass

root.title("online check")
root.attributes("-zoomed", True)



bg = PhotoImage(file = "settings2.png")


kn = Entry(root,width=30,font="Italic",bg="red")
png = Entry(root,width=40,font="Italic")
mode = Entry(root, width=10,font="Italic")

mode.insert(END, "intense")
png.insert(END, "")
kn.insert(END, "")
#btn = Button(root,width=120,height=2,font="Italic",fg="red",text="waiting...")

def settingsfunct():
 btn.forget()
 btn3 = Button(root, width=120, height=2, font="Italic", fg="green", text="open settings...", command=settingsfunct)
 btn3.place(x=50,y=0)

 settings = Tk()
 settings.title("pinger set")

 settings.mainloop()

def checkping():

 import socket
 try:
   try:
      print(t)
      knc.forget()
      forget.rq()

   except:
       pass

   t = socket.gethostbyname(png.get())

   if "1" or ("2") or ("3") or ("4") or ("5") or ("6") or ("7") or ("8") or ("9") or ("10") in t: #ip detection
     iptype = Label(root,text="IPV4",font="Italic",fg="darkgreen")
     iptype.place(x=508,y=460)

   else:
       iptype = Label(root, text="IPV6", font="Italic", fg="darkgreen")
       iptype.place(x=508, y=460)

   btn.forget()
   u = Label(root,text=t,fg="darkgreen",font="Italic")
   rq = Label(root,text="from: ",fg="darkgreen")

   rq.place(x=510,y=440)
   u.place(x=560,y=440)

 except:
    btn.forget()
    btn2 = Button(root, width=120, height=2, font="Italic", fg="darkred", text="offline!")
    btn2.place(x=40,y=0)
    if conf.dom == "yes":
      if mode.get() == "intense":
        try:
          knc = socket.gethostbyname(png.get() + ".xyz")
          inf = Label(root,text="[info] available with .xyz",fg="darkgreen",font="Italic")
          inf.place(x=560,y=400)
        except:
            pass

        try:
          knc = socket.gethostbyname(png.get() + ".sk")
          inf = Label(root, text="[info] available with .sk", fg="darkgreen", font="Italic")
          inf.place(x=560, y=420)
        except:
            pass

        try:
          knc = socket.gethostbyname(png.get() + ".eu")
          inf = Label(root, text="[info] available with .eu", fg="darkgreen", font="Italic")
          inf.place(x=560, y=440)
        except:
             pass

        try:
           knc = socket.gethostbyname(png.get() + ".cz")
           inf = Label(root, text="[info] available with .cz", fg="darkgreen", font="Italic")
           inf.place(x=560, y=460)
        except:
            pass

        try:
            knc = socket.gethostbyname(png.get() + ".gg")
            inf = Label(root, text="[info] available with .gg", fg="darkgreen", font="Italic")
            inf.place(x=560, y=480)
        except:
            pass

        try:
           knc = socket.gethostbyname(png.get() + ".net")
           inf = Label(root, text="[info] available with .net", fg="darkgreen", font="Italic")
           inf.place(x=560, y=500)
           def chkf():
            png.insert(END, png.get() + ".net")

           checkwithnet = Buttton(root,text="check .net",command=chkf,width=20,font="Italic",height=2)
           checkwithnet.place(x=590,y=500)

        except:
            pass

        try:
          knc = socket.gethostbyname(png.get() + ".com")
          inf = Label(root, text="[info] available with .com", fg="darkgreen", font="Italic")
          inf.place(x=560, y=520)

          def chkf():
           png.insert(END, png.get() + ".net")

          checkwithnet = Buttton(root, text="check .com", command=chkf, width=20, font="Italic", height=2,bg="dark")
          checkwithnet.place(x=400, y=10)

        except:
            pass

      try:
          knc = socket.gethostbyname(png.get() + ".pl")
          inf = Label(root, text="[info] available with .pl", fg="darkgreen", font="Italic")
          inf.place(x=560, y=540)
      except:
          pass


      else:
         pass






btn2 = Button(root, width=120, height=2, font="Italic", fg="darkgreen", text="online!")
btn2.place(x=50, y=0)




btn = Button(root,width=120,height=2,font="Italic",fg="red",text="waiting...",command=settingsfunct)
check = Button(root,width=50,height=2,font="Italic",text="check",command=checkping)
settings = Button(root,width=40,height=2,text="settings")


btn.place(x=40,y=0)
kn.place(x=590,y=200)
png.place(x=500,y=200)
check.place(x=450,y=600)
mode.pack()
#settings.place(x=510,y=200)

root.mainloop()