from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.characters_api import router as characters_router
from api.kingdoms_api import router as kingdoms_router
from api.battles_api import router as battles_router

app = FastAPI(title="Mahabharata API")

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(characters_router)
app.include_router(kingdoms_router)
app.include_router(battles_router)
