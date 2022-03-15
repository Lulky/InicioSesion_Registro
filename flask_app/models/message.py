


from flask_app.config.mysqlconnection import connectToMySQL
import re #importamos expresiones regulares

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

from flask import flash

class Message:

    def __init__(self, data):
        self.id= data['id']
        self.message_content= data['message_content']
        self.created_at= data['created_at']
        self.updated_at= data['updated_at']
        self.receiver_id= data['receiver_id']
        self.sender_id= data['sender_id']
        
        self.sender = data['sender']
        self.receiver = data['receiver']

    @classmethod
    def save(cls, formulario):
        query ="INSERT INTO messages(message_content, sender_id, receiver_id) VALUES (%(message_content)s, %(sender_id)s, %(receiver_id)s);"
        return connectToMySQL('muro_privado').query_db(query, formulario)

    @classmethod
    def get_user_messages(cls, data):
        query = "SELECT messages.*, users.first_name as sender, users2.first_name as receiver FROM users LEFT JOIN messages ON users.id = messages.sender_id  LEFT JOIN users as users2 ON users2.id = receiver_id WHERE receiver_id = %(id)s"
        results = connectToMySQL('muro_privado').query_db(query, data)
        messages =[]
        for message in results:
            messages.append(cls(message))
        return messages

    @classmethod
    def delete_message(cls, formulario):
        #formulario = {"id": "1"}
        query = "DELETE FROM messages WHERE id = %(id)s;"
        result = connectToMySQL('muro_privado').query_db(query, formulario)
        return result


