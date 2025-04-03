from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from models.user import User
from utils.auth import verify_password, create_access_token, get_current_user
from models.token import Token  # Importa el modelo de Token
from datetime import datetime, timedelta

router = APIRouter()

@router.post("/")  # Cambio a "/token" para mayor claridad
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await User.find_one(User.email == form_data.username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario no encontrado"
        )
    if not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Contraseña incorrecta"
        )

    # Generar el token de acceso
    access_token = create_access_token({"sub": user.email})

    # Calcular la fecha de expiración si es necesario (por ejemplo, 1 hora)
    expires_at = datetime.utcnow() + timedelta(hours=1)

    # Crear e insertar el token en la colección
    token_entry = Token(
        user_id=str(user.id),  # Asumiendo que `user.id` es un ObjectId, lo convertimos a string
        token=access_token,
        expires_at=expires_at
    )

    # Guardar el token en la base de datos
    await token_entry.insert()

    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/users/me")
async def read_users_me(current_user: dict = Depends(get_current_user)):
    return {"email": current_user.get("sub")}  # Se obtiene correctamente el usuario del token
