from employee import Employee

class Evaluation:
    def __init__(self, evaluation_type: str = "General", evaluator_name: str = "System"):
        self.evaluation_type = evaluation_type
        self.evaluator_name = evaluator_name

    def evaluate_budget(self, budget: float, expenses: float) -> None:
        if expenses > budget:
            print("Expenses are higher than budget")
        else:
            print("Expenses are lower than budget")

    def evaluate_revenue(self, projected_revenue: float, revenue: float) -> None:
        if revenue > projected_revenue:
            print("Revenue is higher than projected revenue")
        else:
            print("Revenue is lower than projected revenue")

    def evaluate_employee(self, employee: Employee) -> None:
        print(f"Evaluating employee: {employee.name} (Type: {self.evaluation_type}, Evaluator: {self.evaluator_name})")
        