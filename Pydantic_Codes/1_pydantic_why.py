from pydantic import BaseModel, EmailStr,AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient less than 50 character')]
    email: EmailStr
    linkedin_url: AnyUrl
    age: Annotated[int, Field(gt=0, lt=60, description='Give the patient age between 0 to 60')]
    weight: Annotated[float, Field(gt = 0, strict=True)]
    married: bool = False
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

patient_data = {'name':'Md. Nissan Ali','email': 'abc@gmail.com','age':"30", 'linkedin_url':'https://linkedin.com','weight':72.2,'contact_details': {'phone': '1234'}}

patient1 = Patient(**patient_data)

def insert_patient_data(patient1: Patient):
    print("Name: ",patient1.name)
    print("Age: ",patient1.age)
    print("Married: ", patient1.married)
    print("Allergies: ", patient1.allergies)
    print("Contact Details: ",patient1.contact_details)
    print("Inserted")

def update_patient_data(patient1: Patient):
    print("Name: ",patient1.name)
    print("Age: ",patient1.age)
    print("Married: ", patient1.married)
    print("Allergies: ", patient1.allergies)
    print("Contact Details: ",patient1.contact_details)
    print("Updated")

update_patient_data(patient1)
