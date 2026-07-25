class Employee :
     def __init__(self,name , department , salary):
          self.name = name 
          self.department = department 
          self.salary = salary 

     def display(self):
          print("Name:", self.name)
          print("Department:",self.department)
          print("Salary:", self.salary)

     def increase_salary( self ,amount) :
          if amount > 0 :
               self.salary += amount 
               print("Salary increased successfully")
               print(self.salary)

     def decrease_salary(self , amount) :
          if amount < self.salary and amount > 0 :
               self.salary -= amount 
               print("Salary decrease successfully")
               print(self.salary)
          else :
               print("Invalid amount") 

     def annual_salary(self):
          anuual = self.salary * 12 
          print("Annual salary :", anuual)


E1 = Employee("Bharath","AIML",20000)
E1.display()
E1.increase_salary(5000)
E1.decrease_salary(100)
E1.display()
E1.annual_salary()
        
