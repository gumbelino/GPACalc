import SetupQuarter
import LinkedList
import Quarter
import Course
import re

SetupQtr = SetupQuarter.SetupQuarter()
quarters = LinkedList.myLL()
originalGPA = 0

def getUnits():
    units = 0
    for i in range (0, quarters.size()):
        qtr = quarters.get(i)
        units += qtr.getUnits()
        return units

def getUnitsTaken():
    defUnits = 0
    for i in range (0, quarters.size()):
        qtr = quarters.get(i)
        defUnits += qtr.defUnits()
        return defUnits


def printGPA(currQtr, diffGPA, newGPA):
    if diffGPA > 0:
        print("\t>\tYour " + currQtr.getName() + " GPA went UP by " + str(diffGPA) + ":", newGPA)
    elif diffGPA < 0:
        print("\t>\tYour " + currQtr.getName() + " GPA went DOWN by " + str(abs(diffGPA)) + ":", newGPA)
    else:
        print("\t>\tYour " + currQtr.getName() + " GPA did NOT change:", newGPA)

def printGenGPA(diffGenGPA, newGenGPA):
    if diffGenGPA > 0:
        print("\t>\tYour General GPA went UP by " + str(diffGenGPA) + ":", newGenGPA)
    elif diffGenGPA < 0:
        print("\t>\tYour General GPA went DOWN by " + str(abs(diffGenGPA)) + ":", newGenGPA)
    else:
        print("\t>\tYour General GPA did NOT change:", newGenGPA)


def getGPADiff():
    newGPA = getGenGPA(quarters)
    diff = newGPA - originalGPA
    diff = round(diff, 3)
    if diff > 0:
        print("\t>\tYour original GPA went UP by " + str(diff) + ":", newGPA)
    elif diff < 0:
        print("\t>\tYour original GPA went DOWN by " + str(abs(diff)) + ":", newGPA)
    else:
        print("\t>\tYour original GPA is the same:", newGPA)

def chooseQuarter():
    print(quarters.printWithIndex())
    qtrIndex = input("Select a quarter: ")
    if qtrIndex == '':
        return None
    qtrIndex = int(qtrIndex)-1
    qtr = quarters.get(qtrIndex)
    return qtr


def chooseQuarterIndex():
    print(quarters.printWithIndex())
    qtrIndex = input("Select a quarter: ")
    if qtrIndex == '':
        return None
    qtrIndex = int(qtrIndex)-1
    return qtrIndex


def chooseCourseIndex():

    print(quarters.printWithIndex())
    qtrIndex = input("Select a quarter: ")
    if qtrIndex == '':
        return None
    qtrIndex = int(qtrIndex)-1
    return qtrIndex

def setupCourse():
    toAddCourse = input('Enter the course (Eg. CSE 30): ')
    toAddCourse = re.compile('\w+').findall(toAddCourse)
    dpt = toAddCourse[0].upper()
    num = toAddCourse[1].upper()
    units = input('Enter the units: ')
    units = float(units)
    course = Course.course(dpt,num,units)
    return course


def getGenGPA(quarters):
    genGTU = 0
    genUnits = 0
    for i in range (0, quarters.size()):
        qtr = quarters.get(i)
        genGTU += qtr.getGTU()
        genUnits += qtr.defUnits()
    if genUnits > 0:
        genGPA = genGTU/genUnits
    else:
        genGPA = 0
    return round(genGPA,3)


def addQuarter(quarter):
    index = 0
    if quarters.size() > 0:
       curr = quarters.get(index)
       while quarter > curr:
           index += 1
           if index == quarters.size():
               break
           curr = quarters.get(index)
    quarters.addIndex(quarter,index)


