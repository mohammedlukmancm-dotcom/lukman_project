import tkinter as tk
from tkinter import messagebox

# -------------------- BANK DATA --------------------
PIN = "6767"
balance = 256262585678353400000000000000000000000000000000000000000000000.00

# -------------------- COLORS --------------------
BG = "#060A11"
CARD = "#1E293B"
GREEN = "#00FF5E"
WHITE = "#FFFFFF"
GRAY = "#7F8A99"
RED = "#FF7A7A"


class BankApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SheruBank | Digital Banking")
        self.root.geometry("900x600")
        self.root.configure(bg=BG)
        self.root.resizable(False, False)

        self.show_login()

    # -------------------- LOGIN SCREEN --------------------
    def show_login(self):
        self.clear_screen()

        frame = tk.Frame(self.root, bg=CARD, padx=40, pady=40)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(
            frame,
            text="SERU BANK",
            font=("Arial", 24, "bold"),
            fg=GREEN,
            bg=CARD
        ).pack(pady=10)

        tk.Label(
            frame,
            text="Welcome to Digital Banking",
            font=("Arial", 12),
            fg=GRAY,
            bg=CARD
        ).pack(pady=5)

        tk.Label(
            frame,
            text="Enter your PIN",
            font=("Arial", 11),
            fg=WHITE,
            bg=CARD
        ).pack(pady=(20, 5))

        self.pin_entry = tk.Entry(
            frame,
            font=("Arial", 16),
            show="*",
            justify="center",
            width=20,
            bg=BG,
            fg=WHITE,
            insertbackground=WHITE,
            relief="flat"
        )
        self.pin_entry.pack(ipady=10, pady=10)
        self.pin_entry.focus()

        tk.Button(
            frame,
            text="LOGIN",
            font=("Arial", 11, "bold"),
            bg=GREEN,
            fg=BG,
            width=20,
            relief="flat",
            cursor="hand2",
            command=self.login
        ).pack(pady=20, ipady=8)

        tk.Label(
            frame,
            text="Demo PIN: 1234",
            font=("Arial", 9),
            fg=GRAY,
            bg=CARD
        ).pack()

    def login(self):
        entered_pin = self.pin_entry.get()

        if entered_pin == PIN:
            self.show_dashboard()
        else:
            messagebox.showerror("Login Failed", "Incorrect PIN!")
            self.pin_entry.delete(0, tk.END)

    # -------------------- DASHBOARD --------------------
    def show_dashboard(self):
        self.clear_screen()

        # Header
        header = tk.Frame(self.root, bg=BG)
        header.pack(fill="x", padx=40, pady=25)

        tk.Label(
            header,
            text="SECUREBANK",
            font=("Arial", 20, "bold"),
            fg=GREEN,
            bg=BG
        ).pack(side="left")

        tk.Button(
            header,
            text="Logout",
            bg=RED,
            fg=WHITE,
            relief="flat",
            cursor="hand2",
            command=self.show_login
        ).pack(side="right", ipadx=15, ipady=5)

        tk.Label(
            self.root,
            text="Welcome Back!",
        font=("Arial", 18, "bold"),
            fg=WHITE,
            bg=BG
        ).pack(anchor="w", padx=40, pady=10)

        # Balance card
        balance_card = tk.Frame(self.root, bg=GREEN, padx=30, pady=30)
        balance_card.pack(fill="x", padx=40, pady=15)

        tk.Label(
            balance_card,
            text="TOTAL ACCOUNT BALANCE",
            font=("Arial", 11),
            fg=BG,
            bg=GREEN
        ).pack(anchor="w")https://github.com/mohammedlukmancm-dotcom/lukman_project.git

        self.balance_label = tk.Label(
            balance_card,
            text=f"₹ {balance:,.2f}",
            font=("Arial", 32, "bold"),
            fg=BG,
            bg=GREEN
        )
        self.balance_label.pack(anchor="w", pady=10)

        tk.Label(
            balance_card,
            text="Account: XXXX XXXX 2048",
            font=("Arial", 10),
            fg=BG,
            bg=GREEN
        ).pack(anchor="w")

        # Buttons
        button_frame = tk.Frame(self.root, bg=BG)
        button_frame.pack(fill="x", padx=40, pady=20)

        self.create_button(
            button_frame, "CHECK BALANCE",
            self.check_balance, 0
        )

        self.create_button(
            button_frame, "DEPOSIT MONEY",
            self.deposit, 1
        )

        self.create_button(
            button_frame, "WITHDRAW MONEY",
            self.withdraw, 2
        )

        # Footer
        tk.Label(
            self.root,
            text="Secure • Simple • Digital Banking",
            font=("Arial", 10),
            fg=GRAY,
            bg=BG
        ).pack(side="bottom", pady=20)

    # -------------------- BUTTON DESIGN --------------------
    def create_button(self, parent, text, command, column):
        btn = tk.Button(
            parent,
            text=text,
            font=("Arial", 10, "bold"),
            bg=CARD,
            fg=WHITE,
            activebackground=GREEN,
            activeforeground=BG,
            relief="flat",
            cursor="hand2",
            command=command
        )

        btn.grid(row=0, column=column, padx=8, pady=10,
                 sticky="nsew", ipady=20)

        parent.grid_columnconfigure(column, weight=1)

    # -------------------- CHECK BALANCE --------------------
    def check_balance(self):
        messagebox.showinfo(
            "Account Balance",
            f"Your current balance is:\n\n₹ {balance:,.2f}"
        )

    # -------------------- DEPOSIT --------------------
    def deposit(self):
        global balance

        amount = self.ask_amount("Deposit Money")

        if amount is None:
            return

        if amount <= 0:
            messagebox.showerror("Error", "Enter a valid amount!")
            return

        balance += amount
        self.update_balance()

        messagebox.showinfo(
            "Success",
            f"₹ {amount:,.2f} deposited successfully!"
        )

    # -------------------- WITHDRAW --------------------
    def withdraw(self):
        global balance

        amount = self.ask_amount("Withdraw Money")

        if amount is None:
            return

        if amount <= 0:
            messagebox.showerror("Error", "Enter a valid amount!")
            return

        if amount > balance:
            messagebox.showerror(
                "Insufficient Balance",
                "You don't have enough money!"
            )
            return

        balance -= amount
        self.update_balance()

        messagebox.showinfo(
            "Success",
            f"₹ {amount:,.2f} withdrawn successfully!"
        )

    # -------------------- AMOUNT INPUT -----------------https://github.com/mohammedlukmancm-dotcom/lukman_project.git---
    def ask_amount(self, title):
        dialog = tk.Toplevel(self.root)
        dialog.title(title)
        dialog.geometry("350x200")
        dialog.configure(bg=CARD)
        dialog.resizable(False, False)

        dialog.transient(self.root)
        dialog.grab_set()

        tk.Label(
            dialog,
            text=title,
            font=("Arial", 16, "bold"),
            fg=GREEN,
            bg=CARD
        ).pack(pady=20)

        entry = tk.Entry(
            dialog,
            font=("Arial", 14),
            justify="center",
            bg=BG,
            fg=WHITE,
            insertbackground=WHITE,
            relief="flat"
        )
        entry.pack(padx=30, fill="x", ipady=8)
        entry.focus()

        result = {"amount": None}

        def submit():
            try:
                result["amount"] = float(entry.get())
                dialog.destroy()
            except ValueError:
                messagebox.showerror(
                    "Invalid Input",
                    "Please enter a valid number.",
                    parent=dialog
                )

        tk.Button(
            dialog,
            text="CONTINUE",
            bg=GREEN,
            fg=BG,
            font=("Arial", 10, "bold"),
            relief="flat",
            command=submit
        ).pack(pady=20, ipadx=20, ipady=5)

        dialog.wait_window()
        return result["amount"]

    # -------------------- UPDATE BALANCE --------------------
    def update_balance(self):
        self.balance_label.config(text=f"₹ {balance:,.2f}")

    # -------------------- CLEAR SCREEN --------------------
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# -------------------- RUN APPLICATION --------------------
root = tk.Tk()
app = BankApp(root)
root.mainloop()
print("messi is far far better than ronaldo")
