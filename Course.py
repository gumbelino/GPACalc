import GPACalc

class course:

    # string grade
    _grade = None
    # grade weight * units
    _GTU = 0
    # letter to number object
    calc = GPACalc.GPACalc()

    # constructor
    def __init__(self, dept, num, units):
        self._dept = dept
        self._num = num
        self._units = units
        self._name = dept + " " + num

    # setters and getters
    def setGrade(self, grade):
        if grade == 'NONE' or grade == 'None':
            self._grade = None
        else:
            self._grade = grade
        GP = self.calc.gradeToGPA(grade)
        self._GTU = GP*self._units
    def getGTU(self):
        return self._GTU
    def getGrade(self):
        return self._grade
    def getDept(self):
        return self._dept
    def getNum(self):
        return self._num
    def getUnits(self):
        return self._units
    def getName(self):
        return self._name

    # overrides
    def __lt__(self, other):
        if self.getDept() < other.getDept():
            return True
        elif self.getDept() == other.getDept():
            if self.getNum() < other.getNum():
                return True
            else:
                return False
        else:
            return False
    def __eq__(self, other):
        if self._name == other.getName():
            return True
        else:
            return False
    def __gt__(self, other):
        if self.getDept() > other.getDept():
            return True
        elif self.getDept() == other.getDept():
            if self.getNum() > other.getNum():
                return True
            else:
                return False
        else:
            return False
    def __str__(self):
        toString = "\t" + self._name
        toString += '(' + str(self._units) + '): ' + str(self._grade)
        return toString