from flask import Flask, request, jsonify
from bson.json_util import dumps
from bson.objectid import ObjectId
import db
from flask_cors import CORS
 
app = Flask(__name__)
CORS(app)

@app.route("/movies/<code>", methods=['GET'])
def get_movie(code):
    con = db.get_connection()
    dbmov = con.dbmovies
    try:
        movies = dbmov.movies
        response = app.response_class(
            response=dumps(movies.find_one({'_id': ObjectId(code)})),
            status=200,
            mimetype='application/json'
        )
        return response
    finally:
        con.close()
        print("Connection closed")

@app.route("/movies", methods=['GET'])
def get_movies():
    con = db.get_connection()
    dbmov = con.dbmovies
    try:
        movies = dbmov.movies
        response = app.response_class(
            response=dumps(
                movies.find()
            ),
            status=200,
            mimetype='application/json'
        )
        return response
    finally:
        con.close()
        print("Connection closed")

@app.route("/movies", methods=['POST'])
def create():
    data = request.get_json() #Sacar datos en formato json
    con = db.get_connection() #se crea la conexión
    dbmov = con.dbmovies  #asociar la colección a la base de datos
    try:
        movies = dbmov.movies
        movies.insert_one(data) #insertar el objeto json en la base de datos
        return jsonify({"message":"OK"})
    finally:
        con.close()
        print("Connection closed")

@app.route("/vacantes/<code>", methods=['PUT'])
def update(code):
    data = request.get_json()
    con = db.get_connection()
    dbmov = con.dbmovies
    try:
        vacantes = dbmov.vacantes
        vacantes.replace_one(
            {'_id': ObjectId(code)},
            data, True
        )
        return jsonify({"message":"OK"})
    finally:
        con.close()
        print("Connection closed")

@app.route("/vacantes/<code>", methods=['DELETE'])
def delete_vacantes(code):
    con = db.get_connection()
    dbmov = con.dbmovies
    try:
        vacantes = dbmov.vacantes
        vacantes.delete_one({'_id': ObjectId(code)})
        return jsonify({"message":"OK"})
    finally:
        con.close()
        print("Connection closed")



@app.route("/vacantes", methods=['GET'])
def get_allvacantes():
    con = db.get_connection()
    dbmov = con.dbmovies
    try:
        vacantes = dbmov.vacantes #nombre de la colección
        response = app.response_class(
            response=dumps(vacantes.find()),
            status=200,
            mimetype='application/json'
        )
        return response
    finally:
        con.close()
        print("Connection closed")








@app.route("/vacantes/<code>", methods=['GET'])
def get_vacantes(code):
    con = db.get_connection()
    dbmov = con.dbmovies
    try:
        vacantes = dbmov.vacantes #nombre de la colección
        response = app.response_class(
            response=dumps(vacantes.find_one({'_id': ObjectId(code)})),
            status=200,
            mimetype='application/json'
        )
        return response
    finally:
        con.close()
        print("Connection closed")


@app.route("/vacantes", methods=['POST'])
def create_vacantes():
    data = request.get_json() #Sacar datos en formato json
    con = db.get_connection() #se crea la conexión
    dbmov = con.dbmovies  #asociar la colección a la base de datos
    try:
        vacantes = dbmov.vacantes
        vacantes.insert_one(data) #insertar el objeto json en la base de datos
        return jsonify({"message":"OK"})
    finally:
        con.close()
        print("Connection closed")
