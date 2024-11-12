from abc import ABC, abstractmethod #Importing the ABC module from the abc package.

class Loan(ABC):
    #Loan is an abstract class.

    @abstractmethod #Decouration Keyword to represent abstract method.
    def Education_Loan(self):
        ...

    @abstractmethod
    def Home_Loan(self):
        ...

    @abstractmethod
    def Personal_Loan(self):
        ...

class Bank(Loan):
    #Bank class inherits the Loan class, which is an abstract class.

    def __init__(self , account : str) -> None:
        self._account = account #Contains the type of account the user contain.
        print("\n" , "*" * 110)

        if self._account.lower() == 'savings':
            print("\nThe avaliable loans are,\n1.Education Loan\n2.Home Loan\n3.Exit")
            loan_choice = int(input("\nEnter your choice (Integer) : "))

            #Conditions to call the functions.
            if loan_choice == 1:
                #Calls the function Education Loan.
                self.Education_Loan()

            elif loan_choice == 2:
                #Calls the function Home Loan.
                self.Home_Loan()

            elif loan_choice == 3:
                #Truncates the program.
                print("\nSorry, We don't have what you need :).")

            else:
                print("!!!Invalid Input!!!")

        elif self._account.lower() == 'current':
            print("\nThe only loan avaliable is Personal Loan.")
            loan_choice = input("Do you want Personal Loan (Yes/No) : ")

            #Conditions to call the Personal loan function.

            if loan_choice.lower() == 'yes':
                #Calls the function Personal Loan function.
                self.Personal_Loan()

            elif loan_choice.lower() == 'no':
                #Truncates the program.
                print("\nSorry we don't have what you need :).")

            else:
                print("!!!Invalid Input!!!")

    def Education_Loan(self) -> None:
        #Function to check the conditions for providing Education loan.
        print("\n" , "*" * 110)
        print("\n5'%' interest is alloted for Education loan.")
        okay = input("Do you want Education Loan (Yes/No) : ") #Getting users wish.

        if okay.lower() == 'yes':
            print("\n" , '-' * 110)
            print("\nEnter the following details.")

            tenth = input("\nDid you pass 10th (Yes/No) : ")
            twelth = input("Did you pass twelth (Yes/No) : ")

            if tenth.lower() == 'no' and twelth.lower() == 'yes':
                print("\nThe input provided is invalid !!!")

            elif tenth.lower() == 'yes' and twelth.lower() == 'no':
                print("\nThe loan amount will be provided upto 400k only.")

                #Getting the amount.
                amount = int(input("Enter the Amount you need (Integer) : "))

                #Condition to check the amount range.
                if amount >= 100000 and amount <= 400000:
                    interest = self.loan(amount , 0.05)
                    print("\nYou will be paying an amount Rs." , interest , "/- every year.")

                elif type(amount) is int:
                    print("\nSorry Loan cannot be provided for the amount you entered !!!")

                else:
                    print("\n!!!Invalid Input!!!")

            elif tenth.lower() == 'yes' and twelth.lower() == 'yes':
                print("\nThe loan amount will be provided upto 800k only.")

                #Getting the amount.
                amount = int(input("Enter the Amount you need (Integer) : "))

                #Condition to check the amount range.
                if amount >= 100000 and amount <= 800000:
                    interest = self.loan(amount , 0.05)
                    print("\nYou will be paying an amount of Rs." , interest , "/- every year.")

                elif type(amount) is int:
                    print("\nSorry Loan cannot be provided for the amount you entered !!!")

                else:
                    print("\n!!!Invalid Input!!!")

            elif tenth.lower() == 'no' and twelth.lower() == 'no':
                print("\nSorry for you  the loan cannot be provided :).")

            else:
                print("\n!!!Invalid Input!!!")

    def Home_Loan(self) -> None:
        #Concrete function for home loan.
        print('\n' , '*' * 110)
        print("\nEnter the following details.")

        location = input("Enter your location (Rural/Urban) : ")

        #Conditions based on location.
        if location.lower() == 'rural':
            print("\n15'%' of interest is provided for Home loan for rural areas.")
            okay = input("Do you want loan? (Yes/No) : ")

            if okay.lower() == 'yes':
                print("\nLoan amount will be provided upto 6 Million.")
                amount = int(input("Enter the loan amount you needed (Integer) : "))

                #Condition for entered amount.
                if amount >= 3000000 and amount <= 6000000:
                    interest = self.loan(amount , 0.15) #Calling the function loan.
                    print("\nYou will be paying an amount of Rs." , interest , "/- every year.")

                elif type(amount) is int:
                    print("\nLoan cannot be provided for the amount you entered :).")

                else:
                    print("\n!!!Invalid Input!!!")

            elif okay.lower() == 'no':
                pass

            else:
                print("\n!!!Invalid choice!!!")

        elif location.lower() == 'urban':
            print("\n20'%' of interest is provided for Home loan for Urban areas.")
            okay = input("Do you want loan? (Yes/No) : ")

            if okay.lower() == 'yes':
                print("\nLoan amount will be provided upto 15 Million.")
                amount = int(input("Enter the loan amount you needed (Integer) : "))

                #Condition for entered amount.
                if amount >= 6000000 and amount <= 15000000:
                    interest = self.loan(amount , 0.15) #Calling the function loan.
                    print("\nYou will be paying an amount of Rs." , interest , "/- every year.")

                elif type(amount) is int:
                    print("\nLoan cannot be provided for the amount you entered :).")

                else:
                    print("\n!!!Invalid Input!!!")

            elif okay.lower() == 'no':
                pass

            else:
                print("\n!!!Invalid choice!!!")

        else:
            print("\n!!!Invalid input!!!")

    def Personal_Loan(self) -> None:
        #Concrete class for providing personal loan.
        print("\n" , "*" * 110)
        print("\nEnter the following details,")

        age = int(input("\nEnter your age : "))

        if age >= 50 and age <= 80:
            print("\n3'%' of interest is provided for Personal Loan.")
            okay = input("Do you want loan? (Yes/No) : ")

            if okay.lower() == 'yes':
                print("\nLoan amount will be provided upto 200K.")
                amount = int(input("Enter the loan amount you needed (Integer) : "))

                #Condition for entered amount.
                if amount >= 50000 and amount <= 200000:
                    interest = self.loan(amount , 0.03) #Calling the function loan.
                    print("\nYou will be paying an amount of Rs." , interest , "/- every year.")

                elif type(amount) is int:
                    print("\nLoan cannot be provided for the amount you entered :).")

                else:
                    print("\n!!!Invalid Input!!!")

            elif okay.lower() == 'no':
                pass

            else:
                print("\n!!!Invalid choice!!!")

        elif age >= 25 and age < 50:
            print("\n7'%' of interest is provided for Personal Loan.")
            okay = input("Do you want loan? (Yes/No) : ")

            if okay.lower() == 'yes':
                print("\nLoan amount will be provided upto 500K.")
                amount = int(input("Enter the loan amount you needed (Integer) : "))

                #Condition for entered amount.
                if amount >= 200000 and amount <= 500000:
                    interest = self.loan(amount , 0.07) #Calling the function loan.
                    print("\nYou will be paying an amount of Rs." , interest , "/- every year.")

                elif type(amount) is int:
                    print("\nLoan cannot be provided for the amount you entered :).")

                else:
                    print("\n!!!Invalid Input!!!")

            elif okay.lower() == 'no':
                pass

            else:
                print("\n!!!Invalid choice!!!")

        else:
            print("\nSorry Loan cannot be provided for you :).")

    def loan(self , amount : int , percentage : float) -> float :
        #Returns the interest amount.
        interest = amount * percentage
        return interest

#Main function getting the user input.
account = input("\nEnter your bank account type (Savings/Current) : ")

#Creating the object for the class Bank.
B = Bank(account)
