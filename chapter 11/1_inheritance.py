class company:
    company_name = "Google"

    @staticmethod
    def gm():
        print("good morning")




class emploey(company):
    
    def __init__(self , name, salary, age):
        self.name = name
        self.age= age 
        self.salary = salary
    

h= emploey("harsh raj" ,100000,20)
print(h.company_name,h.name,h.age,h.salary)

        
