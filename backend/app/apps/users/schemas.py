from pydantic import BaseModel, Field, EmailStr

class UserPasswordSchema(BaseModel):
    password: str = Field(min_length=8)

class UserBaseSchema(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    email: EmailStr = Field(description="Email address")

class IDSchema(BaseModel):
    id: int = Field(gt=0)

class CreateUserSchema(UserPasswordSchema, UserBaseSchema):
    pass
