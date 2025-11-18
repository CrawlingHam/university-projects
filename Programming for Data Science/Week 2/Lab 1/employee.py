from datetime import datetime

class Employee:
    def __init__(self, name: str, employee_id: str, position: str, salary: float, last_promotion: datetime, date_hired: datetime):
        self.last_promotion = last_promotion
        self.onboarding = OnBoarding(self)
        self.employee_id = employee_id
        self.date_hired = date_hired
        self.position = position
        self.salary = salary
        self.name = name

    def get_details(self) -> None:
        print(f"Name: {self.name}, Employee ID: {self.employee_id}, Position: {self.position}, Salary: {self.salary}")

    def salary_raise(self, percent: float) -> None:
        self.salary = round(self.salary * (1 + percent), 2)

    def start_onboarding(self) -> None:
        self.onboarding.start_onboarding()

    def calculate_bonus(self) -> float:
        return self.salary * 0.05

class OnBoarding:
    def __init__(self, employee: Employee, start_date: datetime = None, status: str = "Pending") -> None:
        self.start_date = start_date if start_date else datetime.now()
        self.employee = employee
        self.status = status

    def start_onboarding(self) -> None:
        self.status = "In Progress"
        print(f"Starting onboarding for {self.employee.name} on {self.start_date}")