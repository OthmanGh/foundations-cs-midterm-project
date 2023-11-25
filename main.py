# Note : most functions will get tabs and tabsInOrder as a parameters/arguments so, instead of commenting multiple time same thing will explain them down here once
# Parameters:
# tabs : A dictionary containing tab names as keys and corresponding URLs as values
# tabsInOrder : a list representing the order of tabs

# Function -> renderUserInterFace : takes no parameter, responsible for displaying menu options for the user
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
  

# Function -> isTitleValid : check if user entered tab's title is valid based on a certain conditions
# Parameter -> title : user entered tab's title
# Note : these validation condition based on my preference so it doesn't follow any rule and it can be modifyied
def isTitleValid(title):
    if len(title) < 2:  # at least contain 3 chars
        return False

    for char in title:  # Time Complexity : O(n), n length of title
        if char.isdigit():  # Should not contain any digits
            return False

    if not title.isalnum():  # Title name shouldn't include any symbols
        return False

    return True

# Function -> isUrlValid : since we are not asked to validate urls, this maybe handled later.
# Parameter -> url : user entered url
def isUrlValid(url):
    return len(url) > 5


# Function -> openTab : takes 2 parameters, allow the user to add a new tab
def openTab(tabs, tabsInOrder):
    title = input("\nenter tab title : ")  # Enter tab's title

    if isTitleValid(title):  # Check if tab's title is valid
        url = input("enter URL of the website : ")  # Input url 😀
        if isUrlValid(url):  # Check if url is valid
            tabs[title] = url  # Add title associated with url to dictionary tabs
            tabsInOrder.append(title)  # Add title to order tabs list
        else:
            print("\ninvalid URL !!!")
    else:
        print("\ninvalid title name - Try Again")


# Function -> isValidIndex : takes 2 parameters, check if user entered index value is valid
# Parameter -> index : 
def isValidIndex(index, tabsInOrder):
    try:
        idx = int(index)
        # if index is an actual number must be in range of list 0 <= index < len(list) otherwise generate error
        return 0 <= idx < len(tabsInOrder)

    except ValueError:
        return False


# Fuction -> closeTab : takes 2 parameters, responsible for closing user's selected tab
def closeTab(tabs, tabsInOrder):
    index = input("\nindex of tab you wish to close : ")

    if len(tabsInOrder) >= 1: # Check if there is at least one opened tab
        if isValidIndex(index, tabsInOrder): # Check if inputed index val is valid
            del tabs[tabsInOrder[int(index)]] # Delete selected tab from tabs dictionary
            tabsInOrder.pop(int(index)) # Remove selected tab at its specified index 
        elif index == '': # user provide no input
            print("\nsince no index provided last tab will be closed")
            del tabs[tabsInOrder[-1]]  # -1 To delete last tab from tabs dictionary
            tabsInOrder.pop() # Remove selected tab at its specified index 
        else:
            print("Invalid index - must be a number in the range of opened tabs")
    else:
        print("no tab is opened currently")


# Accessing the HTML content from webpage  docs :  https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/
# youtube : https://www.youtube.com/watch?v=hlSR0JAKpeQ&t=296s&ab_channel=PlayWithCoding

import requests # 1 - First of all import the requests library. 
from bs4 import BeautifulSoup

# Function -> displayHtmlContent : display HTML content
# Parameters:
# - tabs: A dictionary containing tab names as keys and corresponding URLs as values
# - tabsInOrder: A list representing the order of tabs
# - index: An optional parameter specifying the index of the tab to display
def displayHtmlContent(tabs, tabsInOrder, index=''):

    # Determine the title based on the provided index or use the last tab in order
    title = tabsInOrder[-1] if index == '' else tabsInOrder[index] 
    
    # 2 - Specify the URL of the webpage you want to scrape.
    url = tabs[title] 

    # 3 - Send a HTTP request to the specified URL and save the response from server in a response object called r.
    r = requests.get(url) 

    # 4 - Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(r.content, 'html.parser') 

    # Create a formatted output dictionary with the tab title as the key and the prettified HTML as the value
    formattedOutput = {title: soup.prettify()}

    # Print a formatted dictionary with the tab title as the key and the prettified HTML as the value 
    print(formattedOutput)


# Function -> switchTab : takes 2 parameters, responsible for switching tabs to display its html content
def switchTab(tabs, tabsInOrder):

    tabIndex = input("What is the index of the tab to dispalay its content ? ")

    if len(tabsInOrder) >= 1: # Check if there is an actual opened tab
        if isValidIndex(tabIndex, tabsInOrder):
            displayHtmlContent(tabs, tabsInOrder, int(tabIndex))
        elif tabIndex == '':
            displayHtmlContent(tabs, tabsInOrder)
    else:
        print("no tab is opened currently")


# Function -> executeMenuOption : takes a single parameter, depending on the provided option value, a corresponding function will be called to deliver specific functionality...
# Parameter -> option : represent user chosen option from menu interface
def executeMenuOption(option, tabs, tabsInOrder):

    if option == 1:
        openTab(tabs, tabsInOrder)
    elif option == 2:
        closeTab(tabs, tabsInOrder)
    elif option == 3:
        switchTab(tabs, tabsInOrder)
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
    else:  # in case inputed number less than 1 or greater than 9
        print("\ninvalid input - Try Again")


# Function -> Menu : takes no parameter, responsible for handling menu functionality
def Menu():
    exit_program = False  # exit_program will severs as a flag variable

    # Main Data Structures :
    # 1 - Dictionary to store tabs which consists of titles attached to URLs (tabs)
    # 2 - List to maintain the order of open tabs (tabsInOrder) which contain titles of opened tabs in order (depend on the way been inputed)
    # Keep in mind list and dictionaries are referenced data structures so they got passed by reference which means adding/removing local data will modify original data
    tabs = {}
    tabsOrder = []

    # Continue looping while exit_program is false
    while not exit_program:
        renderUserInterfaceOptions()  # Display menu option
        # Handling Exceptions
        try:
            # Type casting entered number
            chosenOption = int(input("choose one of these options ? "))
        except ValueError:  # If inputed data is not a number
            print("\ninvalid input a number must be entered - Try Again")

        executeMenuOption(chosenOption, tabs, tabsOrder)

        print(tabs)
        print(tabsOrder)

Menu()


# useful resources to clarify some used methods and explain other concepts : 

# handling exceptions documentation  URL : https://docs.python.org/3/tutorial/errors.html

# isdigit() method : return true if all characters are digits other wise return false docs : https://www.w3schools.com/python/ref_string_isdigit.asp

# pop() method : remove specified index in a list, if no index provided it removes last item from list docs: https://www.w3schools.com/python/python_lists_remove.asp

# How to Remove a Key from a Dict Using the del Keyword docs : https://www.freecodecamp.org/news/python-remove-key-from-dictionary/

# Falsey Values in Python docs : https://docs.python.org/release/2.5.2/lib/truth.html

# isalnum() method : returns True if all the characters are alphanumeric. Docs: https://www.w3schools.com/python/ref_string_isalnum.asp
