from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Base class for database models
Base = declarative_base()

class TradeLog(Base):
    """
    A class representing the trade log table schema.
    """
    __tablename__ = 'trade_logs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    symbol = Column(String, nullable=False)
    action = Column(String, nullable=False)
    quantity = Column(Float, nullable=False)
    price = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<TradeLog(symbol={self.symbol}, action={self.action}, quantity={self.quantity}, price={self.price}, timestamp={self.timestamp})>"

class AccountBalance(Base):
    """
    A class representing the account balance table schema.
    """
    __tablename__ = 'account_balances'

    id = Column(Integer, primary_key=True, autoincrement=True)
    balance = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<AccountBalance(balance={self.balance}, timestamp={self.timestamp})>"

# Database setup
DATABASE_URL = 'sqlite:///trading_system.db'  # Replace with your preferred database URL
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
