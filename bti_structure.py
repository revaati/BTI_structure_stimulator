from abc import ABC , abstractmethod

class Org(ABC):
    def __init__(self , name , count , budget):
        self.name = name
        self.count = count
        self.budget = budget
        self.parent = list["node"] = None
        self.child = list["none"] = []
    
    @abstractmethod
    def add(self, obj):
        ...

    @abstractmethod
    def remove(self, identifier):
        ...
    
    @abstractmethod
    def headcount(self):
        ...

    # @abstractmethod
    # def kpi(self):
    #     ...

class Employee:
    def __init__(self, emp_id , name , role):
        self.emp_id = emp_id
        self.name = name
        self.role = role

    def show(self):
        return f"{self.name}({self.role})"

class BTI(Org):
    def __init__(self , name = "BMW TEechworks India"):
        self.name = name
        self.__hubs = {}

    def add(self , hub):
        self.__hubs[hub.hub_name] = hub

    def remove(self , hub_name):
        self.__hubs.pop(hub_name , None)

    def headcount(self):
        return sum(hub.headcount() for hub in self.__hubs.values())

