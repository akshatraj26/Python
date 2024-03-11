class Department:
    def set_department(self):
        self.__id = input("Enter department id: ")
        self.__name = input("Enter the department name:")
        
    def display_department(self):
        print("Department Id is:", self.__id)
        print("Department Name is:", self.__name)
        
class Employee:
    def set_employee(self):
        self.__eid = input("Enter employee id:")
        self.__ename = input("Enter employee name:")
        self.__dobj = Department()
        self.__dobj.set_department()
        
    def display_employee(self):
        print("Employee Id:", self.__eid)
        print("Employee Name:", self.__ename)
        self.__dobj.display_department()
        
obj = Employee()
obj.set_employee()
obj.display_employee()