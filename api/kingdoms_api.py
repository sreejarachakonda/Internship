from fastapi import APIRouter
import services.kingdoms_service as service

router = APIRouter(prefix="/kingdoms")

@router.get("/")
def get_kingdoms():
    return service.get_kingdoms()

@router.get("/{id}")
def get_kingdom(id: int):
    return service.get_kingdom(id)

@router.post("/")
def create_kingdom(data: dict):
    return service.create_kingdom(data)

@router.put("/{id}")
def update_kingdom(id: int, data: dict):
    return service.update_kingdom(id, data)

@router.delete("/{id}")
def delete_kingdom(id: int):
    return service.delete_kingdom(id)
