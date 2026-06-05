class Employee:
    salary = 10000
    inc = 20

    @property
    def s_A_i(self):
        return self.salary + self.salary * (self.inc / 100)

    @s_A_i.setter
    def s_A_i(self, value):
        self.inc = ((value / self.salary) - 1) * 100


s = Employee()

print(s.s_A_i)      # 12000.0

s.s_A_i = 15000     # Set salary after increment

print(s.inc)        # 50.0
print(s.s_A_i)      # 15000.0