from flask import Flask, render_template, request, redirect, session

from flask_app import app
from flask_app.models.user import User
from flask_app.models.message import Message

@app.route('/send_message', methods=['POST'])
def send_message():
    if 'user_id' not in session:
        return redirect('/')
    #todos los formularios se recieven con request.form['KEY'] ESTO ES POR LEY
    
    Message.save(request.form)
    return redirect('/wall')

@app.route('/eliminar/mensaje/<int:id>')
def delete_message():

    data = {
        "id": id
    }
    Message.delete_message(data)
    return redirect ('/wall')