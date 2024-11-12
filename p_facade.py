import json
import random
import re
from iterator import CapitalIterable
        
class login:
 
    def login():
        c=0
        c1=0
        with open("customer.json","r") as fh:
            data=json.load(fh)
        n=input("Enter USERNAME: \n")
        if re.search("[a-zA-Z]", n):
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
        if login.password(p):
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
        
    def password(p):
        x = re.search("[a-zA-Z]", p)
        y = re.findall("[0-9]", p)
        z = re.findall("[@#!*&^%$]", p)
        if x and y and z:
            return True
        else:
            print("Doesnt fulfill the conditions of a PASSWORD")

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
           del d[z.upper()]
           print("Product removed !")
        else:
            print("Product not available !") 
            
class customer:
    def __init__(self,cart):
        self.cart=cart

    def Generating_Bill(self,name):
        with open("product.json","r+") as f:
            dic=json.load(f)
        bill=0

        for i in self.cart:
            if i[0] in dic:
                if (dic[i[0]][1]-i[1])>0:
                    print(dic[i[0]][1])
                    dic[i[0]][0]=dic[i[0]][0]-i[1]
                    bill=bill+(i[1])*dic[i[0]][1]

        with open("product.json","w") as f:
            json.dump(dic,f)

        if bill>100:
            print("Hello...",name)
            print("The Order has been placed for the respective list of products...")
            print("The total amount is: ",bill)

        else:
            raise ValueError("The order cannot be delivered to Home due to less amount of bill...")
        
        
class Properties:
    def __init__(self,l):
        self.login=login()
        self.customer=customer(l)
        self.vendor=Vendor()
        
    def customer_s(self):
        n=self.login.login()
        with open("product.json","r") as f:
            l=json.load(f)
            print(l)
        ilop=eval(input("Enter nested list of products and quantity: "))
        po=customer(ilop)
        po.Generating_Bill(n)
        
    def vendor_s(self):
        while True:
           print("Options are: 1. Add Product 2. Delete Product 3. display products")
           ch=int(input("Enter Choice: "))
           if ch==1:
               pn=input("Enter Prodduct name: ")
               self.vendor.append(pn)
           elif ch==2:
               pn=input("Enter Product name: ")
               self.vendor.remove(pn)
           elif ch==3:
               with open("product.json","r") as f:
                   l=json.load(f)
                   print(l)
           else:
               break
        
        

uc=input("Enter Choice as vendor or customer: ")
if uc=="vendor":
    p=Properties(list())
    p.vendor_s()
 
        
if uc=="customer":
    
    p=Properties(list())
    p.customer_s()
    

