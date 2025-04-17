from fastapi import APIRouter
from fastapi.responses import HTMLResponse


counter_router = APIRouter()


@counter_router.get("/{name}", response_class=HTMLResponse)
async def counter_email(name: str):
    with open('opened.txt', 'a') as file:
        file.write(name + '\n')
    return True