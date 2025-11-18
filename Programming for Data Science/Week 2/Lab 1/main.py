from datetime import datetime
from employee import Employee
from company import Company
from manager import Manager

jack_jackson = Employee("Jack Jackson", "1234567890", "Security Analyst", 100000, datetime(2021, 1, 1), datetime(2019, 1, 1))
jessica_jones = Employee("Jessica Jones", "1234567891", "Software Engineer", 120000, datetime(2022, 1, 1), datetime(2020, 1, 1))
diana_diane = Employee("Diana Diane", "1234567892", "Data Analyst", 120000, datetime(2022, 1, 1), datetime(2020, 1, 1))

lebron_micheal = Employee("Lebron Micheal", "1234567895", "Senior Sales Representative", 150000, datetime(2023, 1, 1), datetime(2021, 1, 1))
caicedo_silva = Employee("Caicedo Silva", "1234567896", "Junior Sales Representative", 100000, datetime(2024, 1, 1), datetime(2022, 1, 1))
emily_emily = Employee("Emily Emily", "1234567897", "Sales consultant", 100000, datetime(2024, 1, 1), datetime(2022, 1, 1))

john_johnson = Manager("John Johnson", "1234567898", "District Manager", 200000, datetime(2022, 1, 1), datetime(2018, 1, 1), [jack_jackson, jessica_jones], "Sales")
shane_shaneson = Manager("Shane Shaneson", "1234567899", "Product Manager", 250000, datetime(2023, 1, 1), datetime(2019, 1, 1), [lebron_micheal], "Product Management")
elena_elena = Manager("Elena Elena", "1234567900", "Compliance and Risk Manager", 250000, datetime(2023, 1, 1), datetime(2019, 1, 1), [diana_diane], "Compliance and Risk Management")

ceo = Manager("CEO Smith", "1234567901", "Chief Executive Officer", 500000, datetime(2020, 1, 1), datetime(2015, 1, 1), [john_johnson, shane_shaneson, elena_elena], "Executive")

company = Company("Kompany Inc", [jack_jackson, jessica_jones, lebron_micheal, caicedo_silva, emily_emily, diana_diane], ceo, 300000000, 500000000)

jack_jackson.get_details()
john_johnson.get_details()

new_employee = Employee("Conner Ryan", "1234567902", "Junior Developer", 80000, datetime(2024, 6, 1), datetime(2024, 6, 1))
company.add_employee(new_employee, "1234567899") 
print(f"Added {new_employee.name} under manager {shane_shaneson.name}")

new_manager = Manager("Rafael Mendes", "1234567903", "Operations Manager", 180000, datetime(2024, 1, 1), datetime(2023, 1, 1), [], "Operations")
company.add_employee(new_manager, "1234567901") 
print(f"Added {new_manager.name} under CEO")

company.remove_employee(new_employee)
print(f"Removed {new_employee.name} from company")

company.remove_employee(new_manager)
print(f"Removed {new_manager.name} from company (subordinates transferred)")

print("\n Company ")
company.list_employees()
company.calculate_company_salary()