from api import app, mongo
from api.models.pet_model import Pet
from api.services import pet_service

if __name__ == "__main__":
    with app.app_context():
        if 'pets' not in mongo.db.list_collection_names():
            pet = Pet(nomePet='', nomeTutor='', diaBanho='')
            pet_service.add_pet(pet)
    app.run(host='localhost', port='5000', debug=True)