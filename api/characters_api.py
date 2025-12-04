from fastapi import APIRouter
import services.characters_service as service

router = APIRouter(prefix="/characters")

@router.get("/")
def get_characters():
    return service.get_characters()

@router.get("/{id}")
def get_character(id: int):
    return service.get_character(id)

@router.post("/")
def create_character(data: dict):
    return service.create_character(data)

@router.put("/{id}")
def update_character(id: int, data: dict):
    return service.update_character(id, data)

@router.delete("/{id}")
def delete_character(id: int):
    return service.delete_character(id)
