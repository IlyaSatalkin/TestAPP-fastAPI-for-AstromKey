from pydantic import BaseModel


class EmployeeBase(BaseModel):
    full_name: str
    email: str
    
class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int
    


