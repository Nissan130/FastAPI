from fastapi import FastAPI, Path, HTTPException, Query
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal
from fastapi.responses import JSONResponse
import json

app = FastAPI()

#create a pydantic model to perform the data validation
class Patient(BaseModel):
    id: Annotated[str, Field(..., description='Id of the patient', example='P001')]
    name: Annotated[str, Field(..., description='Enter the name of the patient.', example='full name')]
    city: Annotated[str, Field(..., description='Enter the city where the patient live in.', example='Rajshahi')]
    age: Annotated[int, Field(..., gt=0, lt=150, description='Enter the current age of the patient. Age should be under 150', example='20')]
    gender: Annotated[Literal['Male','Female','Other'], Field(..., description='Enter the gender of the patient.', example='e.g., Male') ]
    height: Annotated[float, Field(..., gt=0, description='Height of the patient in centemeter', example='1.74')]
    weight: Annotated[float, Field(..., gt=0, description='Weight of the patient in kilograms.', example='55')]

    #calculate the bmi using height and weight
    @computed_field
    @property
    def bmi(self)->float:
        return round(self.weight/ (self.height**2),2)
    
    #calculate the verdict based on the bmi
    @computed_field
    @property
    def verdict(self)->str:
        if self.bmi < 18.5:
            return 'underweight'
        elif self.bmi < 25:
            return 'healthy weight'
        elif self.bmi < 30:
            return 'overweight'
        else:
            return 'obese'
    

#function to load data
def load_data():
    with open("patients.json",'r') as f:
        data = json.load(f)
    return data 

#save data function
def save_data(data):
    with open('patients.json','w') as f:
         json.dump(data, f)
        

@app.get("/")
def hello():
    return {"message":"Patient management system api"}

@app.get("/about")
def about():
    return {"message":"A fully functional api to manage patient's records"}

@app.get("/view")
def view():
    data = load_data()
    return data

#find specific patient
@app.get("/view_patient/{patient_id}")
def view_patient(patient_id: str=Path(..., description='Patient ID in the DB', example='P001')):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    else:
        raise HTTPException(status_code = 404, detail="Patient is not found.")

@app.get("/sort")
def sort_patients(sort_by: str=Query(..., description='Sort patient by weight, height or bmi'), order_by=Query('asc',description='Oder patient either asc or desc')):
    
    valid_sorts = ['weight','height','bmi']

    if sort_by not in valid_sorts:
        raise HTTPException(status_code=400, detail='Invalid sort by selection. Select from weight,height and bmi')
    if order_by not in ['asc','desc']:
        raise HTTPException(status_code=400, detail='Invalid oder selection. Select between asc and desc')
    
    data = load_data()

    order = True if order_by=='desc' else False

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by,0), reverse=order)

    return sorted_data


# create patient api
@app.post('/create')
def create_patient(patient: Patient):
    #load the existing data
    data = load_data()

    #check if the new patient already exists or not
    if patient.id in data:
        raise HTTPException(status_code=400, detail='Patient already exists.')
    
    #insert new data
    data[patient.id] = patient.model_dump(exclude='id')

    #save the data
    save_data(data)

    return JSONResponse(status_code=201, content={'message':'Patient created successfully.'})



