class company:
    company_name = "Google"

    @staticmethod
    def gm():
        print("good morning")


class coder(company):
    language = 'python'

class emploey(coder):
    name = "unknown"
    
    def __init__(self , name, salary, age):
        self.name = name
        self.age= age 
        self.salary = salary
    

# h= emploey("harsh raj" ,100000,20)
# print(h.company_name,h.name,h.age,h.salary, h.language)

h= coder()
print(h.company_name,h.language)
        
