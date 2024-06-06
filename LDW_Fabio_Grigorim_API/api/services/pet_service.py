from api import mongo
from ..models import pet_model
from bson import ObjectId

def add_pet(pet):
    mongo.db.pets.insert_one({
        'nomePet' : pet.nomePet,
        'nomeTutor' : pet.nomeTutor,
        'diaBanho' : pet.diaBanho
    })

@staticmethod
def get_pet():
    return list(mongo.db.pets.find())

@staticmethod
def get_pet_by_id(id):
    return mongo.db.pets.find_one({'_id': ObjectId(id)})

def update_pet(self, id):
    mongo.db.pets.update_one({'_id': ObjectId(id)},
                              {'$set':{
                                  'nomePet': self.nomePet,
                                  'nomeTutor': self.nomeTutor,
                                  'diaBanho': self.diaBanho
                              }})
    
@staticmethod
def delete_pet(id):
    mongo.db.pets.delete_one({'_id': ObjectId(id)})