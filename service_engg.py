import json
from services import Services
from min_heap import HeapPriorityQueue


class ServiceEngg(Services):

    def assign_request_ticket_to_engineer(self):
        with open("engineer.json", "r+") as f1:
            x = json.load(f1)
        min_heap = HeapPriorityQueue()
        for service_engineer in x:
            if not x[service_engineer]["expertise"]:
                if x[service_engineer]["years_of_experience"] in [1,2]:
___________________min_heap.add(service_engineer,
___________________x[service_engineer]["tickets_assigned"])
        service_engineer_assigned = min_heap.remove_min()
        x[service_engineer_assigned[0]]["tickets_assigned"] += 1
        with open("engineer.json", "w") as f1:
            json.dump(x,f1)
        print(f"Request ticket assigned to service engineer _____________________{service_engineer_assigned[0]}")

    def assign_complain_ticket_to_engineer(self):
        with open("engineer.json", "r+") as f1:
            x = json.load(f1)
        min_heap=HeapPriorityQueue()
        for service_engineer in x:
            if x[service_engineer]["expertise"]:
                if x[service_engineer]["years_of_experience"] > 5:
___________________min_heap.add(service_engineer,
___________________x[service_engineer]["tickets_assigned"])
        service_engineer_assigned = min_heap.remove_min()
        x[service_engineer_assigned[0]]["tickets_assigned"] += 1            
        with open("engineer.json", "w") as f1:
            json.dump(x,f1)
        print(f"Complaint ticket assigned to service engineer ___________________{service_engineer_assigned[0]}")
        
    def print_mro(self):
        print(ServiceEngg.__mro__)
