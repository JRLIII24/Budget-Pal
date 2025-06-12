from typing import List # Used for type hinting: indicates a relationship returns a list of objects
from datetime import datetime # Used for type hinting: indicates a column stores datetime objects
from enum import Enum 
from sqlalchemy import ForeignKey, String, Float, DateTime # Import SQL data types
from sqlalchemy.orm import Mapped, mapped_column, relationship # Key ORM components for mapping
from sqlalchemy.sql import func # Used for SQL functions like func.now()

from database import Base # Import our declarative base from database.py

class BudgetFrequency(str, Enum):
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    YEARLY = "yearly"


class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(200), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)

    budgets: Mapped[List["Budget"]] = relationship(back_populates="owner")



class Budget(Base):
    __tablename__ = "budgets"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255), index=True, nullable=False)

    total_amount : Mapped[float] = mapped_column(Float, default=0.0)

    frequency: Mapped[BudgetFrequency] = mapped_column(String, nullable=False, default=BudgetFrequency.MONTHLY)


    creation_date: Mapped[datetime] = mapped_column(DateTime, default=func.now())

    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    owner: Mapped["User"] = relationship(back_populates="budgets")

    categories: Mapped[List["BudgetCategory"]] = relationship(back_populates="budget", cascade="all, delete-orphan")

class BudgetCategory(Base):

    __tablename__ = "budget_categories"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    category_name: Mapped[str] = mapped_column(String(255), nullable=False)
    budgeted_amount: Mapped[float] = mapped_column(Float, nullable=False)

    budget_id: Mapped[int] = mapped_column(ForeignKey("budgets.id"))

    budget: Mapped["Budget"] = relationship(back_populates="categories")

