from dataclasses import dataclass
from typing import Optional
from views.employees.schemas import Employee, EmployeeCreate
from pydantic import Field


@dataclass
class EmployeeStorage:
    last_id: int = 0
    employees: dict[int:Employee] = Field(default_factory=dict)

    @property
    def next_id(self) -> int:
        self.last_id += 1
        return self.last_id

    def create_employee(
        self,
        employee_create: EmployeeCreate,
    ) -> Employee:
        employee = Employee(
            id=self.next_id,
            **employee_create.model_dump(),
        )
        self.employees[employee.id] = employee
        return employee

    def get_employee(self) -> list[Employee]:
        return list(self.employees.values())

    def get_employee_by_id(
        self,
        employee_id: int,
    ) -> Optional[Employee]:
        return self.employees.get(employee_id)

    def delete_employee(self, employee_id: int) -> None:
        self.employees.pop(employee_id, None)


storage = EmployeeStorage()
