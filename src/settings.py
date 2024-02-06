from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    TG_BOT_TOKEN: str = ""
    TG_BOT_UNAME: str = ""
    TG_CHANEL_DELIVERIES_ID: str
    TG_CHANEL_ADMINS_ID: str = ""
    DB_SPREAD_SHEET_ID: str
    DB_SHEET_NAME: str = "Ответы на форму (1)"
    GOOGLE_CREDENTIALS_FILE: str = "ballons-413121-cadbf533f328.json"

    model_config = SettingsConfigDict(env_file=".env")

config = Settings()