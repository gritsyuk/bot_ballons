from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    TG_BOT_TOKEN: str
    TG_BOT_UNAME: str
    TG_CHANEL_DELIVERIES_ID: str
    TG_CHANEL_ADMINS_ID: str
    DB_SPREAD_SHEET_ID: str
    DB_SHEET_NAME: str
    GOOGLE_CREDENTIALS_FILE: str = "ballons-413121-cadbf533f328.json"
    GG_CALENDAR_URL: str
    IS_LOOK_CALENDAR: bool = False

    model_config = SettingsConfigDict(env_file=".env")

config = Settings()