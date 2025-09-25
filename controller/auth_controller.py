from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from decouple import config
from datetime import timedelta
from core.auth import create_access_token, verify_password, get_password_hash, ACCESS_TOKEN_EXPIRE_MINUTES



router = APIRouter(prefix="/auth", tags=["Auth"])

# Usuário fake (poderia vir do banco)
fake_user = {
    "username": config("USER_NAME_LOGIN"),
    "hashed_password": get_password_hash(config("PASSWORD_LOGIN"))
}

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username != fake_user["username"] or not verify_password(form_data.password, fake_user["hashed_password"]):
        raise HTTPException(status_code=400, detail="Usuário ou senha inválidos")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(data={"sub": fake_user["username"]}, expires_delta=access_token_expires)
    return {"access_token": token, "token_type": "bearer"}
