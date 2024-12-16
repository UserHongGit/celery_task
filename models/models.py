# # models/models.py
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import create_engine
# from base_config import DataSourceConfig
#
# Base = declarative_base()
#
# class MyModel(Base):
#     __tablename__ = 'my_table'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50), nullable=False)
#
# engine = create_engine(DataSourceConfig.SQLALCHEMY_DATABASE_URI)
# Session = sessionmaker(bind=engine)
