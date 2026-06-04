import random

class train():
    def __init__(self,train_no,fromm,to):
        self.train_no = train_no
        self.fromm= fromm
        self.to= to

    def book(self):
        print(f"your train_no: {self.train_no} from {self.fromm} to {self.to}")

    def status(self):
        print(f"your runing on time:")

    def fear(self):
        print(f"ticket fear in train_no: {self.train_no} from {self.fromm} to {self.to} is {random.randint(222,999)}")

        
harsh = train(18101,"delhi", "jaipur")
harsh.book()
harsh.status()
harsh.fear()