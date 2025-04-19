from datetime import datetime
from fastapi import APIRouter
from fastapi.responses import HTMLResponse


counter_router = APIRouter()


@counter_router.get("/{name}", response_class=HTMLResponse)
async def counter_email(name: str):
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    loog_string = f"{name} : {current_date}"
    with open('opened.txt', 'a') as file:
        file.write(loog_string + '\n')
    return True