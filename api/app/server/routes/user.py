import server.db.user as db
from server.models.user import *
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def hello():
    return {"msg": "Hello World"}


@router.post("/create")
async def create(data: Employees):
    id = db.add_employee(data)
    return {"Inserted": True, "Id": id}

@router.get("/all")
async def get_all():
    data = db.all()
    return {"data": data}

@router.post("/one")
def get_one(emp: Emp):
    res = db.get_one(emp.email)
    return {"Result": res}

@router.delete("/delete")
def delete(emp: Emp):
    res = db.delete(emp.email)
    return {"Delete Status": res}

@router.put("/update")
def update(data: Employees):
    res = db.update(data)
    return {"Update_Status": True,"Update_Count": res}