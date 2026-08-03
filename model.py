from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import Uuid, func
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(AsyncAttrs, DeclarativeBase):
    pass

class Todos(Base):
    __tablename__ = "todos"

    id: Mapped[UUID] = mapped_column(Uuid,primary_key=True,default=uuid4)
    content: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())
    is_done: Mapped[bool] = mapped_column(default=False)