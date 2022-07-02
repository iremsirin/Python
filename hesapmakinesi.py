from tkinter import *
import tkinter as tk
def kok():
    s1=float(sayi1.get())
    sonuc.configure(text=str(s1**.5))
def bolme():
    
    s1=float(sayi1.get())
    s2=float(sayi2.get())
    sonuc.configure(text=str(s1/s2))

def carpma():
    
    s1=float(sayi1.get())
    s2=float(sayi2.get())
    sonuc.configure(text=str(s1*s2))


def cikar():
    
    s1=float(sayi1.get())
    s2=float(sayi2.get())
    sonuc.configure(text=str(s1-s2))

def topla():
    
    s1=float(sayi1.get())
    s2=float(sayi2.get())
    sonuc.configure(text=str(s1+s2))
    

w = Tk()
w.title('HESAP MAKİNESİ')
w.geometry("320x360")

sonuc = tk.Label(w, text= " Sonuç ", font="Arial 15 italic", width=20, justify="center")
sonuc.place(x=30, y=20)
sayi1 = tk.Entry(w, font="Ariel 15 italic", width=15, justify="right")
sayi1.place(x=70, y=50)
sayi2 = tk.Entry(w, font="Ariel 15 italic", width=15, justify="right")
sayi2.place(x=70, y=80)

tus1 = tk.Button(w, text="+", font="Ariel 14 italic",width=10, command=topla,bg="lightpink")
tus1.place(x=90, y=120)
tus2 = tk.Button(w, text="-", font="Ariel 14 italic",width=10, command=cikar,bg="pink")
tus2.place(x=90, y=150)
tus3 = tk.Button(w, text="*", font="Ariel 14 italic",width=10, command=carpma,bg="hotpink")
tus3.place(x=90, y=180)
tus4 = tk.Button(w, text="/", font="Ariel 14 italic",width=10, command=bolme,bg="deeppink")
tus4.place(x=90, y=210)

def temizle():
    sonuc.configure(text="")
    sayi1.delete(0, tk.END)
    sayi2.delete(0, tk.END)
tus5 = tk.Button(w, text="Temizle", font="Ariel 14 italic", width=10, command=temizle,bg="mediumvioletred")
tus5.place(x=90, y=280)

tus6 = tk.Button(w,text='√',font="Ariel 14 italic",width="10",command=kok,bg="mediumorchid")
tus6.place(x=90,y=240)

def kapat(): 
    w.destroy()

tus7 =tk.Button(w, text = "Kapat",font="Ariel 14 italic",width="10", command = kapat,bg="darkmagenta")
tus7.place(x=90,y=320)



sayi1.focus

w.mainloop()

