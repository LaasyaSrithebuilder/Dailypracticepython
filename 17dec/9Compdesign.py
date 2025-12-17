from abc import ABCMeta, abstractmethod

class IDdept(metaclass=ABCMeta):
    @abstractmethod

    def __init__(self, emp):
        """to implement in derived class"""
        pass
    @abstractmethod
    def display_dept_info(self):
        """to implement in derived class"""
        pass

class AccountDept(IDdept):
    def __init__(self, emp):
        self.emp = emp

    def display_dept_info(self):
        print(f"Employee Name: {self.emp.name}, Age: {self.emp.age}, Department: Accounting")

class DevelopmentDept(IDdept):
    def __init__(self, emp):
        self.emp = emp

    def display_dept_info(self):
        print(f"Employee Name: {self.emp.name}, Age: {self.emp.age}, Department: Development")

class ParentDept(IDdept):
    def __init__(self, emp, dept_type):
        self.emp = emp
        self.base_emp = emp
        self.subdepts = []
    def add(self, dept):
        self.subdepts.append(dept)
        self.emp += dept.emp

    def display_dept_info(self):
        print("Parent Department Info:")
        print(f"parent dept base emp: {self.base_emp}")
        for dept in self.subdepts:
            dept.display_dept_info()
        print(f"Total Employees in Parent Dept: {self.emp}")

dept1 = AccountDept(5)
dept2 = DevelopmentDept(10)
parent_dept = ParentDept(0, "Head Office")
parent_dept.add(dept1)
parent_dept.add(dept2)