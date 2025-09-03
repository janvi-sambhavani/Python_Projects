class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_role_details(self):
        return f"Employee: {self.name}"

    def yearly_bonus(self):
        return 0


class Developer(Employee):
    def get_role_details(self):
        return f"Developer: {self.name}"

    def yearly_bonus(self):
        return self.salary * 0.1


class Manager(Employee):
    def get_role_details(self):
        return f"Manager: {self.name}"

    def yearly_bonus(self):
        return self.salary * 0.2


if __name__ == "__main__":
    while True:
        print("\n1. Add Developer\n2. Add Manager\n3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter Developer name: ")
            salary = float(input("Enter Developer salary: "))
            dev = Developer(name, salary)
            print(dev.get_role_details(), "Bonus:", dev.yearly_bonus())

        elif choice == "2":
            name = input("Enter Manager name: ")
            salary = float(input("Enter Manager salary: "))
            mgr = Manager(name, salary)
            print(mgr.get_role_details(), "Bonus:", mgr.yearly_bonus())

        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")
