# import sentry_sdk
from fastapi import APIRouter, status
from apps.users.schemas import CreateUserSchema, UserBaseSchema
from utils.bs_logging import logger

# logger.error('Something bad happened.')
# logger.info('Log message with structured logging.', extra={
#     'item': "Orange Soda",
#     'price': 100.00
# })

router_users = APIRouter()

@router_users.post('/create', status_code=status.HTTP_201_CREATED)
async def create_user(new_user: CreateUserSchema) -> UserBaseSchema:
    """creating users"""
    logger.info(new_user)
    return new_user