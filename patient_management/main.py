from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

#function to load data
def load_data():
    with open("patients.json",'r') as f:
        data = json.load(f)
    return data 
        

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

