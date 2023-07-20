from ..core import session
from ..models import User, Group


class DB_handler():
    @staticmethod
    def add_user(user_id: int, username: str, tg_name: str) -> bool:
        pass

    @staticmethod
    def get_user_by_Id(user_id: int) -> dict:
        pass

    @staticmethod
    def get_group_leaderboard(group_id: int) -> list:
        pass

    @staticmethod
    def remove_user_from_group_leaderboard(user_id: int, group_id: int) -> bool:
        pass