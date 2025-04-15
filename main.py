from CourseDetailExtracterTool import CourseDetailExtracterTool

ch = True
tool = CourseDetailExtracterTool()

def show_menu():
    print("1. Get Course Details")
    print("2. Clear Screen")
    print("3. Exit")
    
while ch:
    show_menu()
    choice = input("Enter your choice: ")
    match choice:
        case "1":
            course_name = input("Enter the course name: ")
            tool.getCourseDetails(course_name, print_res=True, write_file=True)
        case "2":
            print("\033[H\033[J", end="")  # ANSI escape code to clear the screen
        case "3":
            ch = False
        case _:
            print("Invalid choice. Please try again.")
            continue