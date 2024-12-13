# Expense Tracker

# Overview

The Expense Tracker is a Python-based desktop application designed to help users manage and monitor their daily expenses. The application provides a clean and intuitive interface using the tkinter library and supports basic CRUD operations (Create, Read, Update, Delete). It also includes features like expense categorization, summaries, and data persistence using an SQLite database.

This project demonstrates Object-Oriented Programming (OOP) principles, GUI development, and database integration, making it a comprehensive example of Python application development.


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

1. Clone the repository:
git clone https://github.com/Hanjishi/Expense_Tracker.git
cd ExpenseTracker


2. Install required dependencies:
Ensure you have Python 3.6+ installed.
Install required libraries:
pip install -r requirements.txt



3. **Run the application:**
python app.py




---
## Package Structure 

Expense_Tracker/
├── expense_tracker/       # Main package
│   ├── __init__.py
│   ├── expense.py
│   ├── expense_manager.py
│   ├── ui_manager.py
│   ├── base_classes.py
├── tests/                 # Test cases
├── images/                # Screenshots for documentation
├── main.py                # Entry point to run the application
├── README.md              # Documentation
├── requirements.txt       # Python dependencies
└── documentation.ipynb    # Jupyter Notebook with explanations


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

Example

1. Adding an Expense
2. Viewing Expenses
3. SummaryExpense Tracker

---
