"""arquivo contendo as classes Admin e Post"""

import uuid
from typing import Any

from pydantic import BaseModel, Field


class Project(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    title: str
    short_description: str
    full_description: str | None
    post_date: str | Any = None
    authors: str | dict
    is_deleted: bool = False

    class Config:
        allow_population_by_field_name = True
        # it allows you to populate model fields using their field names in addition to any field aliases
        schema_extra = {
            "example": {
                "id": "00010203-0405-0607-0809-0a0b0c0d0e0f",
                "tile": "My important task",
                "short_description": "full stack project using <stack name>.",
                "full_description": "Full description of the project",
                "post_date": "yyyy-mm-dd",
                "authors": "author name or list of names",
                "is_deleted": "True for soft deletion, false is default",
            }
        }


class Admin(BaseModel):
    user_name: str
    password: str  # TODO: implementar hashing
    name: str
    contact_info: dict  # Json contendo telefone, Linkedin, email
