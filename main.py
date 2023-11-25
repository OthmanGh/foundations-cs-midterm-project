# Note : most function will get tabs and tabsInOrder as a parameters/arguments so instead of commenting multiple time same thing will explain them down here once
# parameter tabs : a dictionary contains our tabs titles attached with thier urls
# parameter tabsInOrder :ma list that shows the order of opened tabs, items of the list will be represented as the title of tabs

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

# function -> isTitleValid : check if user entered tab's title is valid based on a certain conditions
# parameter -> title : user entered tab's title
def isTitleValid(title):
    
    if len(title) < 2: # at least contain 3 letters
        return False
    
    for char in title: # Time Complexity : O(n), n length of title
        if char.isdigit(): # should not contain any digits
            return False

    if not title.isalnum(): # title name shouldn't include any symbols
        return False
    
    return True

# function -> isUrlValid : since we are not asked to validate urls, this maybe handled later
# parameter : user entered url
def isUrlValid(url):
    return len(url) > 5

# function -> openTab : takes 2 parameters, allow the user to add a new tab 
def openTab(tabs, tabsInOrder):
    title = input("\nenter tab title : ") # enter tab's title
    
    if isTitleValid(title): # check if tab's title is valid
        url = input("enter URL of the website : ") # input url 😀
        if isUrlValid(url): # check if url is valid
            tabs[title] = url # add title associated with url to tabs dictionary
            tabsInOrder.append(title) # add title to order tabs list
        else:
            print("\ninvalid URL !!!")
    else:
        print("\ninvalid title name - Try Again")


# function isValidIndex : takes 2 parameters, responsible for checking if the user entered a valid index value
def isValidIndex(index, tabsInOrder): 
    try:
        idx = int(index)
        return 0 <= idx < len(tabsInOrder) #  if index is an actual number must be in range of list 0 <= index < len(list) otherwise generate error

    except ValueError:
        return False


# fuction closeTab : responsible for closing user's selected tab
def closeTab(tabs, tabsInOrder):
    index =  input("\nindex of tab you wish to close : ")

    if len(tabsInOrder) >= 1:
        if isValidIndex(index, tabsInOrder):
            del tabs[tabsInOrder[int(index)]]
            tabsInOrder.pop(int(index))
        elif index == '':
            del tabs[tabsInOrder[-1]]  # -1 to pick last item of dictionary
            tabsInOrder.pop()
        else:
            print("Invalid index - must be a number in the range of opened tabs")
    else:
        print("no tab is opened currently")


# function -> executeMenuOption : takes a single parameter, depending on the provided option value, a corresponding function will be called to deliver specific functionality... 
# parameter -> option : represent user chosen option from menu interface
def executeMenuOption(option, tabs, tabsInOrder):
    # creating our data structure here will lead to be re-initialized every time function is called so we'll loose our data
    if option == 1:
        openTab(tabs, tabsInOrder)
    elif option == 2:
        closeTab(tabs, tabsInOrder)
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
    # 1 - Dictionary to store tabs which consists of titles attached to URLs (tabs)
    # 2 - List to maintain the order of open tabs (tabsInOrder) which contain titles of opened tabs in order (depend on the way been inputed)
    # keep in mind list and dictionaries are referenced data structures so they got passed by reference which means adding/removing local data will modify original data
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

# pop() method : remove specified index in a list, if no index provided it removes last item from list docs: https://www.w3schools.com/python/python_lists_remove.asp

# How to Remove a Key from a Dict Using the del Keyword docs : https://www.freecodecamp.org/news/python-remove-key-from-dictionary/

# False Values in Python docs : https://docs.python.org/release/2.5.2/lib/truth.html

# isalnum() method : returns True if all the characters are alphanumeric. Docs: https://www.w3schools.com/python/ref_string_isalnum.asp