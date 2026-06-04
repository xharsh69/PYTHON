class employe():
    salary = 1000000

    def __init__(self, name , salary, language):
        self.name = name
        self.salary =salary
        self.languge = language
        print("i am creating a object:")


harsh = employe("harsh",150000,"python")
print(harsh.name,harsh.salary,harsh.languge)        

rohan = employe("rohan",120000,"javascript")
print(rohan.name,rohan.salary,rohan.languge)        