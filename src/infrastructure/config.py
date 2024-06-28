from typing import Dict

from dotenv import load_dotenv
import os


class Config:
    def __init__(self, database_url):
        self.database_url = database_url


def load_environment() -> Config:
    load_dotenv()

    database_url = os.getenv('DATABASE_URL')

    return Config(database_url)

