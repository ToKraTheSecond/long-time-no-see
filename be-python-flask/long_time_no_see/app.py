import time
import os
from dataclasses import dataclass

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from dotenv import load_dotenv

from long_time_no_see.statistics import summarize

time.sleep(5) # wait for db service

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{os.getenv("POSTGRES_USER")}:{os.getenv("POSTGRES_PASSWORD")}@db:5432/{os.getenv("POSTGRES_DB")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@dataclass
class Encounter(db.Model):
    __tablename__ = "encounters"
    person_id:int = Column(Integer, primary_key=True, autoincrement=True)
    person:str = Column(String(255))
    date_of_meeting:str = Column(String(255))
    what_we_did:str = Column(String(255))

@app.route('/')
def hello():
    return jsonify(message="Hello, nothing to see here!")

@app.route('/records', methods=['POST'])
def add_record():
    data = request.get_json()
    db.session.add(Encounter(
        person=data['person'],
        date_of_meeting=data['date_of_meeting'],
        what_we_did=data['what_we_did']
    ))
    db.session.commit()
    return jsonify({'message': 'Record added successfully'})

@app.route('/records/<int:person_id>', methods=['GET'])
def get_record(person_id):
    record = Encounter.query.get(person_id)
    if record:
        return jsonify(record)
    return jsonify({'message': 'Record not found'})

@app.route('/records', methods=['GET'])
def get_records():
    result = Encounter.query.all()
    return jsonify(result)

@app.route('/records/summary', methods=['GET'])
def get_records_summary():
    records = Encounter.query.all()
    return jsonify(summarize(records))

@app.route('/records/<int:person_id>', methods=['PUT'])
def update_record(person_id):
    '''
    Updates whole record
    '''
    record = Encounter.query.get(person_id)
    if record:
        data = request.get_json()
        record.person=data['person'],
        record.date_of_meeting=data['date_of_meeting'],
        record.what_we_did=data['what_we_did']
        db.session.commit()
        return jsonify({'message': 'Record updated successfully'})
    else:
        return jsonify({'message': 'Record not found'})

@app.route('/records/<int:record_id>', methods=['DELETE'])
def delete_record(record_id):
    record = Encounter.query.get(record_id)
    if record:
        db.session.delete(record)
        db.session.commit()
        return jsonify({'message': 'Record deleted successfully'})
    return jsonify({'message': 'Record not found'})

if __name__ == '__main__':
    app.run(debug=True)