from tkinter import *
import time
import random
import _thread
import subprocess

root = Tk()
poppup = Toplevel()
root.geometry("800x480")
poppup.geometry("500x800")
root.configure(background='white')
poppup.configure(background='white')

list_of_barcodes = [65833254, 12345678, 22222222, 33333333, 44444444]
productcode = 00000000
currentProduct = None
scannedProducts = []
global productBeschrijving
productBeschrijving=' '
global currentProductIndex
currentProductIndex=None
photo = PhotoImage(file="welkom.gif")

def loop():
    while 1:
        update_info()
        time.sleep(0.1)
        
    
def volgende_artikel():
    #het volgende artikel wordt gescand
    #i = random.randint(0,4)
    productcode = list_of_barcodes[0] #hoort i 

    #scannedProducts.append(productcode)
    if productcode == 22222222:
        global productBeschrijving
        productBeschrijving = 'Yoghurt'
        
    elif productcode == 65833254:
        global productBeschrijving
        productBeschrijving = 'Aardbei'
        
    elif productcode == 12345678:
        global productBeschrijving
        productBeschrijving = 'Banaan'
        
    elif productcode == 33333333:
        global productBeschrijving
        productBeschrijving = 'Brood'
        
    elif productcode == 44444444:
        global productBeschrijving
        productBeschrijving = 'Kiwi'

    exists=False
    for p in scannedProducts:
        if p.count(productBeschrijving)!=0:
            exists=True
            p[1]+=1
            global currentProductIndex
            currentProductIndex=scannedProducts.index(p)
            select_product()
            break
    if exists==False:    
        artikel=[productBeschrijving, 1]
        scannedProducts.append(artikel)
        global currentProductIndex
        currentProductIndex=len(scannedProducts)-1
        select_product()

    

    poppup.deiconify()
    print(productcode)
    print(scannedProducts)

def clear_products():
    productCode = 00000000
    scannedProducts[:] = []
    product_text.delete('1.0', END)

    photo2 = PhotoImage(file="")
    picture_label.configure(image = photo2)
    picture_label.image=photo2
    global currentProductIndex
    currentProductIndex=None
    print('all clear')

def update_info():
    
    list_text.delete('1.0', END)
    for p in scannedProducts:
        list_text.insert('1.0', p[0]+' '+ str(p[1]) + '\n', CENTER)

def select_product():
    product_text.delete('1.0', END)
    if productBeschrijving!='':
        product_text.insert('1.0', str(scannedProducts[currentProductIndex][1]), CENTER)
        if productBeschrijving=='Yoghurt':
            photo2 = PhotoImage(file="Yoghurt.gif")
        elif productBeschrijving == 'Aardbei':
            photo2 = PhotoImage(file="milk2.gif")
        elif productBeschrijving == 'Banaan':
            photo2 = PhotoImage(file="Banaan.gif")
        elif productBeschrijving == 'Brood':
            photo2 = PhotoImage(file="Brood.gif")
        elif productBeschrijving == 'Kiwi':
            photo2 = PhotoImage(file="Kiwi.gif")
        picture_label.configure(image = photo2)
        picture_label.image=photo2
    
    print(productBeschrijving)

def plusOne():
    if currentProductIndex!=None and productBeschrijving!='':
        if scannedProducts[currentProductIndex][1]!=9:
           scannedProducts[currentProductIndex][1]+=1
           print('add one')
           select_product()

def MinusOne():
    if currentProductIndex!=None and productBeschrijving!='':
        if scannedProducts[currentProductIndex][1]>1:
            scannedProducts[currentProductIndex][1]-=1
            print('subtract one')
            select_product()
        elif scannedProducts[currentProductIndex][1]==1:
            scannedProducts.remove(scannedProducts[currentProductIndex])
            global currentProductIndex
            currentProductIndex=None
            global productBeschrijving
            productBeschrijving=''
            print('subtract to 0')
            photo2 = PhotoImage(file="")
            picture_label.configure(image = photo2)
            picture_label.image=photo2
            select_product()
            poppup.withdraw()

def removeCurrentProduct():
    scannedProducts.remove(scannedProducts[currentProductIndex])
    global currentProductIndex
    currentProductIndex=None
    global productBeschrijving
    productBeschrijving=''
    photo2 = PhotoImage(file="")
    picture_label.configure(image = photo2)
    picture_label.image=photo2
    select_product()

def quitPoppup():
    removeCurrentProduct()
    poppup.withdraw()
    print('quit poppup')

def confirm_product():
    print('confirm product')

top_label = Label(root, text='Scan het volgende artikel', height=2, width=113, bg='light blue')
top_label.grid(row=0, column=0, columnspan=9)

empty_label1 = Label(root, height=1, width=113, bg='white')
empty_label1.grid(row=1, column=0, columnspan=9)

empty_label2 = Label(root)
empty_label2.grid(row=2, column=0, rowspan=4)

empty_labelPoppup = Label(poppup, height=1, width=10, bg='white')
empty_labelPoppup.grid(row=0, column=0, columnspan=1)

picture_label = Label(poppup, image=photo, width=220, height=450, bg='white')
picture_label.photo=photo
picture_label.grid(row=1, column=1, columnspan=1)

product_text = Text(poppup, font=("Arial",70), fg='#4d4848', height=1, width=2, relief=FLAT)
product_text.tag_configure("center", justify='center')
product_text.grid(row=5, column=1)
product_text.insert('1.0', '00000000', CENTER)

listFrame=Frame(root)
listFrame.grid(row=3, column=1)

list_text = Text(root, font=(" Arial",20), height=5, width=12)
list_text.tag_configure("center", justify='center')
list_text.grid(row=2, column=1, columnspan=2)
list_text.insert('1.0', '00000000', CENTER)

plusPhoto = PhotoImage(file="plus4.gif")
plus1 = Button(poppup, text="plus", image=plusPhoto, fg="blue", width=130, height=150, anchor=W, activebackground='white', relief=SUNKEN, borderwidth=0, bg='white', command = plusOne)
plus1.photo=plusPhoto
minusPhoto = PhotoImage(file="minus4.gif")
Minus1 = Button(poppup, text="Minus", image=minusPhoto, fg="blue", width=130, height=150, anchor=E, activebackground='white', relief=SUNKEN, borderwidth=0, bg='white', command = MinusOne)
Minus1.photo=minusPhoto

quitPhoto = PhotoImage(file="cross2.gif")
quitPoppup = Button(poppup, text="Minus", image=quitPhoto, fg="black", width=80, activebackground='white', relief=SUNKEN, borderwidth=0, bg='white', command = quitPoppup)
quitPoppup.photo=quitPhoto
quitPoppup.grid(row=0, column=2)

plus1.grid(row=5, column=2)
Minus1.grid(row=5, column=0)

artikel_button = Button(root, text="volgende artikel", fg="red", command = volgende_artikel, width=20)
artikel_button.grid(row=4, column=2)

clear_button = Button(root, text="Clear", fg="red", command = clear_products, width=20)
clear_button.grid(row=4, column=1)

confirmPhoto = PhotoImage(file="add2.gif")
confirm_button = Button(poppup, image=confirmPhoto, bg='white', activebackground='white', relief=SUNKEN, borderwidth=0, command = confirm_product, width=310, height=80)
confirm_button.photo=confirmPhoto
confirm_button.grid(row=6, column=0, columnspan=3)

poppup.withdraw()

_thread.start_new_thread(loop,())
root.mainloop()
