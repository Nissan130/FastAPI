from pydantic import BaseModel, EmailStr, field_validator

class Patient(BaseModel):
    name: str 
    email: EmailStr

    #decorator
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com','icici.com']

        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value
    @field_validator('name')
    @classmethod
    def name_validator(cls, value):
        return value.upper()
        




patient_data = {'name': 'Nissan', 'email':'abc@icici.com'}

patient1 = Patient(**patient_data)

def insert_patient_data(patient1: Patient):
    print("Name: ",patient1.name)
    print("Email: ",patient1.email)

insert_patient_data(patient1)