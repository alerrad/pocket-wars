import typing
import requests


class API_handler:
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
        # Maybe come up with something for this route: https://www.codewars.com/api/v1/code-challenges/{challenge}
        pass