while True:

    options = "SELECT AN OPTION:\n"
    options += "[s]etup quarter, [a]dd grades, [c]hange a grade,\n"
    options += "[p]rint quarter, [i]nsert course, [g]eneral GPA,\n"
    options += "[d]elete quarter, [r]ead from file, [w]rite to file,\n"
    options += "[e]rase course, [o]riginal GPA, [Ctrl+D] to exit the program\n"
    options += "Enter an option: "
    try:
        opt = input(options)
    except:
        opt = EOFError

    if opt == 's':

        qtr = SetupQtr.setup()
        addQuarter(qtr)
        qtr.printQuarterNOGPA()

    elif opt == 'p':

        if quarters.size() == 0:
            print("\t>\tYou must setup a quarter before.")
            continue

        qtr = chooseQuarter()
        if qtr is None:
            continue
        print(qtr.printQuarter())

    elif opt == 'c':

        if quarters.size() == 0:
            print("\t>\tYou must setup a quarter before.")
            continue

        currQtr = chooseQuarter()
        currQtr.printWithIndexes()
        oldGenGPA = getGenGPA(quarters)
        oldGPA = currQtr.getGPA()

        CourseIndex = input("Select a course: ")
        CourseIndex = int(CourseIndex)-1
        course = currQtr.getCourse(CourseIndex)
        courseName = course.getName()
        grade = input("Enter grade for " + courseName + ": ")
        currQtr.changeGrade(CourseIndex,grade.upper())

        newGPA = currQtr.getGPA()
        newGenGPA = getGenGPA(quarters)

        diffGPA = newGPA - oldGPA
        diffGPA = round(diffGPA,3)
        diffGenGPA = newGenGPA - oldGenGPA
        diffGenGPA = round(diffGenGPA,3)

        printGPA(currQtr, diffGPA, newGPA)
        printGenGPA(diffGenGPA,newGenGPA)

    elif opt == 'a':

        if quarters.size() == 0:
            print("\t>\tYou must setup a quarter before.")
            continue
        currQtr = chooseQuarter()

        oldGenGPA = getGenGPA(quarters)

        for i in range(0, currQtr.size()):
            course = currQtr.getCourse(i)
            courseName = course.getName()
            grade = input("Enter the grade for " + courseName + ": ")
            currQtr.changeGrade(i,grade.upper())

        newGenGPA = getGenGPA(quarters)

        diffGenGPA = newGenGPA - oldGenGPA
        diffGenGPA = round(diffGenGPA,3)

        print(currQtr.getName(), "GPA:", str(currQtr.getGPA()))
        printGenGPA(diffGenGPA, newGenGPA)

    elif opt == 'w':

        file = input("Enter file name: ")
        file = "files/" + file + ".txt"
        fid = open(file, 'w')
        genGPA = getGenGPA(quarters)

        toWrite = "Your General GPA is " + str(genGPA) + "\n"

        print("\t>\tWriting to " + file)
        fid.write(toWrite)
        for i in range(0,quarters.size()):
            currQtr = quarters.get(i)
            fid.write(currQtr.printQuarter())
            fid.write("\n\n")
        print("\t>\t"+ str(quarters.size()) + " quarter(s) written to file.")
        originalGPA = getGenGPA(quarters)
        print("\t>\tOriginal GPA set to " + str(originalGPA) + ".")
        fid.close()


    elif opt == 'r':

        file = input("Enter file name: ")
        file = "files/" + file + ".txt"
        fid = open(file, 'r')
        qtr = None
        course = None
        numQuarters = 0

        print("\t>\tReading from " + file)

        for line in fid:
            line = re.compile('[a-zA-Z+-]+|[0-9A-Z.]+|[\t]+').findall(line)

            be = None
            if line.__len__() > 0:
                be = line[0]

            if be == 'FALL' or be == 'WINTER' or be == 'SPRING' or be == 'SUMMER':
                term = line[0].upper()
                year = line[1]
                qtr = Quarter.quarter(term,year)

            elif be == '\t':
                dept = line[1].upper()
                num = line[2].upper()
                units = float(line[3])
                grade = line[4].upper()
                course = Course.course(dept,num,units)
                course.setGrade(grade)
                qtr.addCourse(course)

            elif be == "Total":
                addQuarter(qtr)
                numQuarters += 1
                qtr = None

        print("\t>\t" + str(numQuarters) + " quarter read from file.")
        originalGPA = getGenGPA(quarters)
        print("\t>\tOriginal GPA set to " + str(originalGPA) + ".")
        fid.close()

    elif opt == 'i':

        if quarters.size() == 0:
            print("\t>\tYou must setup a quarter before.")
            continue

        qtr = chooseQuarter()
        course = setupCourse()
        qtr.addCourse(course)

    elif opt == 'g':

        if quarters.size() == 0:
            print("\t>\tYou must setup a quarter before.")
            continue

        genGPA = getGenGPA(quarters)
        print("\t>\tYour General GPA is:", genGPA)

    elif opt == 'd':

        if quarters.size() == 0:
            print("\t>\tYou must setup a quarter before.")
            continue

        oldGenGPA = getGenGPA(quarters)

        qtrIndex = chooseQuarterIndex()
        qtr = quarters.removeIndex(qtrIndex)
        if qtr is None: continue
        print("\t>\tRemoving " + qtr.getName()+ ".")
        newGenGPA = getGenGPA(quarters)

        diffGenGPA = newGenGPA - oldGenGPA
        diffGenGPA = round(diffGenGPA,3)

        printGenGPA(diffGenGPA,newGenGPA)

    elif opt == 'e':

        if quarters.size() == 0:
            print("\t>\tYou must setup a quarter before.")
            continue

        currQtr = chooseQuarter()
        if currQtr is None: continue
        currQtr.printWithIndexes()

        oldGenGPA = getGenGPA(quarters)
        oldGPA = currQtr.getGPA()

        courseIndex = input("Select a course: ")
        courseIndex = int(courseIndex)-1
        course = currQtr.removeCourse(courseIndex)
        if course is None: continue

        print("\t>\tRemoving " + course.getName() + ".")

        newGPA = currQtr.getGPA()
        newGenGPA = getGenGPA(quarters)

        diffGPA = newGPA - oldGPA
        diffGPA = round(diffGPA,3)
        diffGenGPA = newGenGPA - oldGenGPA
        diffGenGPA = round(diffGenGPA,3)

        printGPA(currQtr, diffGPA, newGPA)
        printGenGPA(diffGenGPA,newGenGPA)

    elif opt == 'o':
        if quarters.size() > 0 and originalGPA > 0:
            getGPADiff()

    elif opt is EOFError:
        print("Thank you, Gus says thank you!")
        break



