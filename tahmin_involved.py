import tkinter as tk
import random

def kontrolEt():
    global sayac
    if sayi1.get().isdigit():
        s1 = int(sayi1.get())
        sayac = sayac + 1
        if s1 > sayi2:
            yazi2.configure(text='Daha az')
        elif s1 < sayi2:
            yazi2.configure(text='Daha fazla')
        else:
            yazi2.configure(text='{} defa da tahmin ettiniz'.format(sayac))
    sayi1.selection_range(0, tk.END)

pencere = tk.Tk()
pencere.title(' Sayi Tahmin Oyunu')
pencere.geometry('320x200')

yazi1 = tk.Label(pencere, text='1-10 arasında sayı giriniz', font='Courier 14 bold', width=25, justify='center')
yazi1.place(x=15, y=20)
sayi1 = tk.Entry(pencere, font='Courier 14 bold', width=15, justify='center')
sayi1.place(x=70, y=50)
sayi1.focus()
kontrol = tk.Button(pencere, text='Kontrol', font='Courier 14', width=10, command=kontrolEt)
kontrol.place(x=90, y=80)
yazi2 = tk.Label(pencere, text='', font='Courier 16 bold', width=25, justify='center')
yazi2.place(x=0, y=120)
sayi2 = random.randint(1, 10)
sayac = 0

pencere.mainloop()