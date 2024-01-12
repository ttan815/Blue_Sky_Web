from unicodedata import category
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

database_menu = [
    {
        'APPETIZER' : [
            ['Fried Prawns', '$9.95', {'Spicy' : ''}, {'Count' : '6'}],
            ['Egg Rolls', '$8.25', {'Spicy' : ''}, {'Count' : '4'}],
            ['Pot Stickers', '$8.95', {'Spicy' : ''}, {'Count' : '6'}],
            ['Crispy Chicken Wings', '$10.25,', {'Spicy' : ''}, {'Count' : '6'}],
            ['Foil Wrapped Chicken', '$9.25', {'Spicy' : ''}, {'Count' : '6'}],
            ["Wok's Combination Platter (Egg Roll, Fried Prawns, Cream Cheese Wanton, Foil Wrapped Chicken)", '$13.25,', {'Spicy' : ''}],
        ],

        'SOUPS' : [
            ['Sizzling Rice Soup', [{'Small (2-3)' : '$9.50', 'Medium (3-5)' : '$11.95', 'Large (6-8)' : '$14.95', 'Spicy' : ''}], {'Spicy' : ''}],
            ['Hot & Sour Soup', [{'Small (2-3)' : '$8.50', 'Medium (3-5)' : '$10.95', 'Large (6-8)' : '$12.95', 'Spicy' : ''}], {'Spicy' : ''}],
            ['Wonton Soup', [{'Small (2-3)' : '$8.50', 'Medium (3-5)' : '$10.95', 'Large (6-8)' : '$12.95', 'Spicy' : ''}], {'Spicy' : ''}],
            ['Egg Flower Soup', [{'Small (2-3)' : '$8.50', 'Medium (3-5)' : '$10.95', 'Large (6-8)' : '$12.95', 'Spicy' : ''}], {'Spicy' : ''}],
            ['Wor Wonton Soup', [{'Small (2-3)' : '$9.50', 'Medium (3-5)' : '$11.95', 'Large (6-8)' : '$14.95', 'Spicy' : ''}], {'Spicy' : ''}],
        ],
        
        'PORK' : [
            ['Cherry Pork', '$11.25', {'Spicy' : ''}],
            ['Sweet & Sour Pork', '$11.25', {'Spicy' : ''}],
            ['B.B.Q. Pork w/ Vegetables)', '$11.25', {'Spicy' : ''}],
            ['Sweet & Sour Spareribs', '$11.25', {'Spicy' : ''}],
            ['Salt & Pepper Spareribs', '$11.25', {'Spicy' : '🌶️'}],
        ],

        'HOUSE SPECIAL' : [
            ['Sesame Chicken', '$13.25', {'Spicy' : '🌶️'}],
            ['Mandarin Chicken', '$13.25', {'Spicy' : '🌶️'}],
            ['Honey Walnut Chicken', '$13.25', {'Spicy' : ''}],
            ["General Tso's Chicken", '$13.25', {'Spicy' : ''}],
            ['Honey Walnut Prawns', '$15.95', {'Spicy' : ''}],
            ['Salt & Pepper Prawns', '$15.25', {'Spicy' : '🌶️'}],
            ['House Special Spareibs', '$15.95', {'Spicy' : ''}],
            ['String Bean Deluxe', '$15.95', {'Spicy' : ''}],
        ],

        'POULTRY' : [
            ['Almond or Cashew Chicken', '$13.25', {'Spicy' : ''}],
            ['Kung Pao Chicken', '$13.25', {'Spicy' : ''}],
            ['Chicken with Broccoli', '$13.25', {'Spicy' : ''}],
            ['Sweet & Sour Chicken', '$13.25', {'Spicy' : ''}],
            ['Chicken w/ Mixed Vegetables', '$13.25', {'Spicy' : ''}],
            ['Curry Chicken', '$13.25', {'Spicy' : ''}],
            ['Szechuan Chicken', '$13.25', {'Spicy' : ''}],
            ['Chicken w/ Spicy Garlic Sauce', '$13.25', {'Spicy' : ''}],
            ['Lemon Chicken', '$13.25', {'Spicy' : ''}],
            ['Chicken in Black Bean Sauce', '$13.25', {'Spicy' : ''}],
            ['Orange Chicken', '$13.25', {'Spicy' : ''}],
            ['Chicken with Mushroom', '$13.25', {'Spicy' : ''}],
            ['Mongolian Chicken', '$13.25', {'Spicy' : ''}],
            ['Green Bean Chicken', '$13.25', {'Spicy' : ''}],
        ],

        'SIZZLING PLATES' : [
            ['Sizzling Chicken', '$13.25', {'Spicy' : ''}],
            ['Sizzling Beef', '$13.25', {'Spicy' : ''}],
            ['Sizzling Shrimp', '$14.95', {'Spicy' : ''}],
            ['Sizzling Bean Curd & Vegetables', '$13.25', {'Spicy' : ''}],
        ],

        'BEEF' : [
            ['Broccoli Beef', '$11.75', {'Spicy' : ''}],
            ['Mongolian Beef', '$11.75', {'Spicy' : '🌶️'}],
            ['Beef w/ Mixed Vegetables', '$$11.75', {'Spicy' : ''}],
            ['Snow Peas', '$11.75', {'Spicy' : ''}],
            ['Kung Pao Beef', '$11.75', {'Spicy' : '🌶️'}],
            ['Hunan Spicy Sauce Beef', '$11.75', {'Spicy' : '🌶️'}],
            ['Curry Beef', '$11.75', {'Spicy' : '🌶️'}],
            ['Szechuan Beef', '$11.75', {'Spicy' : '🌶️'}],
            ['Oyster Sauce Beef', '$11.75', {'Spicy' : ''}],
            ['Beef w/ Bean Curd', '$11.75', {'Spicy' : ''}],
            ['Beef w/ Green Onion', '$11.75', {'Spicy' : ''}],
            ['Beef w/ Green Pepper', '$11.75', {'Spicy' : ''}],
            ['Green Bean Beef', '$11.75', {'Spicy' : ''}],
        ],

        'VEGETABLE / TOFU' : [
            ['Mixed Vegetable Deluxe', '$10.50', {'Spicy' : ''}],
            ['Fried Bean Curd in Spicy Sauce', '$10.50', {'Spicy' : '🌶️'}],
            ['Braised Bean Curd w/ Vegetables', '$10.50', {'Spicy' : ''}],
            ['Dry Braised Green Beans', '$10.50', {'Spicy' : '🌶️'}],
            ['Broccoli in Spicy Garlic Sauce', '$10.50', {'Spicy' : '🌶️'}],
        ],

        'SEAFOOD' : [
            ['Kung Pao Prawns', '$10.50', {'Spicy' : '🌶️'}],
            ['Sweet & Sour Prawns', '$10.50', {'Spicy' : '🌶️'}],
            ['Prawns w/ Cashew Nuts', '$10.50', {'Spicy' : ''}],
            ['Prawns w/ Snow Peas', '$10.50', {'Spicy' : ''}],
            ['Prawns w/ Mixed Vegetables', '$10.50', {'Spicy' : ''}],
            ['Szechuan Prawns', '$10.50', {'Spicy' : '🌶️'}],
            ['Prawns w/ Black Bean Sauce', '$10.50', {'Spicy' : ''}],
            ['Prawns in Spicy Garlic Sauce', '$10.50', {'Spicy' : '🌶️'}],
        ],



    }
]

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///menu.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=True)
    category = db.Column(db.String(250), nullable=True)
    is_it_spicy = db.Column(db.String(250), nullable=True)
    count = db.Column(db.Integer, nullable=True)

