# BTI_structure_stimulator

Creating a structure of BTI using OOPS concepts.

Base Class - BTI        variable -  name ,salary , experience , joining date , unit, email , 
                        method - add_new_emp , remove_emp ,total_emp_count
Derived Class - Pune Hub var
                        method - add_new_cluster
derived class(Pune Hub) - digital car , digital company , digital product engineering
method - add_new_unit
derived class(digital car) - connected vehicles , driving ecu integration , SW factory      


BTI(Name , Email, Cluster , Unit , Joining_date , Salary) (Add_emp , Remove_emp , Emp_count)
Hub(add_hub , add_unit , remove_unit)
    Pune_Hub
    cluster
        Digital_car
        unit
            Connected_vehicles
            Driving_ECU_integration
            SW_factory
        Digital_company
        unit
            CAE_Simulation_Fucntion
            Geometry_Component_CAD
            Method_Tool_ProductData
        Digital_product_engineering
        unit
            SpecialSkills
    Banglore_Hub
    Chennai_Hub



Instead of creating base class for each stage we will create an abstract class for it and these classes will be concrete subclasses.

org is abstract class
I need add method, remove method 
we can add and delete emp , cluster , hub , unit
so methods will be add() , delete() , count() , set_kpi() , show_kpi()
var = name 


employee - id , name , email , date ,(methods - )

hub = name , cluster , count, budget

unit = name , team , count , budget , 


