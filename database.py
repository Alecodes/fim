from peewee import *
from os import path
njia_yetu = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(njia_yetu, "writer.db"))

class Writer(Model):
    firstName = CharField()
    secondName = CharField()
    phone = CharField()
    email = CharField()
    class Meta:
        database = db

class OrderDetails(Model):
    owner = ForeignKeyField(Writer, related_name ="persons")
    fName = CharField()
    orderID = CharField()
    pageNumbers=IntegerField()
    CPP =IntegerField()
    description=CharField()
    class Meta:
        database = db

Writer.create_table(fail_silently = True)
OrderDetails.create_table(fail_silently = True)


OrderDetails.create(owner =1,fName="Anthony",orderID="7676768668",pageNumbers="7",CPP="250",description="annotated bib")





Writer.create(firstName="John", secondName="John", phone="072344556", email="johjnbxbu@gmail.com")