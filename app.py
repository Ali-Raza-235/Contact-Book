from abc import abstractmethod

class ContactBook:
    def __init__(self, name, father_name, email, phone, address):
        self.name = name
        self.father_name = father_name
        self.email = email
        self.phone = phone
        self.address = address

    @abstractmethod
    def __str__(self):
       pass


class PersonalContact(ContactBook):
    def __str__(self):
        return f"***********\n Name: {self.name}, \n Father Name: {self.father_name}, \n Email: {self.email}, \n Contact: {self.phone}, \n Address: {self.address} \n**********"


class BussinessContact(ContactBook):
    def __str__(self):
        return f"***********\n Business Name: {self.name}, \n Contact Person: {self.father_name}, \n Business Email: {self.email}, \n Business Contact: {self.phone}, \n Business Address: {self.address} \n**********"


class ContactBookManagement:
    def __init__(self):
        self.contact_book = []

    def menu(self):
        choose_option = """
        Enter 'a' for add Record Data
        Enter 's' for show Record Data
        Enter 'e' for Edit Record Data
        Enter 'f' for find Record Data
        Enter 'r' for remove Record Data
        Enter 'q' for quit: 
        """

        user_input = input(choose_option)

        while user_input != "q":
            if user_input == "a":
                self.add_record()
            elif user_input == "s":
                self.show_record()
            elif user_input == "e":
                self.edit_record()
            elif user_input == "f":
                self.find_record()
            elif user_input == "r":
                self.remove_record()
            else:
                print("Invalid Input! Please Try Again")
            
            user_input = input(choose_option)

    def add_record(self):
        contact_type = input("Enter 'p' for Personal Contact or 'b' for Business Contact: ").lower()
        name = input("Enter Name: ")
        father_name = input("Enter the Father Name / Contact Person: ")
        email = input("Enter the Email: ")
        phone = input("Enter the Phone Number: ")
        address = input("Enter Address: ")

        if contact_type == 'p':
            record = PersonalContact(name, father_name, email, phone, address)
        elif contact_type == 'b':
            record = BussinessContact(name, father_name, email, phone, address)
        else:
            print("Invalid Contact Type")
            return

        self.contact_book.append(record)

    def show_record(self):
        for record in self.contact_book:
            print(record)

    def edit_record(self):
        search_name = input("Enter the Name of a Person you want to Search: ")
        search_email = input("Enter the Email of a Person you want to Search: ")

        for record in self.contact_book:
            if record.name == search_name or record.email == search_email:
                name = input("Update the Person Name: ")
                father_name = input("Update the Father Name of the Person: ")
                email = input("Update the Email of the Person: ")
                phone = input("Update the Phone Number of the person: ")
                address = input("Update the Address of the Person: ")

                record.name = name
                record.father_name = father_name
                record.email = email
                record.phone = phone
                record.address = address

                print("Record Updated Successfully.")
            
            
            else:
                print("Data Not Found")

    def find_record(self):
        search_name = input("Enter the Name of a Person you want to Search: ")
        search_email = input("Enter the Email of a Person you want to Search: ")

        for record in self.contact_book:
            if record.name == search_name or record.email == search_email:
                print(record)
            
            
            else:
                print("Data Not Found")

    def remove_record(self):
        search_name = input("Enter the Name of a Person you want to Search: ")
        search_email = input("Enter the Email of a Person you want to Search: ")

        for record in self.contact_book:
            if record.name == search_name or record.email == search_email:
                self.contact_book.remove(record)
                print(f" \n Record {record}, \n has been removed Successfully.")

            else:
                print("Data Not Found")




if __name__ == "__main__":
    cbm = ContactBookManagement()
    cbm.menu()