import tkinter as tk
from expense_tracker.ui_manager import UIManager

def main():
    root = tk.Tk()
    app = UIManager(root)
    root.mainloop()

if __name__ == "__main__":
    main()