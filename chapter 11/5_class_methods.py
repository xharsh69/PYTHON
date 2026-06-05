class student():
    s=45

    @classmethod
    def show(cls):
        print(f"number of student: {cls.s}")


st= student()
st.s=99
st.show()