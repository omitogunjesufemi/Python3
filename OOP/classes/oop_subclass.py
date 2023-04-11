class SchoolMember:
    """Represents any school member."""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Initialised SchoolMember: {}".format(self.name))

    def tell(self):
        """Telll my details"""
        print('Name: "{}" Age: "{}"'.format(self.name, self.age))


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print("Salary: {:d}".format(self.salary))


class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print("Marks: {:d}".format(self.marks))


t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

print()
members = [t, s]
for member in members:
    member.tell()
