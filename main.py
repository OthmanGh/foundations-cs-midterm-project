# Within each step code will be tested to prevent unexpected errors

# function : renderUserInterFace takes no parameter, responsible for rendering menu options for the user
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


# function : Menu takes no parameter, responsible for handling menu functionality
def Menu():

    exit_program = False # exit_program will severs as a flag variable 

    while not exit_program:
        renderUserInterfaceOptions()
        options = int(input("choose one of these options ? "))

        print(options)

Menu()
