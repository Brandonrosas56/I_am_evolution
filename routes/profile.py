from fastapi import APIRouter
from models.profile import Profile

router = APIRouter()

@router.post("/")
async def create_profile(profile: Profile):
    await profile.insert()  # Corrige el uso de insert()
    return {"message": "Profile created successfully"}
