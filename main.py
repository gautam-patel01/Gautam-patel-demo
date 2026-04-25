#EMI MASTER - Loan Calculator & Prepayment Simulator

class LoanCalculator:
    def __init__(self):
        self.P = 0
        self.R = 0
        self.N = 0
        self.r = 0

    def get_input(self):
        try:
            self.P = float(input("Enter Loan Amount: "))
            self.R = float(input("Enter Annual Interest Rate (%): "))
            self.N = int(input("Enter Loan Tenure (months): "))

            if self.P <= 0 or self.R <= 0 or self.N <= 0:
                print("Invalid input! Values must be greater than 0.")
                return False

            self.r = self.R / 12 / 100
            return True
        except:
            print("Invalid input format!")
            return False

    def calculate_emi(self):
        emi = (self.P * self.r * (1 + self.r) ** self.N) / ((1 + self.r) ** self.N - 1)
        return emi

    def calculate_total_payment(self, emi):
        return emi * self.N

    def calculate_total_interest(self, total_payment):
        return total_payment - self.P

    def display_details(self, emi, total_payment, total_interest):
        print("\n----- LOAN DETAILS -----")
        print("Loan Amount:", self.P)
        print("Interest Rate:", self.R)
        print("Tenure:", self.N)
        print("-------------------------")
        print("Monthly EMI:", round(emi, 2))
        print("Total Payment:", round(total_payment, 2))
        print("Total Interest:", round(total_interest, 2))

    def prepayment(self):
        try:
            amount = float(input("\nEnter Prepayment Amount: "))
            if amount <= 0:
                print("Invalid amount!")
                return

            self.P = self.P - amount

        except:
            print("Invalid input!")

    def menu(self):
        while True:
            print("\n====== EMI MASTER MENU ======")
            print("1. Enter Loan Details")
            print("2. Calculate EMI")
            print("3. Prepayment Simulation")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                if self.get_input():
                    print("Details saved successfully!")

            elif choice == "2":
                if self.P == 0:
                    print("Enter loan details first!")
                else:
                    emi = self.calculate_emi()
                    total_payment = self.calculate_total_payment(emi)
                    total_interest = self.calculate_total_interest(total_payment)
                    self.display_details(emi, total_payment, total_interest)

            elif choice == "3":
                if self.P == 0:
                    print("Enter loan details first!")
                else:
                    self.prepayment()

            elif choice == "4":
                print("Exiting program...")
                break

            else:
                print("Invalid choice!")


# Run Program
app = LoanCalculator()
app.menu()
