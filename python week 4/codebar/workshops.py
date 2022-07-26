from student import Student
from instructor import Instructor

class Workshop:
    """Represents a workshop
    """
    def __init__(self, date, subject):
        self.date = date
        self.subject = subject
        self.instructors = []
        self.students = []
        

    def add_participants(self, member):
        if isinstance(member, Instructor):
            self.instructors.append(member)
        elif isinstance(member, Student):
            self.students.append(member)

    def print_details(self):
        print(f'Date: {self.date}')
        print(f'Subject: {self.subject}')
        print("\nInstructors:")
        for instructor in self.instructors:
            print(f'{instructor.full_name}\n\t{instructor.bio}')
            print(f'\tSkills: {", ".join(instructor.skills)}')

        print("\nStudents:")
        for student in self.students:
            print(f'{student.full_name}\n\t{student.reason}')

