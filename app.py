import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task_name = request.form['task']
        if task_name:
            new_task = Task(name=task_name)
            db.session.add(new_task)
            db.session.commit()
        return redirect(url_for('index'))
    else:
        tasks = Task.query.all()
        return render_template('index.html', tasks=tasks)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000, debug=True)
