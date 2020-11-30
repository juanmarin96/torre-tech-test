from typing import Generator

from fastapi import Depends, HTTPException, status
from pydantic import ValidationError
from sqlalchemy.orm import Session

import crud
import models
from database.session import SessionLocal


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
