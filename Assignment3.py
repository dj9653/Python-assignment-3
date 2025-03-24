#Assignment 3
run = True
courseDictionary = dict()
studentDictionary = dict()
        
def menu():
    print("-------------------------------\n")
    print("   Student/course Dictionary   \n")
    print("-------------------------------\n")    
    print("(1)Add a Course\n")
    print("(2)Delete a Course\n")
    print("(3)Add a Student\n")
    print("(4)Delete a Student\n")
    print("(5)List all Courses\n")
    print("(6)List all Students\n")
    print("(7)Add a Course to Student\n")
    print("(8)Delete a Course from Student\n")
    print("(9)List Student Courses\n")
    print("(0)QUIT\n")
def addCourse(courseId, courseName):
    courseDictionary[courseId] = courseName
    print("You added", courseDictionary[courseId])
def deleteCourse(courseId):
    print("You deleted", courseDictionary[courseId])
    del courseDictionary[courseId]
def addStudent(studentId, studentName, studentMajor, studentEmail):
    # Ensure the student doesn't already exist
    if studentId not in studentDictionary:
        studentDictionary[studentId] = {
            "Name": studentName,
            "Major": studentMajor,
            "Email": studentEmail,
            "Courses": []  # Initialize Courses as an empty list
        }
        print(f"Student added: {studentId}, {studentName}")
    else:
        print("Student ID already exists.")
def deleteStudent(studentId):
    print("You deleted", studentDictionary[studentId])
    del studentDictionary[studentId]
def addCourseToStudent(studentId, courseId):
    if studentId in studentDictionary and courseId in courseDictionary:
        studentDictionary[studentId]["Courses"].append(courseId)
        print(f"You added {courseDictionary[courseId]} to {studentDictionary[studentId]['Name']}")
    else:
        print("Invalid Student ID or Course ID.")

while(run):
    menu()
    choice = input("Enter a number for your Choice\n")
    if choice == "1":
        courseId = input("Enter the Course ID of the Course you would like to add\n")
        courseName = input("Enter the Name of the Course you are Adding\n")
        addCourse(courseId, courseName)
    elif choice == "2":
        courseId = input("Enter the Course ID of the Course you would like to delete\n")
        deleteCourse(courseId)
    elif choice == "3":
        studentId = input("Enter the Student ID of the student you would like to add\n")
        studentName = input("Enter the name of the student you would liek to add\n")
        studentMajor = input("Enter the Major of the student you would like to add\n")
        studentEmail = input("Enter the email of the student you would like to add\n")
        addStudent(studentId, studentName, studentMajor, studentEmail)
    elif choice == "4":
        studentId = input("Enter the Student ID of the student you would like to delete")
        deleteStudent(studentId)
    elif choice == "5":
        print(courseDictionary)
    elif choice == "6":
        print(studentDictionary)
    elif choice == "7":
        studentId = input("Enter the Student ID of the student you are adding a course too")
        courseId = input("Enter the course ID you would like to add to the student")
        addCourseToStudent(studentId, courseId)
        
