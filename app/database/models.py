from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Float, DateTime
from datetime import datetime, timezone

from app.database.db import Base

class Currency(Base):
    __tablename__ = "currencies"

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(String(10), unique=True, index=True)
    name: Mapped[str] = mapped_column(String(50))

    rates: Mapped[list["Rate"]] = relationship(
        back_populates="currency",
        cascade="all, delete-orphan"
    )



class Rate(Base):
    __tablename__ = "rates"

    id: Mapped[int] = mapped_column(primary_key=True)
    currency_id: Mapped[int] = mapped_column(
        ForeignKey("currencies.id", ondelete="CASCADE"),
        index=True,
    )
    
    value: Mapped[float] = mapped_column(Float)
    created_at: Mapped[datetime] = mapped_column(
    DateTime(timezone=True),
    default=lambda: datetime.now(timezone.utc)
    )

    currency: Mapped["Currency"] = relationship(
        back_populates="rates"
    )