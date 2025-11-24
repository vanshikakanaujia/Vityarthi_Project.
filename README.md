# Vityarthi_Project.
The expense tracker is a simple Python program that helps users record daily spending. it stores expenses with amount, category and date. Users can add, view, delete, and filter expenses and also check monthly totals. it is easy to use and useful for basic budgeting.
1. Project Description
The CLI Expense Tracker is a simple, textual-based application that helps users manage their own personal finances in a user-friendly environment. Written in Python, the software allows users to enter their daily spending, categorize that spending, and analyze their spending habits without needing sophisticated database software or requiring an internet connection.
Users can keep records of spending using the data persistence feature which saves data in a CSV (Comma Separated Values) file. If a user deletes the application, the data will remain saved even when the program is closed. The CLI Expense Tracker is a relatively "lightweight" application that still implements a menu-driven interface that allows the user to simply Create, Read, Update, and/or Delete one or multiple items of financial data.

2. Functionality
Data Persistence: Automatically creates and opens an expenses.csv file to store the data (and maintains this file during the program session).
Add Expenses: Users will specify Date, Category, Amount, and optional Notes for any records of spending. The system provides an ID that auto-increments and the Date will automatically default to the current Date when left blank.
View/List All Entries: A formatted list of all the transactions of spending with a grand total calculated for all spending is displayed.
View by Category: Users may "filter" a view of the expenses by choice of category (e.g., Food, Transport) to show how much has been spent for a particular category or categories.
Monthly Summary: The system will calculate the total for the spending spent for a month of a specific year (Input: YYYY-MM) to help track the monthly budget.
Removal of Entry: The user of the application will be able to remove actual expenses.
Delete Entry: This feature allows for deleting individual expense entries using a specific ID.
Error Handling: The program will handle the, improper date formats or non-integer amounts to ensure it will not crash when invalid entries are provided.

3. Technologies/Tools Used
Programming Language: Python version 3.x
Interface: Command Line Interface (CLI)
Storage: CSV (Flat file database)
Standard libraries for Python language:
csv: For reading and writing to the storage file.
os: To check for file presence.
datetime: For date and assignment of timestamp.
collections: For data structures.

4. Steps to install the project and run it
Prerequist: Make sure you have Python 3.x installed on your machine. You can check this by typing python --version in your terminal/command prompt.
Create File: Open a Text Editor of your choice (Notepad, VS Code, PyCharm) and copy and paste the code provided.
Save: Save the file as expense_tracker.py.
Open Terminal: Open your Command prompt (Windows) or Terminal (Mac/Linux) and get change directory to the location where you saved the file.
Example: cd Desktop/MyProjects

5. Procedure for Testing
To confirm that the project is functioning as expected, the following "Happy Path" test case should be completed:
Initialize the App: Read the instructions and start the application. You should see "Welcome!" and the 6-item Menu.
Test Add (Option 1):
Chose 1.
Do not enter a Date (just press Enter), which will default to today’s date.
Enter Category: Food.
Enter Amount: 250.
Enter a Note: Lunch.
Result: You should see "Saved expense id=1".
Test View (Option2):
Select 2.
Result: You should see the table that includes the new entry and a Total of ?250.00.
Test Filter (Option 4):
Select 4.
Enter Category: Food.
Result: You should see only the entry for the lunch.
Test Monthly Total (Option 5):
Select 5.
Press Enter (for current month).
Result: You should see "Total for [Current-Month]: ?250.00".
Test Delete (Option 3):
Select 3.
Type in id: 1.
Result: You should see "Deleted expense id 1".
Confirmation of the Delete: Select 2 again, and you will see an empty list.
