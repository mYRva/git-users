
from flask import render_template, url_for, flash, redirect, request, abort
from flaskr import app, db
from flaskr.models import users
from flaskr.seed import Seed

@app.before_first_request
def create_tables():
     db.create_all()
     
     arr = []
     arr = Seed.get_git_users(150, 150)
      
     for item in arr:    
        new_user = users(id=item[0], login=item[1],avatar_url=item[2], tipo=item[3], profile_url=item[4])
        db.session.add(new_user)
     
     db.session.commit()

     
@app.route('/git')    
def git():       
    
    headings = ['id','login','avatar', 'type', 'profile']

    page = request.args.get('page', 1, type=int)
    user = users.query.paginate(page=page, per_page=25)
    print(user)

    return render_template("table.html", headings=headings, data = user.items) 