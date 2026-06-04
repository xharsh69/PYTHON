class emploey():
    name = "unknown"
    salary = 100000
    language = "python"
    
    def importent(self):
        print(f"this is the laguage: {self.language} it's your salary: {self.salary}")

    @staticmethod
    def gm():
        print("good morning")





harsh = emploey()
harsh.name= "Harsh Raj Singh"
harsh.salary = 200000
harsh.gm()
print(harsh.name, harsh.language ,harsh.salary)
harsh.importent()