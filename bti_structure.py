from abc import ABC , abstractmethod

class Org(ABC):
    
    @abstractmethod
    def add(self, obj):
        ...

    @abstractmethod
    def remove(self, identifier):
        ...
    
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
    def __init__(self , name = "BMW Techworks India"):
        self.name = name
        self.__hubs = {}

    def add(self , hub):
        self.__hubs[hub.hub_name] = hub
        return hub

    def remove(self , hub_name):
        self.__hubs.pop(hub_name , None)

    # def headcount(self):
    #     return sum(hub.headcount() for hub in self.__hubs.values())

class Hub(Org):
    def __init__(self, hub_name:str):
        self.hub_name = hub_name
        self.__clusters = {}

    def add(self, cluster):
        self.__clusters[cluster.cluster_name] = cluster
        return cluster

    def remove(self ,cluster_name):
        self.__clusters.pop(cluster_name , None)

    # def headcounts(self):
    #     return sum(cluster.headcounts() for cluster in self.__clusters.values())

class Cluster(Org):
    def __init__(self , cluster_name:str):
        self.cluster_name = cluster_name
        self.__units ={}

    def add(self , unit):
        self.__units[unit.unit_name] = unit
        return unit

    def remove(self, unit_name):
        self.__units.pop(unit_name , None)

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

    def remove(self , emp_id):
        self.__employees = [e for e in self.__employees if e.emp_id != emp_id]

    # def headcounts(self):
    #     return len(self.__employees)


#add employee
bti = BTI()
# emp = Employee(1 , "Revati", "intern")
# driving_ecu.add(emp)
# print(emp in driving_ecu._Unit__employees)


#add hub
pune = bti.add(Hub("Pune"))
chennai = bti.add(Hub("Chennai"))
banglore = bti.add(Hub("Banglore"))
# print("Banglore" in bti._BTI__hubs)

#add clusters
digital_car = pune.add(Cluster("Digital Car"))
digital_company = pune.add(Cluster("Digital Company"))
digital_product_engineering = pune.add(Cluster("Digital Product Engineering"))
# print("Digital Product Engineering" in pune._Hub__clusters)

#add units for each cluster

#digital car cluster
driving_ecu = digital_car.add(Unit("Driving ECU Integration" , capacity = 80))
connected_vehicles = digital_car.add(Unit("Connected Vehicles" , capacity = 50))
sw_factory = digital_car.add(Unit("SW Factory", capacity = 50))
# print("SW Factory" in digital_car._Cluster__units)

#digital company cluster
cae_simulation = digital_company.add((Unit("CAE Simulation & Function" , capacity = 50)))
geometry_component = digital_company.add((Unit("Geometry , Component & CAD")))
method_tool_product = digital_company.add((Unit("Method , Tools and Product Data")))
# print("Method , Tools and Product Data" in digital_company._Cluster__units)

#digital product engineering cluster
special_skills = digital_product_engineering.add(Unit("Special Skills"))
print("Special Skills" in digital_product_engineering._Cluster__units)

#remove

#removing employee
bti = BTI()
pune = bti.add(Hub("Pune"))
digital_car = pune.add(Cluster("Digital Car"))
driving_ecu = digital_car.add(Unit("Driving ECU Integration" , capacity = 80))
emp = Employee(1 , "Revati", "intern")
driving_ecu.remove(emp)
print(emp in driving_ecu._Unit__employees)

# removing hub 
mumbai = bti.add(Hub("Mumbai"))
bti.remove("Mumbai")
print("Mumbai" in bti._BTI__hubs)

# removing cluster
dummy_cluster = pune.add(Cluster("Test"))
pune.remove("Test")
print("Test" in pune._Hub__clusters)

#removing unit
dummy_unit = digital_car.add(Unit("Test"))
digital_car.remove("Test")
print("Test" in digital_car._Cluster__units)

# print("driving_ecu is:", driving_ecu, "id:", id(driving_ecu))
# print("attributes:", driving_ecu.__dict__)


