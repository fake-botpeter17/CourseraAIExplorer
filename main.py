from CourseDetailExtracterTool import CourseDetailExtracterTool
from db.SQLManager import SQLite
from json import loads, dumps
from utils import CertificateValue, CourseType

ch = True
tool = CourseDetailExtracterTool()
db = SQLite("e:\\CourseraAIExplorer\\db\\courses.db")
db.selectTable("Courses")
highest_entry = db.viewTable(["max(id)"])[0]
max_id = highest_entry[0] if highest_entry[0] else 0

def show_menu():
    print("\n\n")
    print("1. Get Course Details")
    print("2. Clear Screen")
    print("3. Exit\n\n")
    
def save_to_db(cName: str):
    global max_id
    with open(f"Course Details\\{cName}.json") as f:
        content = loads(f.read())
    cType, cVal = content['courseType'],  content['certVal']
    content['courseType'], content['certVal'] = CourseType[cType], CertificateValue[cVal]

    if cType != "sa":
        sCourses = content['subCourses']
        content['subCourses'] = dumps(sCourses)
    else:
        content['subCourses'] = "NIL"
    
    db.insertValue(max_id+1, *content.values())
    max_id+=1
    db.commit()
    print(f"\n\nThe course {content['name']} by {content['provider']} has been saved with ID {max_id}.")
    
    
while ch:
    show_menu()
    choice = input("Enter your choice: ")
    match choice:
        case "1":
            course_name = input("\n\nEnter the course name: ")
            tool.getCourseDetails(course_name, print_res=True, write_file=True)
            loop = True
            while loop:
                save_db = int(input("\n\nDo you want to save this course for later access?\n\t1. Yes\n\t2. No\n\nYour Choice: \t"))
                match save_db:
                    case 1:
                        save_to_db(course_name)
                        loop = False
                    case 2:
                        loop = False
                    case _:
                        print("\n\nInvalid Choice! Try again.")
                        
        case "2":
            print("\033[H\033[J", end="")  # ANSI escape code to clear the screen
        case "3":
            ch = False
        case _:
            print("\n\nInvalid choice. Please try again.")
            continue