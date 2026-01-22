from abc import ABC , abstractmethod

class Org(ABC):
    
    @abstractmethod
    def add(self, obj):
        ...

    # @abstractmethod
    # def remove(self, identifier):
    #     ...
    
    # @abstractmethod
    # def headcount(self):
    #     ...

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
        return hub

    # def remove(self , hub_name):
    #     self.__hubs.pop(hub_name , None)

    # def headcount(self):
    #     return sum(hub.headcount() for hub in self.__hubs.values())

class Hub(Org):
    def __init__(self, hub_name:str):
        self.hub_name = hub_name
        self.__clusters = {}

    def add(self, cluster):
        self.__clusters[cluster.cluster_name] = cluster
        return cluster

    # def remove(self ,cluster_name):
    #     self.__clusters.pop(cluster_name , None)

    # def headcounts(self):
    #     return sum(cluster.headcounts() for cluster in self.__clusters.values())

class Cluster(Org):
    def __init__(self , cluster_name:str):
        self.cluster_name = cluster_name
        self.__units ={}

    def add(self , unit):
        self.__units[unit.unit_name] = unit
        return unit

    # def remove(self, unit_name):
    #     self.__units.pop(unit_name , None)

    # def headcounts(self):
    #     return sum(unit.headcounts() for unit in self.__units.values())

class Unit(Org):
    def __init__(self , unit_name:str , capacity= 40):
        self.unit_name = unit_name
        self.__employees= []
        self.__capacity = capacity

    def add(self, employee):
        self.__employees.append(employee)
        return employee

    # def remove(self , emp_id):
    #     self.

    # def headcounts(self):
    #     return len(self.__employees)

bti = BTI()
pune = bti.add(Hub("Pune"))
digital_car = pune.add(Cluster("Digital Car"))
driving_ecu = digital_car.add(Unit("Driving ECU Integration" , capacity = 80))
emp = Employee(1 , "Revati", "intern")
driving_ecu.add(emp)
print(emp in driving_ecu._Unit__employees)


# print("driving_ecu is:", driving_ecu, "id:", id(driving_ecu))
# print("attributes:", driving_ecu.__dict__)


