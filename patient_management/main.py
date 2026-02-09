from fastapi import FastAPI
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
def view_patient(patient_id: str):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    else:
        return {'error':'Patient not found'}