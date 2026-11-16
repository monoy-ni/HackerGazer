from alembic import context
from app.db.base import Base
from app.db.session import get_engine
if context.is_offline_mode():
    raise RuntimeError("Offline migration requires an explicitly configured dialect workflow")
with get_engine().connect() as connection:
    context.configure(connection=connection, target_metadata=Base.metadata)
    with context.begin_transaction():
        context.run_migrations()
