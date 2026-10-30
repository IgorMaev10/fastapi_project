from fastapi import APIRouter, status
from apps.users.schemas import CreateUserSchema, UserBaseSchema

router_users = APIRouter()

@router_users.post('/create', status_code=status.HTTP_201_CREATED)
async def create_user(new_user: CreateUserSchema) -> UserBaseSchema:
    """creating users"""
    return new_user