list_of_all_menu_groups = [
    'APPETIZER', 'SOUPS', 'PORK', 'HOUSE SPECIAL', 'POULTRY', 'SIZZLING PLATES', 'BEEF', 'VEGETABLE / TOFU', 'SEAFOOD'
]
with app.app_context():
    db.create_all()

for i in (list_of_all_menu_groups):
    for each_item in database_menu[0][i]:
        if i == 'APPETIZER':
            the_appetizer = each_item[0]
            the_price = each_item[1]
            is_it_spicy = each_item[2]['Spicy']
            try:
                how_many_pieces = each_item[3]['Count']
            except:
                how_many_pieces = None
            new_menu_item = Menu(name=the_appetizer, category=i, is_it_spicy=is_it_spicy, count=how_many_pieces)
            with app.app_context():
                db.session.add(new_menu_item)
                db.session.commit()
        elif i == 'SOUPS':
            the_soup = each_item[0]
            the_price = each_item[1]
            is_it_spicy = each_item[2]['Spicy']
            new_menu_item = Menu(name=the_soup, category=i, is_it_spicy=is_it_spicy, count=how_many_pieces)
            with app.app_context():
                db.session.add(new_menu_item)
                db.session.commit()
        elif i == 'PORK':
            the_pork = each_item[0]
            the_price = each_item[1]
            is_it_spicy = each_item[2]['Spicy']
            new_menu_item = Menu(name=the_pork, category=i, is_it_spicy=is_it_spicy, count=how_many_pieces)
            with app.app_context():
                db.session.add(new_menu_item)
                db.session.commit()
        elif i == 'HOUSE SPECIAL':
            the_house_special = each_item[0]
            the_price = each_item[1]
            is_it_spicy = each_item[2]['Spicy']
            new_menu_item = Menu(name=the_house_special, category=i, is_it_spicy=is_it_spicy, count=how_many_pieces)
            with app.app_context():
                db.session.add(new_menu_item)
                db.session.commit()
        elif i == 'POULTRY':
            the_poultry = each_item[0]
            the_price = each_item[1]
            is_it_spicy = each_item[2]['Spicy']
            new_menu_item = Menu(name=the_poultry, category=i, is_it_spicy=is_it_spicy, count=how_many_pieces)
            with app.app_context():
                db.session.add(new_menu_item)
                db.session.commit()
        elif i == 'SIZZLING PLATES':
            the_sizzling_plates = each_item[0]
            the_price = each_item[1]
            is_it_spicy = each_item[2]['Spicy']
            new_menu_item = Menu(name=the_sizzling_plates, category=i, is_it_spicy=is_it_spicy, count=how_many_pieces)
            with app.app_context():
                db.session.add(new_menu_item)
                db.session.commit()
        elif i == 'BEEF':
            the_beef = each_item[0]
            the_price = each_item[1]
            is_it_spicy = each_item[2]['Spicy']
            new_menu_item = Menu(name=the_beef, category=i, is_it_spicy=is_it_spicy, count=how_many_pieces)
            with app.app_context():
                db.session.add(new_menu_item)
                db.session.commit()
        elif i == 'VEGETABLE / TOFU':
            the_vege_tofu = each_item[0]
            the_price = each_item[1]
            is_it_spicy = each_item[2]['Spicy']
            new_menu_item = Menu(name=the_vege_tofu, category=i, is_it_spicy=is_it_spicy, count=how_many_pieces)
            with app.app_context():
                db.session.add(new_menu_item)
                db.session.commit()
        elif i == 'SEAFOOD':
            the_seafood = each_item[0]
            the_price = each_item[1]
            is_it_spicy = each_item[2]['Spicy']
            new_menu_item = Menu(name=the_seafood, category=i, is_it_spicy=is_it_spicy, count=how_many_pieces)
            with app.app_context():
                db.session.add(new_menu_item)
                db.session.commit()