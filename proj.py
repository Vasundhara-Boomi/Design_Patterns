import json
import re
fromclass CapitalIterable():
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        return CapitalIterator(self.lst)

class CapitalIterator():
    def __init__(self, lst):
        self.lst = lst
        self.index = 0

    def __iter__(self):
        return self
        
    def __next__(self):
        if self.index == len(self.lst):
            raise StopIteration()

        x = self.lst[self.index]
        self.index =self.index+1
        return xclass CapitalIterable():
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        return CapitalIterator(self.lst)

class CapitalIterator():
    def __init__(self, lst):
        self.lst = lst
        self.index = 0

    def __iter__(self):
        return self
        
    def __next__(self):
        if self.index == len(self.lst):
            raise StopIteration()

        x = self.lst[self.index]
        self.index =self.index+1
        return xclass CapitalIterable():
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        return CapitalIterator(self.lst)

class CapitalIterator():
    def __init__(self, lst):
        self.lst = lst
        self.index = 0

    def __iter__(self):
        return self
        
    def __next__(self):
        if self.index == len(self.lst):
            raise StopIteration()

        x = self.lst[self.index]
        self.index =self.index+1
        return xclass CapitalIterable():
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        return CapitalIterator(self.lst)

class CapitalIterator():
    def __init__(self, lst):
        self.lst = lst
        self.index = 0

    def __iter__(self):
        return self
        
    def __next__(self):
        if self.index == len(self.lst):
            raise StopIteration()

        x = self.lst[self.index]
        self.index =self.index+1
        return xclass CapitalIterable():
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        return CapitalIterator(self.lst)

class CapitalIterator():
    def __init__(self, lst):
        self.lst = lst
        self.index = 0

    def __iter__(self):
        return self
        
    def __next__(self):
        if self.index == len(self.lst):
            raise StopIteration()

        x = self.lst[self.index]
        self.index =self.index+1
        return x
        
class login:
    def login():
        c=0
        c1=0
        with open("customer.json","r") as fh:
            data=json.load(fh)
        n=input("Enter USERNAME: \n")
        i1=CapitalIterable(list(data.keys()))
        iter1=iter(i1)
        while True:
            try:
                if n==next(iter1):
                    print("VALID USERNAME !\n")
                    c=1
                    break
            except StopIteration:
                print("Enter VALID Username\n")
                break
            
        p=input("Enter password : \n")
        i2=CapitalIterable(list(data.values()))
        iter2=iter(i2)
        while True:
            try:
                if p==next(iter2):
                    print("VALID PASSWORD !\n")
                    c1=1
                    break
            except StopIteration:
                print("Enter VALID Password\n")
                break
        if c and c1:
            return n
        
    def password(self):
        PASSWORD = input("ENTER YOUR PASSWORD : ")
        x = re.search("[a-zA-Z]", PASSWORD)
        y = re.findall("[0-9]", PASSWORD)
        z = re.findall("[@#!*&^%$]", PASSWORD)
        if x and y and z:
            print("VALID PASSWORD")
        else:
            print("INVALID INPUT, PASSWORS MUST CONTAIN ANY OF THE ALPHABETS AND NUMBERS AND @ or # SYMBOL")
            quit()
        
n=login.login()
print(n)  #Username          

class Vendor:
   
    def append(z):
        with open("product.json","r") as fh:
            d=json.load(fh)
        k=list(d.keys())
        if z.upper() in k:
            print("Vegetable already exists!")
        else:
            q=int(input("Enter the quantity: "))
            w=int(input("Enter the price/kg: "))
            d[z.upper()]=[q,w]
            with open("product.json","w") as f1:
               json.dump(d,f1)
            print("Sucessfully appended !")
            
    def remove(z):
        with open("product.json","r") as fh:
            d=json.load(fh)
        k=list(d.keys())
        if z.upper() in k:
           d.remove(z)
           print("Product removed !")
        else:
            print("Product not available !")
        
class VegetableFactory:
    def choice(id):
        if id=="vendor":
            return Vendor()
        if id=="customer":
            return Customer()  
            
Vendor.append("Carrot")
Vendor.append("SPInach")
        



