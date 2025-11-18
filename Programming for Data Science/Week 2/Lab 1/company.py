from evaluation import Evaluation
from employee import Employee
from manager import Manager

class Company:
    def __init__(self, name: str, employees: list[Employee], general_manager: Manager, annual_budget: float, annual_revenue: float):
        self.evaluation = Evaluation("Company Evaluation", "HR Department")
        self.general_manager = general_manager
        self.annual_revenue = annual_revenue
        self.annual_budget = annual_budget
        self.employees = employees
        self.name = name

    def add_employee(self, employee: Employee, manager_id: str) -> None:
        # Check if adding to general manager
        if self.general_manager.employee_id == manager_id:
            if not isinstance(employee, Manager):
                raise ValueError("Only managers can be added directly under the general manager")
            self.general_manager.add_subordinate(employee)
            if employee not in self.employees:
                self.employees.append(employee)
            return
        
        # Find appropriate manager
        for manager in self.general_manager.subordinates:
            if manager.employee_id == manager_id:
                manager.add_subordinate(employee)
                if employee not in self.employees:
                    self.employees.append(employee)
                return
        raise ValueError(f"Manager with ID {manager_id} not found")

    def remove_employee(self, employee: Employee) -> None:
        manager_found = None
        if isinstance(employee, Manager) and employee in self.general_manager.subordinates:
            manager_found = self.general_manager
        else:
            for manager in self.general_manager.subordinates:
                if employee in manager.subordinates:
                    manager_found = manager
                    break
        
        if not manager_found:
            raise ValueError(f"Employee {employee.name} not found")
        
        # If removing a manager, transfer subordinates to another manager
        if isinstance(employee, Manager):
            other_managers = [m for m in self.general_manager.subordinates if m != employee]
            if other_managers:
                other_managers[0].subordinates.extend(employee.subordinates)
            else:
                for sub in employee.subordinates:
                    if sub in self.employees:
                        self.employees.remove(sub)
        
        manager_found.remove_subordinate(employee)
        if employee in self.employees:
            self.employees.remove(employee)

    def list_employees(self) -> list[Employee]:
        print(f"Employees: {[employee.name for employee in self.employees]}, Managers: {[manager.name for manager in self.general_manager.subordinates]}, General Manager: {self.general_manager.name}")
        return self.employees

    def evaluate_budget(self, expenses: float) -> None:
        self.evaluation.evaluate_budget(self.annual_budget, expenses)

    def evaluate_revenue(self, revenue: float) -> None:
        self.evaluation.evaluate_revenue(self.annual_revenue, revenue)

    def calculate_company_salary(self) -> float:
        regular_employees = [emp for emp in self.employees if not isinstance(emp, Manager)]
        managers = [manager for manager in self.general_manager.subordinates]
        company_salary = sum([emp.salary for emp in regular_employees]) + sum([manager.salary for manager in managers]) + self.general_manager.salary
        print(f"Company salary: {company_salary}")
        return company_salary