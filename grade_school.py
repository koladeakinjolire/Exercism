class School:
    def __init__(self):
        self.students = {}
        self.added_status = []

    def add_student(self, name, grade):
        if  not isinstance(name, str) or  not isinstance(grade, int):
            return False
            
        if name not in self.students:
            self.students[name] = grade
            self.added_status.append(True)
            return True
        else:
            self.added_status.append(False)
            return False

    def roster(self):
        return [name for name, _ in sorted(self.students.items(), key=lambda item: (item[1], item[0]))]
        
    def grade(self, grade_number):

        return sorted([name for name, grade in self.students.items() if grade == grade_number])

    def added(self):

        return self.added_status