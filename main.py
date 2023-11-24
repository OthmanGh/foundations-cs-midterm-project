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

# function -> isTitleValid : check if user entered tab's title is valid based on certain a conditions
# parameter -> title : user entered tab's title
def isTitleValid(title):
    if len(title) < 2: # at least contain 3 letters
        return False
    
    for char in title: # Time Complexity : O(n), n length of title
        if char.isdigit(): # should not contain any digits
            return False

    return True

# function -> isUrlValid : since we are not asked to validate urls, this maybe handled later
# parameter : user entered url
def isUrlValid(url):
    if len(url) < 5:
        return False
    
    return True

# function -> openTab : takes a single parameter which will hold user entered tabs
# parameter -> tabs : a dictionary holds tabs titles associated with URLs
def openTab(tabs, tabsOrder):
    
    title = input("\nenter tab title : ") # enter tab's title
    
    if isTitleValid(title): # check if tab's title is valid
        url = input("enter URL of the website : ")
        if isUrlValid(url): # check if url is valid
            tabs[title] = url # add title associated with url to tabs dictionary
            tabsOrder.append(title)
    else:
        print("\ninvalid title name - Try Again")


# function -> executeMenuOption : takes a single parameter, depending on the provided option value, a corresponding function will be called to deliver specific functionality.. 
# parameter -> option : represent user chosen option on menu interface
def executeMenuOption(option, tabs, tabsOrder):

    # creating our data structure here will lead to be re-initialized every time function is called so we'll loose our data

    if option == 1:
        openTab(tabs, tabsOrder)
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

    # Main Data Structures : 
    # Dictionary to store tabs which consists of titles attached to URLs (tabs)
    # List to maintain the order of open tabs (tabsOrder) which contain titles of opened tabs in order (depend on the way been inputed)

    tabs = {}
    tabsOrder = []

    # continue looping while exit_program is false
    while not exit_program:
        renderUserInterfaceOptions() # display menu option
        # handling Exceptions
        try:
            chosenOption = int(input("choose one of these options ? ")) # type casting entered number
        except ValueError: # if inputed data is not a number
            print("\ninvalid input a number must be entered - Try Again")

        executeMenuOption(chosenOption, tabs, tabsOrder) 

    
        print(tabs)
        print(tabsOrder)

Menu()


# handling exceptions documentation  URL : https://docs.python.org/3/tutorial/errors.html
# isdigit() method : return true if all characters are digits other wise return false docs : https://www.w3schools.com/python/ref_string_isdigit.asp
