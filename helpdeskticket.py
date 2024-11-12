from abc import ABC, abstractmethod

class HelpDeskTicket(ABC):
    faculty={}
    student={}
    def __init__(self,username):
        self.username = username

    @abstractmethod
    def request():
        ...

    @abstractmethod
    def complaint():
        ...
