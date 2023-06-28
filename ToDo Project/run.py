from todo_app import db,app
from todo_app.models import Todolist

if __name__=='__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
        for lst in ['Default','Personal','Shopping', 'Wishlist', 'Work']:
            db.session.add(Todolist(name=lst))
        db.session.commit()
    print('done')
    app.run(debug=True)
    
