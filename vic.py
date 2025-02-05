import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

class ChurchMemberApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Church Member Registration")
        self.root.geometry("800x700")

        self.main_frame = tk.Frame(root)
        self.form_frame_1 = tk.Frame(root)
        self.form_frame_2 = tk.Frame(root)
        self.prayer_requests_frame = tk.Frame(root)
        self.search_frame = tk.Frame(root)

        for frame in (self.main_frame, self.form_frame_1, self.form_frame_2, self.prayer_requests_frame, self.search_frame):
            frame.grid(row=0, column=0, sticky="nsew")

        self.create_main_menu()
        self.create_member_form_1()
        self.create_member_form_2()
        self.create_prayer_request_form()
        self.create_search_feature()

        self.main_frame.tkraise()
        self.create_database()

    def create_main_menu(self):
        tk.Label(self.main_frame, text="Welcome to Church Member System", font=("Arial", 20)).pack(pady=20)
        tk.Button(self.main_frame, text="Register New Member", width=20, height=2, command=lambda: self.form_frame_1.tkraise()).pack(pady=10)
        tk.Button(self.main_frame, text="Search Members", width=20, height=2, command=lambda: self.search_frame.tkraise()).pack(pady=10)
        tk.Button(self.main_frame, text="Exit", width=20, height=2, command=self.root.quit).pack(pady=10)

    def create_member_form_1(self):
        tk.Label(self.form_frame_1, text="New Member Registration (Part 1)", font=("Arial", 20)).pack(pady=20)

        fields = ["Surname", "Full Name", "Date of Birth", "Gender", "Street Address", "City", "State", "Postal Code",
                  "Phone Number", "Email", "Children"]
        self.entries_1 = {}
        form_frame_1 = tk.Frame(self.form_frame_1)
        form_frame_1.pack(pady=10)

        for idx, field in enumerate(fields):
            tk.Label(form_frame_1, text=field + ":", font=("Arial", 12)).grid(row=idx, column=0, sticky="w", padx=10, pady=5)
            if field == "Gender":
                self.gender = ttk.Combobox(form_frame_1, values=["Male", "Female", "Other"], state="readonly")
                self.gender.grid(row=idx, column=1, padx=10, pady=5)
            else:
                entry = tk.Entry(form_frame_1, width=60)
                entry.grid(row=idx, column=1, padx=10, pady=5)
                self.entries_1[field] = entry

        tk.Label(form_frame_1, text="Marital Status:", font=("Arial", 12)).grid(row=len(fields), column=0, sticky="w", padx=10, pady=5)
        self.marital_status = ttk.Combobox(form_frame_1, values=["Single", "Married", "Divorced", "Widowed"], state="readonly")
        self.marital_status.grid(row=len(fields), column=1, padx=10, pady=5)

        tk.Button(self.form_frame_1, text="Back", width=20, height=2, command=lambda: self.main_frame.tkraise()).pack(pady=10)
        tk.Button(self.form_frame_1, text="Next", width=20, height=2, command=lambda: self.form_frame_2.tkraise()).pack(pady=10)

    def create_member_form_2(self):
        tk.Label(self.form_frame_2, text="New Member Registration (Part 2)", font=("Arial", 20)).pack(pady=20)

        fields = ["Date of Salvation", "Date of Baptism", "Previous Church", "Previous Church City/State"]
        self.entries_2 = {}
        form_frame_2 = tk.Frame(self.form_frame_2)
        form_frame_2.pack(pady=10)

        for idx, field in enumerate(fields):
            tk.Label(form_frame_2, text=field + ":", font=("Arial", 12)).grid(row=idx, column=0, sticky="w", padx=10, pady=5)
            entry = tk.Entry(form_frame_2, width=60)
            entry.grid(row=idx, column=1, padx=10, pady=5)
            self.entries_2[field] = entry

        tk.Label(form_frame_2, text="Ministry Involvement:", font=("Arial", 12)).grid(row=len(fields), column=0, sticky="w", padx=10, pady=5)
        self.ministry_involvement = ttk.Combobox(form_frame_2, values=["Children", "Youth", "Young Adult", "Adult"], state="readonly")
        self.ministry_involvement.grid(row=len(fields), column=1, padx=10, pady=5)

        tk.Button(self.form_frame_2, text="Back", width=20, height=2, command=lambda: self.form_frame_1.tkraise()).pack(pady=10)
        tk.Button(self.form_frame_2, text="Next", width=20, height=2, command=lambda: self.prayer_requests_frame.tkraise()).pack(pady=10)

    def create_prayer_request_form(self):
        tk.Label(self.prayer_requests_frame, text="Prayer Requests", font=("Arial", 20)).pack(pady=20)
        self.prayer_requests = tk.Text(self.prayer_requests_frame, height=5, width=50)
        self.prayer_requests.pack(pady=10)
        tk.Button(self.prayer_requests_frame, text="Back", width=20, height=2, command=lambda: self.form_frame_2.tkraise()).pack(pady=10)
        tk.Button(self.prayer_requests_frame, text="Submit", width=20, height=2, command=self.add_member).pack(pady=10)

    def add_member(self):
        messagebox.showinfo("Success", "Member added successfully!")
        self.main_frame.tkraise()

    def create_search_feature(self):
        tk.Label(self.search_frame, text="Search Members", font=("Arial", 20)).pack(pady=20)
        self.search_entry = tk.Entry(self.search_frame, width=60)
        self.search_entry.pack(pady=10)
        tk.Button(self.search_frame, text="Search", width=20, height=2, command=self.search_member).pack(pady=10)
        tk.Button(self.search_frame, text="Back", width=20, height=2, command=lambda: self.main_frame.tkraise()).pack(pady=10)

    def search_member(self):
        messagebox.showinfo("Search", f"Searching for {self.search_entry.get()}...")

    def create_database(self):
        pass  # Implement database logic

if __name__ == "__main__":
    root = tk.Tk()
    app = ChurchMemberApp(root)
    root.mainloop()























