from dataclasses import dataclass
from views.employees.schemas import Employee


@dataclass
class EmployeeStorage:
    last_id: int = 0
    employees: dict[int : Employee]  =  {}
