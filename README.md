# Expense Tracker

# Overview

The Expense Tracker is a Python-based desktop application designed to help users manage and monitor their daily expenses. The application provides a clean and intuitive interface using the tkinter library and supports basic CRUD operations (Create, Read, Update, Delete). It also includes features like expense categorization, summaries, and data persistence using an SQLite database.

This project demonstrates Object-Oriented Programming (OOP) principles, GUI development, and database integration, making it a comprehensive example of Python application development.

---
Expense_Tracker/
|
├── expense_tracker/
│   ├── __init__.py               # Package initializer
│   ├── base_classes.py           # Base classes for managers and UI components
│   ├── expense.py                # Defines the Expense class
│   ├── expense_manager.py        # Manages CRUD operations for expenses
│   └── ui_manager.py             # Handles the graphical user interface
|
├── app.py                        # Entry point for the application
└── README.md                     # Project documentation
---

## Features

Add, edit, and delete expenses.
View all recorded expenses in a tabular format.
Categorize expenses into predefined categories (e.g., Food, Transportation, Utilities).
View a summary of total expenses by category.
Persistent data storage using SQLite.
User-friendly tkinter interface.



---


## Installation

Follow these steps to set up and run the Expense Tracker system:

**Prerequisites**

1. Make sure Python 3.6 or later is installed on your computer. You can download it from the official Python website: https://www.python.org/downloads/.

2. Confirm Python is installed by checking its version. This ensures compatibility.


**Clone the Repository**

1. Clone the repository to your local machine:

git clone https://github.com/Hanjishi/Expense_Tracker.git


2. Navigate into the project directory:

cd Expense_Tracker



**Run the Application**

1. Start the application directly by running the following command:

python app.py
or
python3 app.py

2. The Expense Tracker UI will launch, and you can begin tracking your expenses.


Notes
No additional installations are needed since the system only uses built-in Python libraries (tkinter and sqlite3).
Make sure your Python installation includes tkinter, as it is required for the GUI.


---

## Usage

1. **Add an Expense**
Open the application.
Click "Add Expense".
Enter the amount, category, date, and optional description.


2. **Edit an Expense**
Select an expense from the table.
Click "Edit Expense".
Modify the details and save.

3. **Delete an Expense**
Select an expense from the table.
Click "Delete Expense".

4. **View Expense Summary**
Click "View Summary" to see the total expenses by category.



---

## Example

1. **Adding an Expense**
2. **Viewing Expenses**
3. **Deleting Expenses**
4. **SummaryExpense Tracker**

---
