class employee :
    def __init__(self,empId,empName,empPost,empSalary):
        self.empid = empId
        self.empName = empName
        self.empPost = empPost
        self.empSalary = empSalary
    def printObject(self):
        print("I am Employee Number",self.empid)
        print("I am",self.empName)
        print("My Post is ",self.empPost)
        print("I earn",self.empSalary,"monthly")
    

Daksh = employee(1420,"Daksh Singh","Manager",20000)
Vedanta = employee(1203,"Vedanta Sharma","asstaint",10000)

Daksh.printObject()
Vedanta.printObject()
        