from tkinter import *
from PIL import ImageTk, Image
import yfinance as yf

root = Tk()

root.title("Stock Bobba")
root.geometry("1000x1000")

hi2 = ""



def yesss(*args):
    try:
        hi = u.get()
        hi2 = hi
        tiger = yf.Ticker(hi)
        win = Toplevel(root)
        win.geometry("800x800")
        def btmye(*args):
            win.destroy()

        pe,eps = tiger.info['trailingPE'], tiger.info['trailingEps']
        price = pe * eps
        bye = Label(win, text="The predicted stock price of "+ hi + " is " + str(round(price, 2)), font=('kaiti bold',30), background='#2b2a26', fg = 'white', justify=CENTER)
        bye.place(relx = 0.3, rely=0.25)
        bag = Label(win, text="Take me back to home", font=('kaiti bold',30), background='#2b2a26', fg='white')
        bag.pack()
        bag.bind("<Button-1>", btmye)
        def yess():
            tiger = yf.Ticker(hi2)
            pe,eps = tiger.info['trailingPE'], tiger.info['trailingEps']
            price = pe * eps
            bye.configure(text="The predicted stock price of "+ hi2 + " is " + str(round(price, 2)))
            win.after(1000, yess)
            
        win.after(1000, yess)
        win.configure(bg='#2b2a26')
        
    except KeyError:
        root.destroy()

    


sideBars = ImageTk.PhotoImage(Image.open('Untitled-9.png'))
sideMan = Label(root, image=sideBars, bg="#2b2a26")
sideMan.pack(side=LEFT)#relx=0, relheight=1)


sideBars2 = ImageTk.PhotoImage(Image.open('Untitled-9(1).png'))
sideMan2 = Label(root, image=sideBars2, background='#2b2a26')
sideMan2.pack(side = RIGHT)#relx=0.763, relheight=1)

infot = Label(root, text="Please Enter The Stock Symbol", font=('kaiti bold',30), fg='white', bg='#2b2a26')
infot.place(relx = 0.33, rely=0.12)

u = Entry(root, width = 25, font='kati')
u.place(relx=0.412, rely=0.2)

b = Label(root, text='submit',fg='white', font=('kaiti bold',30), background='#2b2a26')
b.place(relx=0.467, rely=0.25)

b.bind("<Button-1>", yesss)

root.configure(bg='#2b2a26')

root.attributes('-fullscreen', True)

root.mainloop()