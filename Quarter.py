import LinkedList
import GPACalc

class quarter:

    calc = GPACalc.GPACalc()

    def __init__(self, term, year):
        self._term = term
        self._year = year
        # each quarter has own list of courses
        self.courses = LinkedList.myLL()
        self.units = 0
        self.GTU = 0
        self.GPA = 0
        self.DefUnits = 0
    def defUnits(self):
        units = 0
        for i in range (0, self.courses.size()):
            course = self.courses.get(i)
            grade = course.getGrade()
            if grade is not None and grade != 'P' and grade != 'NP':
                units += course.getUnits()
        return units
    def getUnits(self):
        return self.units
    def getGTU(self):
        return self.GTU
    def getGPA(self):
        return round(self.GPA,3)
    def getName(self):
        return self._term + " " + self._year
    def removeCourse(self, index):
        course = self.courses.removeIndex(index)
        if course is not None:
            self.units -= course.getUnits()
        return course
    def getYear(self):
        return self._year
    def getTermIndex(self):
        if self._term == "WINTER":
            return 1
        elif self._term == "SPRING":
            return 2
        elif self._term == "SUMMER":
            return 3
        else:
            return 4
    def isDefined(self):
        for i in range(0, self.courses.size()):
            course = self.courses.get(i)
            if course.getGrade() is None:
                return False
        return True
    def addCourse(self, course):
        index = 0
        if self.courses.size() > 0:
           curr = self.courses.get(index)
           while course > curr:
               index += 1
               if index == self.courses.size():
                   break
               curr = self.courses.get(index)
        self.courses.addIndex(course,index)
        self.units += course.getUnits()
        self.GTU += course.getGTU()
        if self.defUnits() > 0:
            self.GPA = self.GTU/self.defUnits()
    def getCourse(self, index):
        if index > self.courses.size():
            return
        course = self.courses.get(index)
        return course
    def printWithIndexes(self):
        print(self.courses.printWithIndex())
    def changeGrade(self,index,grade):
        if index > self.courses.size():
            return
        course = self.courses.get(index)
        course.setGrade(grade)
        self.updateGPA()
    def updateGPA(self):
        self.GTU = 0
        for i in range(0, self.courses.size()):
            course = self.courses.get(i)
            self.GTU += course.getGTU()
        if self.defUnits() > 0:
            self.GPA = self.GTU/self.defUnits()
    def size(self):
        return self.courses.size()
    def printQuarter(self):
        toPrint = self._term + " " + self._year + "\n"
        toPrint += self.courses.__str__() + "\n"
        toPrint += "Total units: " + str(self.units) + "\n"
        toPrint += "Term GPA: " + str(round(self.GPA,3))

        return toPrint
    def printQuarterNOGPA(self):
        toPrint = self._term + " " + self._year + "\n"
        toPrint += self.courses.__str__() + "\n"
        toPrint += "Total units: " + str(self.units)
        print(toPrint)
    def __str__(self):
        if self.isDefined() == True:
            return '\t' + self._term + " " + self._year
        else:
            return '\t' + "*" + self._term + " " + self._year
    def __lt__(self, other):
        if int(self.getYear()) < int(other.getYear()):
            return True
        elif int(self.getYear()) == int(other.getYear()):
            if self.getTermIndex() < other.getTermIndex():
                return True
            else:
                return False
        else:
            return False
    def __eq__(self, other):
        if int(self.getYear()) == int(other.getYear()):
            if self.getTermIndex() == other.getTermIndex():
                return True
            else:
                return False
        else:
            return False
    def __gt__(self, other):
        if int(self.getYear()) > int(other.getYear()):
            return True
        elif int(self.getYear()) == int(other.getYear()):
            if self.getTermIndex() > other.getTermIndex():
                return True
            else:
                return False
        else:
            return False