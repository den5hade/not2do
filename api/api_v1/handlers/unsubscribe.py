from fastapi import APIRouter


unsubscribe_router = APIRouter()


@unsubscribe_router.get("/{name}")
async def add_email_to_list(name: str):
    with open('emails.txt', 'a') as file:
        file.write(name + '\n')
    return {"message": "Email added to list"}
