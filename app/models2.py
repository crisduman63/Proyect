from sqlalchemy import Boolean

class SoftDeleteMixin:
    is_deleted = Column(Boolean, default=False)

    @classmethod
    def filter_not_deleted(cls, query):
        return query.filter(cls.is_deleted == False)

class User(SoftDeleteMixin, Base):
    # Resto del modelo User...

# Se aplica el mismo mixin a los demás modelos que necesiten soft delete
