class company:
    company_name = "Google"
    def __init__(self):
        print("this is my company")

    @staticmethod
    def gm():
        print("good morning")


class coder(company):
    language = 'python'

    def __init__(self):
        super().__init__()
        print("it's my code class")

class emploey(coder):
    name = "unknown"

   
    
    def __init__(self , name, salary, age):
        super().__init__()
        self.name = name
        self.age= age 
        self.salary = salary
    

h1= emploey("harsh",100000,20)
print(h1.name,h1.salary,h1.age)

