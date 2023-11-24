# function -> renderUserInterFace : takes no parameter, responsible for rendering menu options for the user
def renderUserInterfaceOptions():
    print("\n     1. Open Tab")
    print("     2. Close Tab")
    print("     3. Switch Tab")
    print("     4. Display All Tabs")
    print("     5. Open Nested Tab")
    print("     6. Sort All Tabs")
    print("     7. Save Tabs")
    print("     8. Import Tabs")
    print("     9. Exit\n") 


# function -> Menu : takes no parameter, responsible for handling menu functionality
def Menu():
    exit_program = False # exit_program will severs as a flag variable 

    # continue looping while exit_program is false
    while not exit_program:
        renderUserInterfaceOptions()
        # handling Exceptions
        try:
            options = int(input("choose one of these options ? "))
        except ValueError:
            print("\ninvalid input a number must be entered - Try Again")

Menu()





# handling exceptions wasn't explained however during code review sessions some class mates uses them to handle user inputs so I had to look out for the offical documentation to learn how to implemet it in python URL : https://docs.python.org/3/tutorial/errors.html


# Within each step code will be tested to prevent unexpected errors
