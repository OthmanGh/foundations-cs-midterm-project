# Note : most functions will get tabs and tabsInOrder as a parameters/arguments so, instead of commenting multiple time same thing will explain them down here once
# most functions will work fine within one level of nested tabs....
# Ouside loops time complexity is O(1) constant time
# Parameters:
# tabs : Dictionary to store tabs which consists of titles attached to another dictionary which may consist of 3 main keys url, htmlContent, nestedTab sure each one of them will be attached to values
# tabsInOrder : List to maintain the order of open tabs (tabsInOrder) which contain titles of opened tabs in order (depend on the way been inputed)

# Function -> renderUserInterFaceOptions : takes no parameter, responsible for displaying menu options for the user
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
    if len(title) < 3:  # at least contain 3 chars
        return False

    for char in title:  # Time Complexity : O(n), n length of title
        if char.isdigit():  # Should not contain any digits
            return False

    for char in title:  # Title name shouldn't include any symbols except spaces
        if char != ' ':
            if not char.isalnum(): 
                return False

    return True

# how to check if a URL is valid or not docs : https://stackoverflow.com/questions/7160737/how-to-validate-a-url-in-python-malformed-or-not
from urllib.parse import urlparse

# Function -> isUrlValid : since we are not asked to validate urls, this maybe handled later.
# Parameter -> url : user entered url
def isUrlValid(url): 
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False


# Function -> openTab : takes 2 parameters, allow the user to add a new tab
def openTab(tabs, tabsInOrder):
    title = input("\nenter tab title : ")  # Enter tab's title

    if isTitleValid(title):  # Check if tab's title is valid
        url = input("enter URL of the website : ")  # Input url 😀
        if isUrlValid(url):  # Check if url is valid
            tabs[title] = {'url' : url}  # Add title attached to dictionary that contains url link
            tabsInOrder.append(title)  # Add title to order tabs list
        else:
            print("\ninvalid url....")
    else:
        print("\ninvalid title name - Try Again")


# Function -> isValidIndex : takes 2 parameters, check if user entered index value is valid
# Parameter -> index : 
def isValidIndex(index, tabsInOrder):
    try:
        idx = int(index)
        # if index is an actual number must be in range of list 0 <= index < len(list) otherwise generate error
        return 0 <= idx < len(tabsInOrder)

    except ValueError: #ValueError raised when a function receives an argument of the correct type but an inappropriate value. 
        return False


# Fuction -> closeTab : takes 2 parameters, responsible for closing user's selected tab
def closeTab(tabs, tabsInOrder):
    index = input("\nindex of tab you wish to close : ")

    if len(tabsInOrder) >= 1: # Check if there are at least one opened tab
        if isValidIndex(index, tabsInOrder): # Check if inputed index val is valid
            idx = int(index) # Convert index to number
            title = tabsInOrder[idx] if len(tabsInOrder[idx]) == 1 else tabsInOrder[idx][0] # Check if tab inclueds nested tab
            del tabs[title] # Celete the whole tab
            tabsInOrder.pop(int(index)) # Remove selected tab at its specified index 
        elif index == '': # User provide no input
            print("\nsince no index provided last tab will be closed")
            del tabs[tabsInOrder[-1]]  # -1 To delete last tab from tabs dictionary
            tabsInOrder.pop() # Remove selected tab
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
    url = tabs[title]['url'] 

    # 3 - Send a HTTP request to the specified URL and save the response from server in a response object called r.
    r = requests.get(url) 

    # 4 - Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(r.content, 'html.parser') 

    # creating an 'htmlContent' key within the value dictionary of each Title
    tabs[title]['htmlContent'] = soup
    print("\n")
    print({title : tabs[title]['htmlContent']})

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


