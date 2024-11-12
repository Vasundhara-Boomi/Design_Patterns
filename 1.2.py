class Library:
    Books = [["DDS" , "ISBN" , "Book Name" , "Subject" , "Author"] , [123 , 123456 , "Discrete Mathematics" , "Mathematics" , "Rajesh"] , [124 , 123457 , "Semiconductors" , "Physics" , "Selvi"] , [125 , 123458 , "DS" , "IT" , "Karthika"]]
    magazine = [["UPC" , "Title" , "Volume" , "Issue Number"] , [1 , "PS" , 5 , 14] , [2 , "HS" , 4 , 18] , [3 , "HP" , 5 , 1]]
    cd = [["UPC" , "Author"] , [1 , "Vasundhara"] , [2 , "Raji"]]
    dvd = [["UPC" , "Author"] , [1 , "Manoj"] , [2 , "Bharath"]]

    def Book_add(self):
        print('\n' , "*" * 55)
        List = [] #temepravary list
        print("\nEnter the details of the book to be added.")
        
        List.append(int(input("Enter the DDS number : ")))
        List.append(int(input("Enter the ISBN number : ")))
        List.append(input("Enter the book name : "))
        List.append(input("Enter the subject of the book : "))
        List.append(input("Enter the subject of the book : "))

        self.Books.append(List) #Adding to the list Book.
        print("The Book is added.")

    def DVD_add(self):
        print('\n' , "*" * 55)
        List = [] #Temperavary List.
        print("\nEnter the details of the DVD to be added.")

        List.append(int(input("Enter the UPC number " )))
        List.append(input("Enter the author name : "))

        self.dvd.append(List) #Adding to the list DVD.
        print("The dvd is added.")

    def Magazine_add(self):
        print('\n' , "*" * 55)
        List =[] #Temperavary List.

        List.append(int(input("\nEnter the UPC number : ")))
        List.append(input("Enter the title : "))
        List.append(int(input("Enter the volume : ")))
        
        self.magazine.append(List) #Adding to the list Magazine.
        print("The magazine is added.")

    def CD_add(self):
        print('\n' , "*" * 55)

        List = [] #Temperavary List.
        print("\nEnter the details of the CD to be added.")

        List.append(int(input("Enter the UPC number " )))
        List.append(input("Enter the author name : "))

        self.cd.append(List) #Adding to the list DVD.
        print("The cd is added.")

    #program for reader.           

    def Book(self):
        print('\n' , "*" * 55)
        print("\nThe Books avaliable in the Library are : ")

        for i in self.Books:
            print(i)

    def DVD(self):
        print('\n' , "*" * 55)
        print("\nThe DVDs avaliable in the Library are : ")

        for i in self.dvd:
            print(i)

    def Magazine(self):
        print('\n' , "*" * 55)
        print("\nThe Magazines avaliable in the Library are : ")

        for i in self.magazine:
            print(i)

    def CD(self):
        print('\n' , "*" * 55)
        print("\nThe CDs avaliable in the Library are : ")

        for i in self.cd:
            print(i)

#Ensure wheather the user is reader or contributor.
print("Select your category.")
a = int(input("\n1.Reader\n2.Constributor\n3.Exit\nEnter as a number : "))
L = Library()

while a > 0 and a < 4:
    #category condition.
    if a == 2:
        #condition for reader.
        #Contributor - Ask their contributing material.
        print('\n' , '*' * 55)
        print("\nWhat are you going to contribute?\n1.Book\n2.DVD\n3.Magazine\n4.CD")
        material = int(input("Enter as number : "))

        #If conditions to find their needs.
        if material == 1:
            L.Book_add()

        elif material == 2:
            L.DVD_add()

        elif material == 3:
            L.Magazine_add()

        elif material == 4:
            L.CD_add()

        else:
            print("Invalid Input!")

    elif a == 1:
        #condition for constributor.
        #Reader - Ask their needs.
        print('\n' , '*' * 55)
        print("\nWhat do you want?\n1.Book\n2.DVD\n3.Magazine\n4.CD")
        material = int(input("Enter as number : "))

        #If conditions to find their needs.
        if material == 1:
            L.Book()

        elif material == 2:
            L.DVD()

        elif material == 3:
            L.Magazine()

        elif material == 4:
            L.CD()

        else:
            print("Invalid Input!")

    elif a == 3:
        break

    print("\nSelect your category.")
    a = int(input("\n1.Reader\n2.Constributor\n3.Exit\nEnter as a number : "))

else:
    print("\nInvalid Input!")

