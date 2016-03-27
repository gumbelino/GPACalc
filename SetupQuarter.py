import re
import Quarter
import Course

class SetupQuarter:

    def setup(self):

        toAddQtr = input('Enter the quarter (Eg. FALL 2015): ')
        toAddQtr = re.compile('\w+').findall(toAddQtr)
        term = toAddQtr[0].upper()
        year = toAddQtr[1]

        qtr = Quarter.quarter(term, year)

        while True:
            toAddCourse = input('Enter the course (Eg. CSE 30): ')

            if toAddCourse == "":
                break

            toAddCourse = re.compile('\w+').findall(toAddCourse)
            dpt = toAddCourse[0].upper()
            num = toAddCourse[1].upper()
            units = input('Enter the units: ')
            units = float(units)

            course = Course.course(dpt,num,units)

            qtr.addCourse(course)

        return qtr
