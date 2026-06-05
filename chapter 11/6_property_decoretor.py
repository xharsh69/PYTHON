class student():
    s=45

    @classmethod
    def show(cls):
        print(f"number of student: {cls.s}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self,value):
        self.fname= value.split(" ")[0]
        self.lname= value.split(" ")[1]



st= student()
# st.s=99
st.name= "harsh raj"
print(st.fname)
st.show()