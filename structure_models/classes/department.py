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

    def loadEmployees(self):
        reader = EmployeeReader()
        self.employees = reader.ReadFromFile(employeeFileName, self.code)

    def show_my_employees(self):
        print "I'm the department of %s." % self.name
        print "Here are my employees:"
        for empl in self.employees:
            print "%s\t%s\tof age:%s" %(empl.emp_code, empl.name, empl.age)

class EmployeeReader:
    def ReadFromFile(self, fileName, departmentCode):
        array = []
        f = open(fileName, "r")
        for line in f:
            line = line.replace('\n','')
            code, name, age, dep = line.split(",")
            if departmentCode == dep:
                array.append(Employee(code, name, age, dep))
        f.close()
        return array

class DepartmentReader:
    def ReadFromFile(self, fileName):
        array = []
        f = open(fileName, "r")
        for line in f:
            line = line.replace('\n','')
            code, name = line.split(",")
            array.append(Department(code, name))
        f.close()
        return array


def main():
    departmentReader = DepartmentReader()
    departments = departmentReader.ReadFromFile(departmentFileName)
    
    for dep in departments:
        dep.loadEmployees()

    for dep in departments:
        dep.show_my_employees()

if __name__ == "__main__":
    main()