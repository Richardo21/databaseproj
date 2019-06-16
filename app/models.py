from . import db
from sqlalchemy.schema import PrimaryKeyConstraint
# from werkzeug.security import generate_password_hash 


class User(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'User'

    uid = db.Column(db.Integer, primary_key = True)
    uname = db.Column(db.String(30))
    pword = db.Column(db.String(30))
    # account = db.relationship('Account', backref = 'User', uselist=False)
    # account = db.relationship("Account", cascade="save-update")

    def __init__(self, uname, pword):
        self.uname = uname
        self.pword = pword


    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.uid)  # python 2 support
        except NameError:
            return str(self.uid)  # python 3 support

    # def __repr__(self):
    #     return '<User %r>' % (self.username)

class Account(db.Model):

    __tablename__='Account'

    aid = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, db.ForeignKey('User.uid'))
    crdcardno = db.Column(db.Integer)
    # user = db.relationship("User",
    # backref=backref("account", cascade="save-update")
    # )
    
    def __init__(self, uid, crdcardno):
        self.uid = uid
        self.crdcardno = crdcardno

class Item(db.Model):

    __tablename__ = 'Item'
    iid = db.Column(db.Integer, primary_key = True)
    iname = db.Column(db.String(30))
    icost = db.Column(db.Numeric(10,2))
    instore = db.Column(db.String(1))
    online1 = db.Column(db.String(1))

class Customer(db.Model):
    __tablename__ = 'Customer'
    cid = db.Column(db.Integer, primary_key = True)
    fname = db.Column(db.String(30))
    lname = db.Column(db.String(30))
    phone = db.Column(db.String(11))
    addr = db.Column(db.String(30))

class Branch(db.Model):
    __tablename__= 'Branch'
    branch_id = db.Column(db.Integer, primary_key=True)
    branch_name = db.Column(db.String(30))
    blocation = db.Column(db.String(30))

class Warehouse(db.Model):
    __tablename__='Warehouse'
    wid = db.Column(db.Integer, primary_key=True)
    wlocation = db.Column(db.String(30))

class Buy(db.Model):
    __tablename__='Buy'
    cid = db.Column(db.Integer,db.ForeignKey('Customer.cid'))
    iid = db.Column(db.Integer,db.ForeignKey('Item.iid'))

    __table_args__ = (
        PrimaryKeyConstraint('cid', 'iid'),
        {},)

    branch_id = db.Column(db.Integer, db.ForeignKey('Branch.branch_id'))
    quantity = db.Column(db.Integer)
    p_date = db.Column(db.String(10))

class Located_At(db.Model):
    __tablename__ ='Located_At'
    iid = db.Column(db.Integer,db.ForeignKey('Item.iid'))
    branch_id = db.Column(db.Integer, db.ForeignKey('Branch.branch_id'))
    __table_args__ = (
        PrimaryKeyConstraint('iid', 'branch_id'),
        {},)
    amount_in_store = db.Column(db.Integer)

    










    