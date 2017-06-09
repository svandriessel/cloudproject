from tkinter import *
import time
import random
import _thread
import subprocess
from PIL import Image

root = Tk()
root.geometry("800x800")
root.configure(background='white')

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
    i = random.randint(0,4)
    productcode = list_of_barcodes[i]

    #scannedProducts.append(productcode)
    if productcode == 22222222:
        global productBeschrijving
        productBeschrijving = 'Yoghurt'
        
    elif productcode == 65833254:
        global productBeschrijving
        productBeschrijving = 'melk'
        
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
        elif productBeschrijving == 'melk':
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
           addOneToAantal(currentProductIndex)
           print('add one')
           select_product()

def MinusOne():
    if currentProductIndex!=None and productBeschrijving!='':
        if scannedProducts[currentProductIndex][1]>1:
            scannedProducts[currentProductIndex][1]-=1
            subtractOneOfAantal(currentProductIndex)
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

def removeProduct(row):
    for i in len(productenTabel[row]):
        productenTabel[row][column].configure(text=text)# --------------------------------------------------

def addOneToAantal(row):
    productenTabel[row][1].configure(text=productenTabel[row][1]+1)

def subtractOneOfAantal(row):
    productenTabel[row][1].configure(text=productenTabel[row][1]-1)  

def changeCel(row, column, text):
    productenTabel[row][column].configure(text=text)
    

#top_label = Label(root, text='Scan het volgende artikel', height=2, width=113, bg='light blue')
#top_label.grid(row=0, column=0, columnspan=9)

quitPhoto = PhotoImage(file="cross2.gif")
quitPoppup = Button(root, text="Minus", image=quitPhoto, fg="black", width=100, activebackground='white', relief=SUNKEN, borderwidth=0, bg='white')#, command = quitPoppup)
quitPoppup.photo=quitPhoto
quitPoppup.grid(row=0, column=7)

empty_label1 = Label(root, height=1, width=113, bg='white')
empty_label1.grid(row=1, column=0, columnspan=9)

empty_label2 = Label(root)
empty_label2.grid(row=2, column=0, rowspan=4)

picture_label = Label(root, image=photo, width=400, height=450, bg='white')
picture_label.photo=photo
picture_label.grid(row=2, column=5, columnspan=3)

product_text = Text(root, font=("Arial",70), fg='#4d4848', height=1, width=2, relief=FLAT)
product_text.tag_configure("center", justify='center')
product_text.grid(row=4, column=6)
product_text.insert('1.0', '00000000', CENTER)

list_text = Text(root, font=("Arial",20), height=5, width=12)
list_text.tag_configure("center", justify='center')
list_text.grid(row=2, column=1, columnspan=2)
list_text.insert('1.0', '00000000', CENTER)
list_text.grid_forget()

listFrame=Frame(root, bg='#4d4848')
listFrame.grid(row=2, column=1, columnspan=3)

productenTabel =[]
for i in range(7):
    tableRow=[]
    for j in range(4):
        l = Label(listFrame, text='', font=("Arial", 10), fg='#0080FF', relief=FLAT, bg='white')
        l.grid(row=i, column=j, sticky=NSEW, padx=1, pady=1)
        tableRow.append(l)
    productenTabel.append(tableRow)

productenTabel[0][0].configure(text="Product", width=18, font=("Arial", 10, "bold"), fg='#0080FF')
productenTabel[0][1].configure(text="Aantal", width=7, font=("Arial", 10, "bold"), fg='#0080FF')
productenTabel[0][2].configure(text="Prijs", width=7, font=("Arial", 10, "bold"), fg='#0080FF')
productenTabel[0][3].configure(text="Totaal", width=7, font=("Arial", 10, "bold"), fg='#0080FF')

changeCel(1, 0, "Melk")
changeCel(1, 1, "1")
changeCel(1, 2, "€2,50")
changeCel(1, 3, "€2,50")

plusPhoto = PhotoImage(file="plus4.gif")
plus1 = Button(root, text="plus", image=plusPhoto, fg="blue", width=100, height=150, activebackground='white', relief=SUNKEN, borderwidth=0, bg='white', command = plusOne)
plus1.photo=plusPhoto
minusPhoto = PhotoImage(file="minus4.gif")
Minus1 = Button(root, text="Minus", image=minusPhoto, fg="blue", width=100, activebackground='white', relief=SUNKEN, borderwidth=0, bg='white', command = MinusOne)
Minus1.photo=minusPhoto

plus1.grid(row=4, column=7)
Minus1.grid(row=4, column=5)

artikel_button = Button(root, text="volgende artikel", fg="red", command = volgende_artikel, width=20)
artikel_button.grid(row=4, column=2)

clear_button = Button(root, text="Clear", fg="red", command = clear_products, width=20)
clear_button.grid(row=4, column=1)

confirmPhoto = PhotoImage(file="add2.gif")
confirm_button = Button(root, image=confirmPhoto, bg='white', activebackground='white', relief=SUNKEN, borderwidth=0, width=310, height=80)#, command = confirm_product)
confirm_button.photo=confirmPhoto
confirm_button.grid(row=6, column=5, columnspan=3)


_thread.start_new_thread(loop,())
root.mainloop()
