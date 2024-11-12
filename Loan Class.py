from abc import abstractmethod

class Loan:
    
    @abstractmethod
    def e_amt(self,a_balance,l_type):
        ...
class SBAC(Loan):

    def e_amt(self,a_balance,l_type):
        if l_type == 1:
         ty = int(input("Enter your type (1 for Rural/2 for Urban) :"))
         try:
            if isinstance(a_balance,int):
                try:
                    if isinstance(ty,int):
                        try:
                            if ty == 1:
                                if a_balance>= 2000:
                                        print('\033[4m'+'\033[1m'+'5 percent interest'+'\033[0m'+'\033[0m')
                                else:
                                    print(' not eligible for rural home loan due to low bank balance'+'\n'+ ' Expected to have at least 2000')
                            elif ty == 2:
                                if a_balance>=5000:
                                        print('\033[4m'+'\033[1m'+'10 percent interest'+'\033[0m'+'\033[0m')
                                else:
                                    print(' Not eligible for urban home loan due to low bank balance'+'\n'+ ' Expected to have atleast 5000')
                        except:
                            raise TypeError(" Only rural and urban loan available ")
                except:
                    raise TypeError(" only integers can be passed as type eg: 1,2... ")
         except:
            raise TypeError(" only integer can be passed as bank balance  ")
        

        elif l_type == 2:
         try:
            if isinstance(a_balance,int):
                if a_balance>=1000:
                    print('\033[4m'+'\033[1m'+'2 percent interest'+'\033[0m'+'\033[0m')
                else:
                    print(' Not eligible for educational loan')
         except:
            raise TypeError(" only integer can be passed as bank balance  ")

class CAC(Loan):

    def e_amt(self,a_balance,l_type):
        if l_type == 1:
         ty = int(input(" Enter your age: "))
         try:
            if isinstance(a_balance,int):
                try:
                    if isinstance(ty,int):
                        try:
                            if ty >=50:
                                if a_balance> 1000:
                                        print('\033[4m'+'\033[1m'+'7 percent interest'+'\033[0m'+'\033[0m')
                            elif ty<50 and ty >0:
                                if a_balance>2000:
                                        print('\033[4m'+'\033[1m'+'5 percent interest'+'\033[0m'+'\033[0m')
                        except:
                            raise TypeError(" Given age is not valid")
                except:
                    raise TypeError(" only string can be passed as type of home loan  ")
         except:
            raise TypeError(" only integer can be passed as bank balance  ")


#driver code
print('\n'+'\033[4m' + 'Loan available: ' + '\033[0m','\n')
print('1.SBAC:')
print('1)Home loan'.center(20))
print('2)Educational loan'.center(25))
print('2.CAC:')
print('1)Personal loan'.center(24)+'\n')

ans = 'y'
while ans == 'y':
    print(" Enter 1 for home loan , 2 for Educational Loan and 3 for personal loan ")
    try:
        a = int(input(" Enter your choice: "))
        try:  
            b = int(input(" Enter your bank balance:  "))
            print("\n")
            if a ==1:
                print('ELIGIBILTY CRITERIA :'+'\n'+'BANK BALANCE ABOVE 1999 FOR RURAL = 5 PERCENT'+'\n'+'ABOVE 4999 FOR URBAN = 5 PERCENT'+'\n')
                cl=SBAC()
                cl.e_amt(b,1)
            elif a==2:
                print('ELIGIBILTY CRITERIA :'+'\r'+'BANK BALANCE ABOVE 999 = 2 PERCENT'+'\n')

                cl=SBAC()
                cl.e_amt(b,2)
            elif a==3:
                print('ELIGIBILTY CRITERIA :'+'\r'+'AGE ABOVE OR EQUAL TO 50 = 7 PERCENT'+'\r'+'LESS THAN 50 = 5 PERCENT'+'\n')

                cl =CAC()
                cl.e_amt(b,1)

        except:
            raise TypeError('Only integers can be given as bank balance eg:1000,2000...')
    except:
        raise TypeError('Only integers can be given as choice eg:1,2...')
    ans = input('\n'+'Do you want to continue (y/n): ')