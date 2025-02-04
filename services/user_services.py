from typing import Optional
from models.user_model import User



class UserService:
    @staticmethod
    async def create_user(user):
        user_in = User(
            username=user.username,
            telegram_id=user.telegram_id,
            phone_number=user.phone_number
        )
        await user_in.save()
        return user_in
    
    @staticmethod
    async def get_user_by_telegram_id(telegram_id: int) -> Optional[User]:
        user = await User.find_one(User.telegram_id == telegram_id)
        return user