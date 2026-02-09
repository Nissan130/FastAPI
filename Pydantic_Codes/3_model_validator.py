from pydantic import BaseModel, EmailStr, model_validator
from typing import Dict

class Patient(BaseModel):
    name: str 
    email: EmailStr
    age: int
    contact_details: Dict[str, str]

    #decorator
    @model_validator(mode='after')
    @classmethod
    def validate_emegency_contact(cls, model):
        if model.age >60 and 'emergency' not in model.contact_details:
            raise ValueError('Since age is greater than 60, so an emerygency contact number must be added')
        return model
        




patient_data = {'name': 'Nissan', 'email':'abc@icici.com','age':'20', 'contact_details':{'phone':'12345'}}

patient1 = Patient(**patient_data)

def insert_patient_data(patient1: Patient):
    print("Name: ",patient1.name)
    print("Email: ",patient1.email)

insert_patient_data(patient1)