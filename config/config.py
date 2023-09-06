import os
from dataclasses import dataclass
from dotenv import load_dotenv
from .base import getenv, ImproperlyConfigured



@dataclass
class TelegramBotConfig:
    token: str


@dataclass
class Config:
    tg_bot: TelegramBotConfig


def load_config() -> Config:
    load_dotenv()
    API_TOKEN = os.getenv('BOT_TOKEN')
    return Config(tg_bot=TelegramBotConfig(token=API_TOKEN))
