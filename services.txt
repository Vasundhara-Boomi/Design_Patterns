from abc import ABC, abstractmethod

class Services(ABC):

    @abstractmethod
    def assign_complain_ticket_to_engineer():
        ...

    @abstractmethod
    def assign_request_ticket_to_engineer():
        ...
