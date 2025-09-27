class Signage:
    def __init__(self, content):
        self.content = content

class Theater:
    def __init__(self, name):
        self.name = name
        self.signage = None

    def update_signage(self, signage):
        self.signage = signage

class DigitalSignageManager:
    def __init__(self):  # Fixed __init__ method
        self.signages = {}
        self.theaters = []

    def add_signage(self, signage_id, content):
        if signage_id not in self.signages:
            signage = Signage(content)
            self.signages[signage_id] = signage
            print(f"Signage {signage_id} added successfully.")
        else:
            print("Signage with the same ID already exists.")

    def delete_signage(self, signage_id):
        if signage_id in self.signages:
            del self.signages[signage_id]
            print(f"Signage {signage_id} deleted successfully.")
        else:
            print("Signage not found.")

    def update_signage_content(self, signage_id, new_content):
        if signage_id in self.signages:
            self.signages[signage_id].content = new_content
            print(f"Signage {signage_id} content updated.")
        else:
            print("Signage not found.")

    def add_theater(self, theater_name):
        theater = Theater(theater_name)
        self.theaters.append(theater)
        print(f"Theater '{theater_name}' added successfully.")

    def delete_theater(self, theater_name):
        for theater in self.theaters:
            if theater.name == theater_name:
                self.theaters.remove(theater)
                print(f"Theater '{theater_name}' deleted successfully.")
                return
        print("Theater not found.")

    def update_theater_signage(self, signage_id):
        if signage_id in self.signages:
            for theater in self.theaters:
                theater.update_signage(self.signages[signage_id])
            print(f"Signage {signage_id} updated across all theaters.")
        else:
            print("Signage not found.")

    def track_signage_updates(self, update_data):
        for update in update_data:
            signage_id = update['signage_id']
            new_content = update['new_content']
            self.update_signage_content(signage_id, new_content)

def main():
    signage_manager = DigitalSignageManager()

    while True:
        print("\nDigital Signage Management Menu:")
        print("1. Add Signage")
        print("2. Delete Signage")
        print("3. Update Signage Content")
        print("4. Add Theater")
        print("5. Delete Theater")
        print("6. Update Theater Signage")
        print("7. Track Signage Updates")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            signage_id = input("Enter signage ID: ")
            content = input("Enter signage content: ")
            signage_manager.add_signage(signage_id, content)
        elif choice == "2":
            signage_id = input("Enter signage ID to delete: ")
            signage_manager.delete_signage(signage_id)
        elif choice == "3":
            signage_id = input("Enter signage ID: ")
            new_content = input("Enter new signage content: ")
            signage_manager.update_signage_content(signage_id, new_content)
        elif choice == "4":
            theater_name = input("Enter theater name: ")
            signage_manager.add_theater(theater_name)
        elif choice == "5":
            theater_name = input("Enter theater name to delete: ")
            signage_manager.delete_theater(theater_name)
        elif choice == "6":
            signage_id = input("Enter signage ID to update across theaters: ")
            signage_manager.update_theater_signage(signage_id)
        elif choice == "7":
            update_data = [
                {'signage_id': '1', 'new_content': 'New content for Signage 1'},
                {'signage_id': '2', 'new_content': 'Updated content for Signage 2'},
            ]
            signage_manager.track_signage_updates(update_data)
        elif choice == "8":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":  # Fixed __name__ condition
    main()
