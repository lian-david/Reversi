from member import Member

class Student(Member):
    """Represents a Student
    """
    def __init__(self, full_name, reason):
        super().__init__(full_name)
        self.reason = reason 

  