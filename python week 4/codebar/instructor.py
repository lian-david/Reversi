from member import Member

class Instructor(Member):
    """Represents an instructor
    """
    def __init__(self, full_name, bio):
        super().__init__(full_name)
        self.bio = bio
        skills = []
        self.skills = skills

    def add_skill(self, skill):
        self.skills.append(skill)
