class StudentMarksManagement:
    def __init__(self):
        self.students = []

    def add_student(self, name, marks):
        self.students.append({'name': name, 'marks': marks})

    def calculate_average(self):
        if not self.students:
            return 0
        total_marks = sum(student['marks'] for student in self.students)
        return total_marks / len(self.students)

    def find_highest_scorer(self):
        if not self.students:
            return None
        return max(self.students, key=lambda student: student['marks'])

    def find_lowest_scorer(self):
        if not self.students:
            return None
        return min(self.students, key=lambda student: student['marks'])

if __name__ == '__main__':
    management = StudentMarksManagement()
    management.add_student('Alice', 85)
    management.add_student('Bob', 92)
    management.add_student('Charlie', 78)

    print(f'Average Marks: {management.calculate_average()}')
    print(f'Highest Scorer: {management.find_highest_scorer()}')
    print(f'Lowest Scorer: {management.find_lowest_scorer()}')
