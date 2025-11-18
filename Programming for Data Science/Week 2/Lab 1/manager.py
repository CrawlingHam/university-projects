from evaluation import Evaluation
from datetime import datetime
from employee import Employee
from meeting import Meeting

class Manager(Employee):
    def __init__(self, name: str, employee_id: str, position: str, salary: float, last_promotion: datetime, date_hired: datetime, subordinates: list[Employee], department: str, reports: list[Employee] = []):
        super().__init__(name, employee_id, position, salary, last_promotion, date_hired)
        self.evaluation = Evaluation("Manager Evaluation", name)
        self.meetings: list[dict[list[str], Meeting]] = []
        self.subordinates = subordinates
        self.department = department
        self.reports = reports

    def schedule_meeting(self, meeting: Meeting, attendees: list[str]) -> None:
        meeting_dict: dict[list[str], Meeting] = {
            "attendees": attendees,
            "meeting": meeting
        }
        self.meetings.append(meeting_dict)

    def add_subordinate(self, employee: Employee) -> None:
        self.subordinates.append(employee)

    def remove_subordinate(self, employee: Employee) -> None:
        self.subordinates.remove(employee)

    def get_subordinates(self) -> list[Employee]:
        return self.subordinates

    def get_details(self) -> None:
        print(f"Name: {self.name}, Employee ID: {self.employee_id}, Position: {self.position}, Salary: {self.salary}")
        print(f"Subordinates: {[employee.name for employee in self.subordinates]}")

    def evaluate_employee(self, employee: Employee) -> None:
        self.evaluation.evaluate_employee(employee)

    def calculate_bonus(self) -> float:
        return super().calculate_bonus() + sum([employee.salary for employee in self.subordinates]) * 0.01