# If the admin chooses (4), the system should print the titles of all open tabs. If there are nested tabs, display them hierarchically.
def displayAllTabs(tabsInOrder):
    if len(tabsInOrder) >= 1: 
        print("\nTitles of All Opened Tabs : ")
        for title in tabsInOrder: # Time Comlexity O(n), n length of tabsInOrder list
            if type(title) == str:
                print(title)
            elif type(title) == list:
                print(title[0])
                print(f"  {title[1]}")            
        print("\n")
    else:
        print("no tab is opened currently")

# If the admin chooses (5), the system should enable users to create nested tabs by specifying the index of the parent tab where they want to insert additional tabs. After entering the index, the system should prompt the user to input the titles and contents for the new tabs.

# Function openNestedTab 
def openNestedTab(tabs, tabsInOrder):
    if len(tabsInOrder) >= 1: # Check if there are an actual opened tabs
        index = input("What is the index of the parent tab that you want to insert additional tabs : ")

        if isValidIndex(index, tabsInOrder) : # Check if index val is valid
            idx = int(index) # Convert to actu    title = input("\nenter tab title : ")  # Enter tab's title
            parentTitle = tabsInOrder[idx] #
            childTitle = input("enter nested tab title : ")

            if isTitleValid(childTitle):  # Check if nested tab's title is valid
                url = input("enter URL of the website : ")  # Input url 😀
                if isUrlValid(url):  # Check if url is valid
                    tabs[parentTitle]['nested tab'] = {'url' : url}
                    print(tabs)
                    tabsInOrder[idx] = [parentTitle, childTitle]
                else:
                    print("\ninvalid url....")
            else:
                print("\ninvalid title name - Try Again")


# Function -> merge : takes 3 params, combine sublists into one sorted array
# Params -> starterIdx : first index of tabsInOrder
# Params -> endIdx : last index of tabsInOrder
def merge(list, starterIndx, endIdx): # Time complexity for merging log(N), N number of items inside list
    s = starterIndx 
    m = (starterIndx + endIdx) // 2
    j = m + 1

    temp = []

    while s <= m and j <= endIdx: # Compare 2 sorted sublists to append them into one sorted list
        if list[s].lower() < list[j].lower(): 
            temp.append(list[s])
            s += 1
        else:
            temp.append(list[j])
            j += 1
    
    # Handle remaining elements in one of the lists
    while s <= m:
        temp.append(list[s])
        s += 1

    while j <= endIdx:
        temp.append(list[j])
        j += 1

    k = 0
    for index in range(starterIndx, endIdx + 1):
        list[index] = temp[k]
        k += 1


# Function -> sortAllTabs : takes 3 params,  will sort all elements in tabsInOrder using merge sort algorithm
# Params -> starterIdx : first index of tabsInOrder
# Params -> endIdx : last index of tabsInOrder
# Merge sort is a divide and conquer algorithm, in total time complexity for merge sort is O(Nlog N) where N is the number of items inside list
def sortAllTabs(tabsInOrder, starterIdx, endIdx): # Time Complexity for this function O(logN) N tabs inside list
    # Base Case
    if starterIdx >= endIdx : # We reached this when evey sublist contain only 1 element which considered to be sorted 
        return  
    
    # Recursive Case 
    mid = (starterIdx + endIdx) // 2 # Will split array into 2 part continously
    
    sortAllTabs(tabsInOrder, starterIdx, mid)  # Handle left part of tabsInOrder
    sortAllTabs(tabsInOrder, mid + 1, endIdx)  # Handle right part of tabsInOrder

    merge(tabsInOrder, starterIdx, endIdx) # Call merge to combine sublists into a sorted one


# resources for codes below
# Json docs : https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON, https://www.geeksforgeeks.org/json/
# Read, Write and Parse JSON using Python docs : https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/
# JSON Parsing Errors in Python docs : https://www.geeksforgeeks.org/json-parsing-errors-in-python/, https://ioflood.com/blog/read-json-file-python/
# How to Parse Data From JSON into Python docs : https://www.geeksforgeeks.org/how-to-parse-data-from-json-into-python/
# Difference between except: and except Exception as e docs : https://stackoverflow.com/questions/18982610/difference-between-except-and-except-exception-as-e

