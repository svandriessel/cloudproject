from tkinter import *
import time
import random
import _thread
import subprocess

root = Tk()
root.geometry("800x480")

list_of_barcodes = [65833254, 12345678, 22222222, 33333333, 44444444]
productcode = 00000000
currentProduct = None
scannedProducts = []
scannedObjects = []

def loop():
    while 1:
        print('a')
        update_info()
        time.sleep(1)
        
    
def volgende_artikel():
    #het volgende artikel wordt gescand
    i = random.randint(0,4)
    productcode = list_of_barcodes[i]

    currentProduct = Goods(productcode)
    scannedObjects.append(currentProduct)

    #scannedProducts.append(productcode)
    if productcode == 22222222:
        productBeschrijving = 'Yoghurt'
        scannedProducts.append(productBeschrijving)
    elif productcode == 65833254:
        productBeschrijving = 'Aardbei'
        scannedProducts.append(productBeschrijving)
    elif productcode == 12345678:
        productBeschrijving = 'Banaan'
        scannedProducts.append(productBeschrijving)
    elif productcode == 33333333:
        productBeschrijving = 'Brood'
        scannedProducts.append(productBeschrijving)
    elif productcode == 44444444:
        productBeschrijving = 'Kiwi'
        scannedProducts.append(productBeschrijving)

    print(productcode)
    print(scannedProducts)

def clear_products():
    productCode = 00000000
    scannedProducts[:] = []
    print('all clear')

def update_info():
    product_text.delete('1.0', END)
    #product_text.insert('1.0', currentProduct.returnName(), CENTER)
    list_text.delete('1.0', END)
    list_text.insert('1.0', '\n'.join(scannedProducts), CENTER)

def plusOne():
    print('add one to article 1')

def plusTwo():
    print('add one to article 2')

def plusThree():
    print('add one to article 3')

def plusFour():
    print('add one to article 4')

def MinusOne():
    print('subtract one from article 1')

def MinusTwo():
    print('subtract one from article 2')

def MinusThree():
    print('subtract one from article 3')

def MinusFour():
    print('subtract one from article 4')




        
topFrame = Frame(root)
midFrame = Frame(root)
empty = Frame(root, height=20,width=15)
bottomFrame = Frame(root)

product_text = Text(midFrame, font=("Neuropol X Rg",20), height=5, width=10)
product_text.tag_configure("center", justify='center')
product_text.pack(side=LEFT)
product_text.insert('1.0', '00000000', CENTER)

list_text = Text(midFrame, font=("Neuropol X Rg",20), height=5, width=10)
list_text.tag_configure("center", justify='center')
list_text.pack(side=LEFT)
list_text.insert('1.0', '00000000', CENTER)

plus1 = Button(midFrame, text="plus", fg="blue", command = plusOne)

Minus1 = Button(midFrame, text="Minus", fg="blue", command = MinusOne)


plus1.pack(side=RIGHT)
Minus1.pack(side=RIGHT)

artikel_button = Button(bottomFrame, text="volgende artikel", fg="red", command = volgende_artikel)
artikel_button.pack(side=LEFT)

clear_button = Button(bottomFrame, text="clear", fg="red", command = clear_products)
clear_button.pack(side=LEFT)

topFrame.grid(row=0)
midFrame.grid(row=2)
empty.grid(row=1)
bottomFrame.grid(row=3)

class Goods(object):
    #class voor Goods objecten
    def __init__(self, barcode, amount=1):
        self.barcode = barcode
        self.amount = amount
    def addAmount(addition):
        self.amount += addition
    def returnName():
        if productcode == 22222222:
            productBeschrijving = 'Yoghurt'
        elif productcode == 65833254:
            productBeschrijving = 'Aardbei'
        elif productcode == 12345678:
            productBeschrijving = 'Banaan'
        elif productcode == 33333333:
            productBeschrijving = 'Brood'
        elif productcode == 44444444:
            productBeschrijving = 'Kiwi'
        return productBeschrijving
    
    #einde class Goods        

_thread.start_new_thread(loop,())
root.mainloop()
