1. Problem Statement
Many people, primarily students and young professionals, do not maintain managing their money and reserves because they are simply unaware of their spending habits. Old methods of documenting personal spending, such as a physical notebook, are likely to get lost or damaged, and they also can't perform calculations. Mobile apps will likely need internet, require account creation (often mandatory), or would overwhelm the user with intricate services intended for tracking. There is a need for a digital solution that is a lightweight, offline, and completely private experience that allows a user to quickly document and track their spending without set up time.

2. Project Scope
The project scope is restricted to the creation of a standalone Desktop Command Line Interface (CLI) application in Python. 
In-Scope: 
- Development of a text-based user interface for menus. 
- Implementation of CSV file handling for persistent local storage (Create, Read, Update, Delete operations). 
- Core logic for adding expenses, totaling amounts, and filtering data by date or category. 
- Basic error handling to prevent invalid user inputs (e.g., dates and numbers).
Out-of-Scope: 
- Integration with bank APIs or reading SMS automatically. 
- Cloud syncing or multi-device synchronization. 
- Graphical User Interfaces (GUI) or mobile app development. 
- Multi-user logins (login systems). 

3. Target Users
Students: People who are on very limited pocket money or stipends who want to closely monitor exactly where their money is going (food, print-out, travel). 
Privacy-Conscious Individuals: Users who do not want to share or transmit any of their financial data to third parties or cloud apps. 
Minimalist/Technology-oriented Individuals: Users who wish to interact with the application quickly using only the keyboard rather than having to navigate complex graphical menus.
Beginner Programmers: Someone in search of an open-source tool that they can modify themselves, or build upon themselves. 

4. High Level Features
Transaction Management: Users can log expenses with full attributes including a unique ID, dates (with auto-fill for "today"), categories, exact amounts, and an optional note.
Durable Data Storage: The application automatically creates and maintains an expenses.csv file, so that data is saved to a local file which is auto-loaded the next time the app is run.
Category Filtering: A search function that retrieves transactions based on user-defined categories (e.g. getting all "Food" expenses), for the purpose of having easier analysis of spending.
Monthly Totals: A report that provides a total of all expenses for a specified month (YYYY-MM format) so the user can easily see their monthly burn rate.
Record Deletion: The ability to permanently delete bad records using a unique ID system to ensure the very best tracking.
