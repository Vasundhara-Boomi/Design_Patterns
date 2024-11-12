from helpdeskticket import HelpDeskTicket   
from service_engg import ServiceEngg
class Student(HelpDeskTicket):

    def __init__(self,username, name, phone_no, block_no, dept):
        super().__init__(username)  
        self.name = name 
        self.phone_no = phone_no
        self.block_no = block_no
        self.dept = dept
        self.unique_ticket_id = self.generate_unique_id()
        self.details = {"name": "", "phone_number":0, "block_no":0, "dept":""}

    def request(self):
        self.details["name"] = self.name
        self.details["phone_number"] = self.phone_no
        self.details["block_no"] = self.block_no
        self.details["dept"] = self.dept
        HelpDeskTicket.student[self.unique_ticket_id]=self.details
        print("Request submitted successful")
        service_engg = ServiceEngg()
        service_engg.assign_request_ticket_to_engineer()

    def complaint(self):
        ch = input("Enter the detail to be changed name/ phone/ block/ dept")
        if ch.lower() == "name":
            name = input("Enter name: ")
            self.details["name"] = name
        elif ch.lower() == "phone":
            phone = int(input("Enter phone number: "))
            self.details["phone_number"] = phone
        elif ch.lower() == "block":
            block = int(input("Enter block number: "))
            self.details["block_no"] = block
        elif ch.lower() == "dept":
            dept = input("Enter department: ")
            self.details["dept"] = dept
        HelpDeskTicket.student[self.unique_ticket_id] = self.details
        print("Complaint submitted successful")
        service_engg = ServiceEngg()
        service_engg.assign_complain_ticket_to_engineer()
        
    def generate_unique_id(self):
            self.unique_ticket_id = f"{self.username[:4]}2023"
            print(f"This is your unique ticket number{self.unique_ticket_id}")
