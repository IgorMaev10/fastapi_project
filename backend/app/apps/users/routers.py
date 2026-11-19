# import sentry_sdk
from fastapi import APIRouter, status, Depends, Request, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from apps.users.schemas import CreateUserSchema, UserBaseSchema
from utils.bs_logging import logger
from apps.dependencies.database import get_async_session
from apps.users.crud import user_manager

# logger.error('Something bad happened.')
# logger.info('Log message with structured logging.', extra={
#     'item': "Orange Soda",
#     'price': 100.00
# })

router_users = APIRouter()

@router_users.post('/create', status_code=status.HTTP_201_CREATED)
async def create_user(new_user: CreateUserSchema, session: AsyncSession = Depends(get_async_session)) -> UserBaseSchema:
    """creating users"""
    logger.info(new_user)
    created_user = await user_manager.create_user(new_user, session)
    return created_user