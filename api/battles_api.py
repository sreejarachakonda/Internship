from fastapi import APIRouter
import services.battles_service as service

router = APIRouter(prefix="/battles")

@router.get("/")
def get_battles():
    return service.get_battles()

@router.get("/{id}")
def get_battle(id: int):
    return service.get_battle(id)

@router.post("/")
def create_battle(data: dict):
    return service.create_battle(data)

@router.put("/{id}")
def update_battle(id: int, data: dict):
    return service.update_battle(id, data)

@router.delete("/{id}")
def delete_battle(id: int):
    return service.delete_battle(id)
