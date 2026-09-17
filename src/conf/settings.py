from typing import Literal
from pydantic import model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict



class EnvSettings(BaseSettings):
    """Application configuration loaded from enviroment variables and `.env` file

    Attributes are loaded from the .env file at project root
    """

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore'
    )


    HOST: str = "127.0.0.1"
    """The IP address or host interface to bind the Uvicorn ASGI server to."""

    PORT: int = 8000
    """The port number on which the Uvicorn ASGI server listens for requests."""

    RELOAD: bool = False
    """Boolean flag to enable automatic code reloading upon file modifications."""


    DATABASE_URL: str = "sqlite+aiosqlite:///./database_name.db" # للتطوير فقط استخدام النسخة اللمتزامنة من (.db)
    """The async database connection URL"""

    # AsyncEngineSettings
    ECHO: bool = True
    """Whether `SQLAlchemy` should log all SQL statements"""

    ENVIRONMENT: str = 'dev'


    API_PREFIX: str = '/api/v1'

    # AsyncSessionSettings
    AUTO_FLUSH: bool = False
    """Controls `SQLAlchemy` session autoflush behavior"""

    EXPIRE_ON_COMMIT: bool = False
    """Whether to expire all instance after commit"""


    # ———————————————— JWT Settings ————————————————
    # JWT Authentacation
    SECRET_KEY: str = "secret-key-in-production-time-in-this-place"
    """Secret key used for signing `JWT` tokens"""

    REFRESH_SECRET_KEY: str = "refresh-secret-key-in-production-time-in-this-place"
    """Separate secret key used for signing JWT refresh tokens."""

    ALGORITHM: str = 'HS256'
    """Algorithm used for `JWT` encoding"""

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    """Access token expiry duration in minutes"""

    REFRESH_TOKEN_EXPIRE_DAYS: int = 30
    """Refresh token expiry duration in days. Long-lived, revocable."""

    TRIAL_DAYS: int = 3
    # ————————————————————————————————————————————————————

    @model_validator(mode='after')
    def _validate_production_secrets(self) -> "EnvSettings":

        if self.ENVIRONMENT != 'pro':
            return self

        placeholders = {
            'SECRET_KEY': "secret-key-in-production-time-in-this-place",
            'REFRESH_SECRET_KEY': "refresh-secret-key-in-production-time-in-this-place"
        }
        for field_name, placeholder in placeholders.items():
            value: str = getattr(self, field_name)
            if value.startswith(placeholder):
                raise ValueError(
                    f"FATAL: {field_name} contans a placeholder value. "
                    f"Set a real secret in `.env` before running in production mode."
                )

        if self.ECHO:
            raise ValueError(
                "FATAL: `ECHO` must be False in production to prevent SQL statement leaks."
            )

        return self





settings = EnvSettings()