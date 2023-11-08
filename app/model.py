from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    __abstract__ = True


class Test(Base):
    __tablename__ = 'Test'

    id: Mapped[int] = mapped_column(primary_key=True, unique=True, index=True)
    name: Mapped[str] = mapped_column(unique=True)