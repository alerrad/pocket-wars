import typing
import requests


class APIHandler:
    @staticmethod
    def get_warrior(username: str) -> typing.Dict:
        pass
    
    @staticmethod
    def get_completed(username: str) -> list[typing.Dict]:
        pass
    
    @staticmethod
    def get_badge(username: str) -> str:
        return f'https://www.codewars.com/users/{username}/badges/large'

    @staticmethod
    def get_random() -> typing.Dict:
        ## INACCESSIBLE until the api gets updated
        pass