from tortoise import fields, models 
from tortoise.contrib.pydantic import pydantic_model_creator 

class Users(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)

    class Meta:
        table = 'users'

    def __str__(self):
        return self.name

class Items(models.Model):
    id = fields.IntField(pk=True)
    item = fields.CharField(max_length=255)
    owner = fields.ForeignKeyField('models.Users', related_name='owner')

    def __str__(self):
        return self.name

UserSchema = pydantic_model_creator(Users, name="User")
ItemSchema = pydantic_model_creator(Items)

UserInSchema = pydantic_model_creator(Users, name="UserIn", exclude_readonly=True)


