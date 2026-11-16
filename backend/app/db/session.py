from functools import lru_cache
from sqlalchemy import URL, create_engine
from app.core.config import Settings

@lru_cache
def get_engine():
    s = Settings()
    if not s.db_host or not s.db_user or not s.db_password.get_secret_value():
        raise RuntimeError("Database configuration incomplete")
    args = {"connect_timeout": 5, "sslmode": s.db_sslmode}
    if s.db_sslrootcert:
        args["sslrootcert"] = s.db_sslrootcert
    url = URL.create("postgresql+psycopg", host=s.db_host, port=s.db_port, database=s.db_name,
                     username=s.db_user, password=s.db_password.get_secret_value())
    return create_engine(url, connect_args=args, pool_pre_ping=True, pool_size=3, max_overflow=2)