import json

def saveTabs(tabs):
    # Enter a file path directory :
    try:
        path = input("Enter a file path : ")

        with open(path, 'a') as outfile: # json data will be saved in provided directory 
            json.dump(tabs, outfile)  # Json.dump() will transform the Python dictionary to a JSON string 
            
    except PermissionError: # Check if directory is not valid
        print("Permission error. Please indicate a valid directory where you have write permissions.")
        
    except Exception as e:
        print(f"unexpected error occured  : {e} !!!")


def importTabs(tabs, tabsInOrder):
            path = input("input a file path to load tabs : ")  # Enter a file path directory :
            try:
                with open(path, 'r') as inputFile:
                    loadedData = json.load(inputFile)
            except PermissionError: # Check if directory is not valid
                print("Permission error. Please indicate a valid directory.")
            except FileNotFoundError:  # Check if targeted file don't exist
                print("File not found. Please check the file path.")
            except json.JSONDecodeError as e: # Check if imported json syntax is valid
                print("invalid json syntax : ", e)
            else:
                tabs.update(loadedData)

                for key in tabs:
                    tabsInOrder.append(key)

# Function -> terminateProgram : takes no parameter, responsible for closing the program by return true to exitProgram variable
def terminateProgram():
    print("Program Terminated.....")
    return True


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
        displayAllTabs(tabsInOrder)
    elif option == 5:
        openNestedTab(tabs, tabsInOrder)
    elif option == 6:
        sortAllTabs(tabsInOrder, 0, len(tabsInOrder) - 1)
    elif option == 7:
        saveTabs(tabs)
    elif option == 8:
        importTabs(tabs, tabsInOrder)
    elif option == 9:
        return terminateProgram()
    else:  # in case inputed number less than 1 or greater than 9
        print("\ninvalid input - Try Again")


# Function -> Menu : takes no parameter, responsible for handling menu functionality
def Menu():
    exitProgram = False  # exitProgram will severs as a flag variable

    # Main Data Structures :
    # 1 - Dictionary to store tabs which consists of titles attached to another dictionary which may consist of 3 main keys url, htmlContent, nestedTab sure each one of them will be attached to values
    # 2 - List to maintain the order of open tabs (tabsInOrder) which contain titles of opened tabs in order (depend on the way been inputed)
    # Keep in mind list and dictionaries are referenced data structures so they got passed by reference which means adding/removing local data will modify original data
    tabs = {}
    orderTabsList = []

    # Continue looping while exitProgram is false
    while not exitProgram:
        renderUserInterfaceOptions()  # Display menu option
        # Handling Exceptions
        try:
            # Type casting entered number
            chosenOption = int(input("choose one of these options ? "))
        except ValueError:  # If inputed data is not a number
            print("\ninvalid input a number must be entered - Try Again")

        exitProgram = executeMenuOption(chosenOption, tabs, orderTabsList)
    
        print(orderTabsList)
      
Menu()

# useful resources to clarify some used methods and explain other concepts : 

# handling exceptions documentation  URL : https://docs.python.org/3/tutorial/errors.html

# isdigit() method : return true if all characters are digits other wise return false docs : https://www.w3schools.com/python/ref_string_isdigit.asp

# pop() method : remove specified index in a list, if no index provided it removes last item from list docs: https://www.w3schools.com/python/python_lists_remove.asp

# How to Remove a Key from a Dict Using the del Keyword docs : https://www.freecodecamp.org/news/python-remove-key-from-dictionary/

# Falsey Values in Python docs : https://docs.python.org/release/2.5.2/lib/truth.html

# isalnum() method : returns True if all the characters are alphanumeric. Docs: https://www.w3schools.com/python/ref_string_isalnum.asp


# Python - Add Dictionary Items docs : https://www.w3schools.com/python/python_dictionaries_add.asp