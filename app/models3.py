class TimestampMixin:
    created_at = Column(func.now())
    updated_at = Column(func.now(), onupdate=func.now())

class User(TimestampMixin, SoftDeleteMixin, Base):
    # Resto del modelo User...
