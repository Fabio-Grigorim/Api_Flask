from flask_restful import Resource
from api import api
from ..schemas import pet_schemas
from ..models import pet_model
from ..services import pet_service
from flask import make_response, jsonify, request

class PetList(Resource):
    def get(self):
        pets = pet_service.get_pet()
        g = pet_schemas.PetSchema(many=True)
        return make_response(g.jsonify(pets), 200)
    
    def post(self):
        g = pet_schemas.PetSchema()
        validate = g.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400) #Código 400:
            #(BAD REQUEST) : Solicitação inválida ou malformada
        else:
            nomePet = request.json["nomePet"]
            nomeTutor = request.json["nomeTutor"]
            diaBanho = request.json["diaBanho"]

            new_pet = pet_model.Pet(nomePet=nomePet, nomeTutor=nomeTutor, diaBanho=diaBanho)
            result = pet_service.add_pet(new_pet)
            res = g.jsonify(result)
            return make_response(res, 201) #Código 201 (CREATED): Criação bem-sucedida de um novo recurso


class PetDetails(Resource):
    def get(self, id):
        pet = pet_service.get_pet_by_id(id)
        if pet is None:
            return make_response(jsonify("Pet não foi encontrado"), 400)
        g = pet_schemas.PetSchema()
        return make_response(g.jsonify(pet),200)
    
    def put(self, id):
        pet_bd = pet_service.get_pet_by_id(id)
        if pet_bd is None:
            return make_response(jsonify("Pet não foi encontrado"), 404)
        g = pet_schemas.PetSchema()
        validate = g.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 404)
        else:
            nomePet = request.json["nomePet"]
            nomeTutor = request.json["nomeTutor"]
            diaBanho = request.json["diaBanho"]
            new_pet = pet_model.Pet(nomePet=nomePet, nomeTutor=nomeTutor, diaBanho=diaBanho)
            pet_service.update_pet(new_pet, id)
            updated_pet = pet_service.get_pet_by_id(id)
            return make_response(g.jsonify(updated_pet), 200)
        
    def delete(self, id):
        pet_bd = pet_service.get_pet_by_id(id)
        if pet_bd is None:
            return make_response(jsonify("Pet não encontrado"), 404) # NOT FOUND
        pet_service.delete_pet(id)
        return make_response(jsonify("Pet excluido com sucess!"), 204) #Código 204 (NO CONTENT): Indica que a requisição foi bem sucedida, mas não há retorno de conteúdo

    
api.add_resource(PetList, '/pet')
api.add_resource(PetDetails, '/pet/<id>')

        