from sqlalchemy import (
    Column,
    Integer,
    Text,
    ForeignKey
)
from sqlalchemy.orm import relationship

from ..core import Base


class UserGroup(Base):
    __tablename__ = "user_group"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    group_id = Column(Integer, ForeignKey("groups.id"), primary_key=True)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    tg_name = Column("telegram_name", Text, nullable=False)
    username = Column("username", Text, nullable=False)

    groups = relationship("Group", secondary="user_group", back_populates="users")

class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, nullable=False)
    groupname = Column("group_name", Text, nullable=False)

    users = relationship("User", secondary="user_group", back_populates="groups")