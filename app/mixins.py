from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func

class SoftDeleteMixin:
    is_deleted = Column(DateTime, nullable=True)

    @classmethod
    def filter_deleted(cls, query):
        return query.filter(cls.is_deleted == None)

class TimestampMixin:
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())