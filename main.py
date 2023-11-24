# function -> openTab : takes a single parameter which will hold user inputed tabs
def openTab(tabs):
    title = input("\nenter tab title : ")
    url = input("enter URL of the website : ")
    tabs[title] = url

# function -> renderUserInterFace : takes no parameter, responsible for displaying menu options for the user
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


# function -> executeMenuOption : takes a single parameter which represent user inputed option
# Depending on the provided option value, a corresponding function will be called to deliver specific functionality.. 

def executeMenuOption(option):
    # Main Data Structure : 
    # Dictionary to store tabs which consists of titles attached to URLs (tabs)
    # list to maintain the order of open tabs (openedTabsOrder)

    tabs = {}
    openedTabsOrder = []

    if option == 1:
        openTab(tabs)
        print(tabs)
    elif option == 2:
        print("\nClosing Tab....")
    elif option == 3:
        print("\nSwitch Tab....")
    elif option == 4:
        print("\nDisplay All Tabs....")
    elif option == 5:
        print("\nOpen Nested Tab")
    elif option == 6:
        print("\nSort All Tabs")
    elif option == 7:
        print("\nSave Tabs")
    elif option == 8:
        print("\nImport Tabs")
    elif option == 9:
        print("\nExit")
    else: # in case inputed number less than 1 or greater than 9
        print("\ninvalid input - Try Again")


# function -> Menu : takes no parameter, responsible for handling menu functionality
def Menu():
    exit_program = False # exit_program will severs as a flag variable 

    # continue looping while exit_program is false
    while not exit_program:
        renderUserInterfaceOptions() # display menu option
        # handling Exceptions
        try:
            chosenOption = int(input("choose one of these options ? ")) # type casting entered number
        except ValueError: # if inputed data is not a number
            print("\ninvalid input a number must be entered - Try Again")

        executeMenuOption(chosenOption) 

Menu()


# handling exceptions documentation  URL : https://docs.python.org/3/tutorial/errors.html