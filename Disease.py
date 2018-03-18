from mongoengine import *

class Disease(Document):
    name = StringField(required=True, unique=True, max_length=30)
    pd = IntField(required=True)
    cli = IntField(required=True)
    loc = IntField(required=True)
    symptoms = ListField(StringField(max_length=30))

    # def __str__(self):
    #     return self.name