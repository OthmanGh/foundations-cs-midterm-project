# Within each step code will be tested to prevent unexpected errors

# First let's start by creating our Menu function which will take no parameter and output options, one of them will be chosen by the user

def Menu():
    exit_program = False

    while not exit_program:

        print("     1. Open Tab")
        print("     2. Close Tab")
        print("     3. Switch Tab")
        print("     4. Display All Tabs")
        print("     5. Open Nested Tab")
        print("     6. Sort All Tabs")
        print("     7. Save Tabs")
        print("     8. Import Tabs")
        print("     9. Exit")    
        
        options = int(input("choose one of these options ? "))

        print(options)

Menu()
