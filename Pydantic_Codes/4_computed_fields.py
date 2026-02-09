from pydantic import BaseModel, EmailStr, computed_field
from typing import Dict

class Patient(BaseModel):
    name: str 
    email: EmailStr
    age: int
    weight: float 
    height: float 
    contact_details: Dict[str, str]

    #decorator
    @computed_field
    @property
    def bmi(self)->float:
        return round((self.weight/self.height**2),2)
        

patient_data = {'name': 'Nissan', 'email':'abc@icici.com','age':'20','weight':60,'height':1.7, 'contact_details':{'phone':'12345'}}

patient1 = Patient(**patient_data)

def insert_patient_data(patient1: Patient):
    print("Name: ",patient1.name)
    print("Email: ",patient1.email)
    print("BMI: ", patient1.bmi)

insert_patient_data(patient1)