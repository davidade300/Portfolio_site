"""arquivo contendo as classes Admin e Post"""

from typing import Any

from pydantic import BaseModel


class Project(BaseModel):
    id: int
    title: str
    short_description: str
    full_description: str | None
    post_date: str | Any = None
    authors: str | dict
    is_deleted: bool = False


class Admin(BaseModel):
    user_name: str
    password: str  # TODO: implementar hashing
    name: str
    contact_info: dict  # Json contendo telefone, Linkedin, email
