from flask import Flask, session, redirect, request, render_template, current_app
from model import db, connect_db, User, Post

app = Flask(__name__)

       
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogging_site'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
# app.config['SERVER_NAME']= 'http://localhost:5000'
app.config['SECRET_KEY'] = 'userisactivated'
app.app_context().push()

connect_db(app)

@app.route('/')
def home_page_user_list():
    
    users= User.query.all()
    return render_template('home.html', users=users)

@app.route('/create', methods=['GET'])
def create_new_user():
     
    return render_template('create.html')

@app.route('/create', methods=['POST'])
def create_user():
    
    new_user = User(
    first_name = request.form["first_name"],
    last_name = request.form["last_name"],
    image_url = request.form["image_url"])

    
    db.session.add(new_user)
    db.session.commit()

    return redirect('/')

@app.route('/users/<int:user_id>')
def user_deatials(user_id):
    
    user = User.query.get_or_404(user_id)
    return render_template('posted.html', user=user)

@app.route('/users/<int:user_id>/edit')
def user_edit(user_id):
     user = User.query.get_or_404(user_id)
     return render_template('edit.html',user=user)

@app.route('/users/<int:user_id>/edit', methods=['POST'])
def user_editing(user_id):

    edited_user = User.query.get_or_404(user_id)
    edited_user.first_name = request.form['first_name']
    edited_user.last_name = request.form['last_name']
    edited_user.image_url = request.form['image_url'] or None

    db.session.add(edited_user)
    db.session.commit()

    return redirect('/')

@app.route('/users/<int:user_id>/delete')
def user_delete(user_id):
     delete_user = User.query.get_or_404(user_id)
     db.session.delete(delete_user)
     db.session.commit()

     return redirect('/')
# start of post code/information
@app.route('/users/<int:user_id>/posts/new')
def posts_new_form(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('post.html', user=user)

@app.route('/users/<int:user_id>/posts/new', methods=['POST'])
def posts_new(user_id):
     user = User.query.get_or_404(user_id)
     new_post = Post(title= request.form['title'],
                 content = request.form['content'],
                 user = user)
     db.session.add(new_post)
     db.session.commit()

     return redirect('/')

@app.route('/users/<int:user_id>')
def post_details(user_id):
    user = Post.query.get_or_404(user_id)
    return render_template('detail.html', user=user)


@app.route('/post/<int:user_id>/edit_post')
def make_post(user_id):
     post = Post.query.get_or_404(user_id)
     return render_template('post.html', post=post)


@app.route('/post/<int:user_id>/edit_post')
def make_post_update(user_id):
     edited_post = Post.query.get_or_404(user_id)
     edited_post.title = request.form['title']
     edited_post.content = request.form['content']
     edited_post.created_at = request.form['created_at']

     
     db.session.add(edited_post)
     db.session.commit()

@app.route('/posts/<int:user_id>/delete')
def post_delete(user_id):
     delete_post = User.query.get_or_404(user_id)
     db.session.delete(delete_post)
     db.session.commit()

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)







