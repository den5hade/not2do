from typing import Optional
from models.user_model import User



class UserService:
    @staticmethod
    async def create_user(user):
        user_in = User(
            username=user.username,
            email=user.email,
            hashed_password=user.password
        )
        await user_in.save()
        return user_in
    
    @staticmethod
    async def get_user_by_email(email: str) -> Optional[User]:
        user = await User.find_one(User.email == email)
        return user