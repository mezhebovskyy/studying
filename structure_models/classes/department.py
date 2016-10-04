departmentFileName = "department_info.csv"
employeeFileName = "employee_info.csv"

class Employee:
    def __init__(self, emp_code, name, age, dep_code):
        self.emp_code = emp_code
        self.name = name
        self.age = age
        self.dep_code = dep_code

class Department:
    def __init__(self, code, name):
        self.code = code
        self.name = name
        self.employees = []

    def fill_employees(self, all_employees):
        for employee in all_employees:
            if employee.dep_code == self.code:
                self.employees.append(employee)
    def show_my_employees(self):
        print "I'm the department of %s." % self.name
        print "Here are my employees:"
        for empl in self.employees:
            print "%s\t%s\tof age:%s" %(empl.emp_code, empl.name, empl.age)

class EmployeeReader:
    def __init__(self, filename):
        self.filename = filename
        self.employees = []
        
    def ReadFromFile(self):
        p = open(self.filename, "r")
        for line in p:
            line = line.replace('\n','')
            code, name, age, dep = line.split(",")
            self.employees.append(Employee(code, name, age, dep))
        p.close()
        return self.employees

class DepartmentReader:
    def __init__(self, filename):
        self.filename = filename
        self.departments = []
        
    def ReadFromFile(self):
        d = open(self.filename, "r")
        for line in d:
            line = line.replace('\n','')
            code, name = line.split(",")
            self.departments.append(Department(code, name))
        d.close()
        return self.departments


def main():
    #Create readers
    employeeReader = EmployeeReader(employeeFileName)
    departmentReader = DepartmentReader(departmentFileName)
    #read data
    employees = employeeReader.ReadFromFile()
    departments = departmentReader.ReadFromFile()
    #Define the connection 
    for dep in departments:
        dep.fill_employees(employees)
        dep.show_my_employees()

if __name__ == "__main__":
    main()