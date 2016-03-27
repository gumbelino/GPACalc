class GPACalc:
    def gradeToGPA(self, grade):
        if grade == 'A+': return 4.0
        elif grade == 'A': return 4.0
        elif grade == 'A-': return 3.7
        elif grade == 'B+': return 3.3
        elif grade == 'B': return 3.0
        elif grade == 'B-': return 2.7
        elif grade == 'C+': return 2.3
        elif grade == 'C': return 2.0
        elif grade == 'C-': return 1.7
        elif grade == 'D': return 1.0
        else: return 0
