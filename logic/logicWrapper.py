"""
fix to camelCase not python_case
"""

from logic.employeeHandler import EmployeeHandler
from baseClasses.Employee import Employee
from logic.PropertyHandler import PropertyHandler
from baseClasses.Property import Property

class Logic_Wrapper:
    def __init__(self) -> None:
        self.employee_handler = EmployeeHandler()
        self.Property_handler = PropertyHandler()

    def addEmployee(self, employee: Employee) -> bool:
        return self.employee_handler.addEmployee(employee)
    
    def editEmployee(self, target_kennitala: str, **kwargs) -> bool:
        return self.employee_handler.editEmployee(target_kennitala, **kwargs)
    
    def listEmployees(self, **kwargs) -> list['Employee']:
        return self.employee_handler.listEmployes(**kwargs)

    def addProperty(self, property: Property) -> bool:
        return self.Property_handler.addProperty(property)
    
    def listProperties(self, **kwargs) -> list['Property']:
        return self.Property_handler.listProperties(**kwargs)
