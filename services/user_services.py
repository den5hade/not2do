from typing import Optional
from models.user_model import User



class UserService:
    @staticmethod
    async def create_user(user):
        user_in = User(**user.dict())
        await user_in.insert()
        return user_in
    
    @staticmethod
    async def get_user_by_telegram_id(telegram_id: str) -> Optional[User]:
        user = await User.find_one(User.telegram_id == telegram_id)
        return user