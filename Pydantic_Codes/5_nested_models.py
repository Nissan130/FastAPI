from pydantic import BaseModel

#address model
class Address(BaseModel):
    city: str
    division: str

address_data = {'city': 'Mundumala','division':'Rajshahi'}

address1 = Address(**address_data)

#patient model
class Patient(BaseModel):
    name: str 
    age: int 
    address: Address    #from nested models

patient_data = {'name':'Nissan', 'age':23, 'address': address1}

patient1 = Patient(**patient_data)

def updated_patient_data(patient1: Patient):
    print(patient1)
    print(patient1.address)

updated_patient_data(patient1)


# Benifits of using nested models
#1. Better organization of related data (e.g., vitals, insurance, address)
#2. Reusuability: Use same vitals in multiple models (e.g., patient, medical records etc)
#3. Readibility: Easy to understand for developers and api consumers
#4. Validation: Nested models are automatically validated - no extra works are needed.