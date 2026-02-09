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


#convert models into dictionary and export
# export_data = patient1.model_dump()

#convert models into json and export
# export_data = patient1.model_dump_json()

#convert models into dictionary and export specific keys
# export_data = patient1.model_dump(include=['name'])
export_data = patient1.model_dump(exclude=['name'])

print(export_data)
print(type(export_data))
