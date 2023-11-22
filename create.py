from sqlalchemy import create_engine, Integer, String, Column
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///bank.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)
Session = Session()

class Account(Base):
    __tablename__ = "accounts"
    accno = Column(Integer, primary_key=True)
    name = Column(String, nullable=False,unique=True)
    balance = Column(Integer, nullable=False)
    aadhaar = Column(Integer, nullable=False,unique=True)

    def __str__(self):
        return str({
            "accno":self.accno,
            "name": self.name,
            "balance": self.balance,
            "aadhaar": self.aadhaar
        })

Base.metadata.create_all(engine)