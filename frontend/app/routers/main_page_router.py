from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get('/')
async def index(request: Request):
    context = {
        "data": 11111111111,
        "page_title": "main page"
    }
    response = templates.TemplateResponse(request=request, name="index.html", context=context)
    return response
