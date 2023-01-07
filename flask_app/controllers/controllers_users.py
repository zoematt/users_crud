from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.model_user import User
from flask_app.config.mysqlconnection import connectToMySQL

@app.route('/show')
def index():
    users = User.getall_users()
    return render_template('readall.html', users=users)

@app.route('/')
def user_form():
    return render_template('create.html')

@app.route('/create_user', methods=['POST'])
def create_user():
    User.create(request.form)
    return redirect('/show')

@app.route('/getone_user/<int:user_id>')
def getone_user(user_id):
    data={"id": user_id}
    users = User.get_one(data)
    return render_template('show_user.html', user=users)

#Edit User
@app.route('/edit/<int:user_id>')
def edit_user(user_id):
    data={"id": user_id}
    users = User.get_one(data)
    return render_template('edit_user.html', user=users)

@app.route('/edit_user/<int:user_id>',methods=['POST'])
def user_edit(user_id):
    User.edit_user(request.form, user_id)
    return redirect(f'/getone_user/{user_id}')

@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    data= {"id": user_id}
    User.delete_user(data)
    return redirect('/')


 




