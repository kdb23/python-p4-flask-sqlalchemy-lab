#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = Animal.query.filter(Animal.id == id). first()

    if not animal:
        response_body = '<h1>404 animal not found</h1>'
        response = make_response(response_body, 404)
        return response
    
    response_body = f'''
        <h1>Information for {animal.name}</h1>
        <h2>Animal Species is {animal.species}</h2>
        <h2>Animal Zookeeper is {animal.zookeeper.name}</h2>
        <h2>Animal Enclosure is {animal.enclosure.environment}</h2>
    '''

    response = make_response(response_body, 200)

    return response

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.filter(Zookeeper.id == id).first()

    if not zookeeper:
        response_body = '<h1>404 zookeeper not found</h1>'
        response = make_response(response_body, 404)
        return response
    
    response_body = f'<h1>Information for {zookeeper.name}, birthday {zookeeper.birthday}</h1>'

    animals = [animal for animal in zookeeper.animals]

    if not animals:
        response_body += f'<h2> Has no Animals at this time</h2>'

    else:
        for animal in animals:
            response_body += f'<h2>Has Animal {animal.name}</h2> '

    response = make_response(response_body, 200)

    return response

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.filter(Enclosure.id == id).first()

    if not enclosure:
        response_body = '<h1>404 enclosure not found</h1>'
        response = make_response(response_body, 404)
        return response
    
    response_body = f'<h1> Information for {enclosure.environment}, Open to Visitors {enclosure.open_to_visitors}</h1>'

    animals = [animal for animal in enclosure.animals]

    if not animals:
        response_body += f'<h2> Has no Animals at this time</h2>'

    else:
        for animal in animals:
            response_body += f'<h2>Has Animal {animal.name}</h2> '

    response = make_response(response_body, 200)

    return response


if __name__ == '__main__':
    app.run(port=5555, debug=True)
