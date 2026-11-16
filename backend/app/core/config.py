from pathlib import Path
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="HG_", env_file=Path(__file__).resolve().parents[2] / ".env", extra="ignore")
    environment: str = "development"
    cors_origins: list[str] = ["http://localhost:5173", "http://127.0.0.1:5173"]
    db_host: str = ""
    db_port: int = 5432
    db_name: str = "postgres"
    db_user: str = ""
    db_password: SecretStr = SecretStr("")
    db_sslmode: str = "verify-full"
    db_sslrootcert: str = ""
