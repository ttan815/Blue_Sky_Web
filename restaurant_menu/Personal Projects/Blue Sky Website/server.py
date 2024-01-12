from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from sqlalchemy import or_

app = Flask(__name__)
Bootstrap5(app)
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


# MENU IDEA: WHEN A PERSON SEARCHES AN ITEM, SEARCH AND FILTER FOR THE ITEM, IF MULTIPLE SHOW UP,
#APPEND EACH ITEM AND THEIR CONTENTS INTO A LIST AND APPEND THAT INTO A BIGGER LIST
#FOR LOOP THROUGH THE LIST, AND FIND FOR KEY WORDS REGARDING THE CATEGORY, WHERE IT'LL THROW THE LIST OF JUST THE ITEM INTO THE RIGHT CATEGORY
#WHICH WILL BE PRINTED OUT ONTO THE SCREEN NORMALLY.
list_of_all_menu_groups = [
    'APPETIZER', 'SOUPS', 'PORK', 'HOUSE SPECIAL', 'POULTRY', 'SIZZLING PLATES', 'BEEF', 'VEGETABLE / TOFU', 'SEAFOOD'
]

list_of_appetizers = []
list_of_soups = []
list_of_pork = []
list_of_house_special = []
list_of_poultry = []
list_of_sizzling_plates = []
list_of_beef = []
list_of_vege_tofu = []
list_of_seafood = []

list_to_hold_selected_items = []

class ContactForm(FlaskForm):
    style={'style': 'width:200%; height:50%;'}
    first_name = StringField('First Name', validators=[DataRequired()], render_kw=style)
    last_name = StringField('Second Name', validators=[DataRequired()], render_kw=style)
    submit = SubmitField('Submit')


with app.app_context():
    db.create_all()
    the_menu = db.session.query(Menu).all()

class SearchMenu(FlaskForm):
    search_query = StringField(validators=[DataRequired()])
    submit_query = SubmitField('Submit')

@app.route('/')
def home():
    return render_template('home_screen.html')

@app.route('/menu/', methods=['GET','POST'])
def menu():
    form = SearchMenu()
    if request.method == 'GET':
        list_of_appetizers.clear()
        list_of_soups.clear()
        list_of_pork.clear()
        list_of_house_special.clear()
        list_of_poultry.clear()
        list_of_sizzling_plates.clear()
        list_of_beef.clear()
        list_of_vege_tofu.clear()
        list_of_seafood.clear()
        'APPETIZER', 'SOUPS', 'PORK', 'HOUSE SPECIAL', 'POULTRY', 'SIZZLING PLATES', 'BEEF', 'VEGETABLE / TOFU', 'SEAFOOD'
        a_number = 15
        for each_menu_item in the_menu:
            if each_menu_item.category == 'APPETIZER':
                a_list = [each_menu_item.name, {'Spicy' : each_menu_item.is_it_spicy}, {'Count' : each_menu_item.count}]
                print(type(a_list[2]['Count']))
                if type(a_list[2]['Count']) != type(a_number):
                    a_list[2]['Count'] = 'Not Applicable'
                list_of_appetizers.append(a_list)
            elif each_menu_item.category == 'SOUPS':
                a_list = [each_menu_item.name, {'Spicy' : each_menu_item.is_it_spicy}, {'Count' : each_menu_item.count}]
                list_of_soups.append(a_list)
            elif each_menu_item.category == 'PORK':
                a_list = [each_menu_item.name, {'Spicy' : each_menu_item.is_it_spicy}, {'Count' : each_menu_item.count}]
                list_of_pork.append(a_list)
            elif each_menu_item.category == 'HOUSE SPECIAL':
                a_list = [each_menu_item.name, {'Spicy' : each_menu_item.is_it_spicy}, {'Count' : each_menu_item.count}]
                list_of_house_special.append(a_list)
            elif each_menu_item.category == 'POULTRY':
                a_list = [each_menu_item.name, {'Spicy' : each_menu_item.is_it_spicy}, {'Count' : each_menu_item.count}]
                list_of_poultry.append(a_list)
            elif each_menu_item.category == 'SIZZLING PLATES':
                a_list = [each_menu_item.name, {'Spicy' : each_menu_item.is_it_spicy}, {'Count' : each_menu_item.count}]
                list_of_sizzling_plates.append(a_list)
            elif each_menu_item.category == 'BEEF':
                a_list = [each_menu_item.name, {'Spicy' : each_menu_item.is_it_spicy}, {'Count' : each_menu_item.count}]
                list_of_beef.append(a_list)
            elif each_menu_item.category == 'VEGETABLE / TOFU':
                a_list = [each_menu_item.name, {'Spicy' : each_menu_item.is_it_spicy}, {'Count' : each_menu_item.count}]
                list_of_vege_tofu.append(a_list)
            elif each_menu_item.category == 'SEAFOOD':
                a_list = [each_menu_item.name, {'Spicy' : each_menu_item.is_it_spicy}, {'Count' : each_menu_item.count}]
                list_of_seafood.append(a_list)
        return render_template('menu.html', form=form,
                                appetizer = list_of_appetizers, soup = list_of_soups, 
                                pork = list_of_pork, house_special = list_of_house_special, 
                                poultry = list_of_poultry, sizzling_plates = list_of_sizzling_plates, 
                                beef = list_of_beef, vege_tofu = list_of_vege_tofu, 
                                seafood = list_of_seafood)
    
    elif request.method =='POST':
        list_of_appetizers.clear()
        list_of_soups.clear()
        list_of_pork.clear()
        list_of_house_special.clear()
        list_of_poultry.clear()
        list_of_sizzling_plates.clear()
        list_of_beef.clear()
        list_of_vege_tofu.clear()
        list_of_seafood.clear()
        list_to_hold_selected_items.clear()
        searched_item = request.form['item_searched']
        if searched_item == '':
            list_of_appetizers.clear()
            list_of_soups.clear()
            list_of_pork.clear()
            list_of_house_special.clear()
            list_of_poultry.clear()
            list_of_sizzling_plates.clear()
            list_of_beef.clear()
            list_of_vege_tofu.clear()
            list_of_seafood.clear()
            a_number = 15
            for each_menu_item in the_menu:
                a_number = 15
                if each_menu_item.category == 'APPETIZER':
                    a_list = [each_menu_item.name, {'Spicy' : each_menu_item.is_it_spicy}, {'Count' : each_menu_item.count}]
                    print(type(a_list[2]['Count']))
                    if type(a_list[2]['Count']) != type(a_number):
                        a_list[2]['Count'] = 'Not Applicable'
                    list_of_appetizers.append(a_list)
                elif each_menu_item.category == 'SOUPS':
                    a_list = [each_menu_item.name, {'Spicy' : each_menu_item.is_it_spicy}, {'Count' : each_menu_item.count}]
                    list_of_soups.append(a_list)
                elif each_menu_item.category == 'PORK':
                    a_list = [each_menu_item.name, {'Spicy' : each_menu_item.is_it_spicy}, {'Count' : each_menu_item.count}]
                    list_of_pork.append(a_list)
                elif each_menu_item.category == 'HOUSE SPECIAL':
                    a_list = [each_menu_item.name, {'Spicy' : each_menu_item.is_it_spicy}, {'Count' : each_menu_item.count}]
                    list_of_house_special.append(a_list)
                elif each_menu_item.category == 'POULTRY':
                    a_list = [each_menu_item.name, {'Spicy' : each_menu_item.is_it_spicy}, {'Count' : each_menu_item.count}]
                    list_of_poultry.append(a_list)
                elif each_menu_item.category == 'SIZZLING PLATES':
                    a_list = [each_menu_item.name, {'Spicy' : each_menu_item.is_it_spicy}, {'Count' : each_menu_item.count}]
                    list_of_sizzling_plates.append(a_list)
                elif each_menu_item.category == 'BEEF':
                    a_list = [each_menu_item.name, {'Spicy' : each_menu_item.is_it_spicy}, {'Count' : each_menu_item.count}]
                    list_of_beef.append(a_list)
                elif each_menu_item.category == 'VEGETABLE / TOFU':
                    a_list = [each_menu_item.name, {'Spicy' : each_menu_item.is_it_spicy}, {'Count' : each_menu_item.count}]
                    list_of_vege_tofu.append(a_list)
                elif each_menu_item.category == 'SEAFOOD':
                    a_list = [each_menu_item.name, {'Spicy' : each_menu_item.is_it_spicy}, {'Count' : each_menu_item.count}]
                    list_of_seafood.append(a_list)
            return render_template('menu.html', form=form,
                                    appetizer = list_of_appetizers, soup = list_of_soups, 
                                    pork = list_of_pork, house_special = list_of_house_special, 
                                    poultry = list_of_poultry, sizzling_plates = list_of_sizzling_plates, 
                                    beef = list_of_beef, vege_tofu = list_of_vege_tofu, 
                                    seafood = list_of_seafood)
        search_results = db.session.query(Menu).filter(or_(Menu.name.like(f'%{searched_item}%'))).all()
        for i in search_results:
            list_to_hold_selected_items.append(i.name)
        
        for each_item in list_to_hold_selected_items:
            a_number = 15
            the_food_item = Menu.query.filter_by(name=f'{each_item}')
            for each_menu_item in the_food_item:
                if each_menu_item.category == 'APPETIZER':
                    a_list = [each_menu_item.name, {'Spicy' : each_menu_item.is_it_spicy}, {'Count' : each_menu_item.count}]
                    try:
                        if type(a_list[2]['Count']) != type():
                            a_list[2]['Count'] = 'Not Applicable'
                    except:
                        pass
                    list_of_appetizers.append(a_list)
                elif each_menu_item.category == 'SOUPS':
                    a_list = [each_menu_item.name, {'Spicy' : each_menu_item.is_it_spicy}, {'Count' : each_menu_item.count}]
                    list_of_soups.append(a_list)
                elif each_menu_item.category == 'PORK':
                    a_list = [each_menu_item.name, {'Spicy' : each_menu_item.is_it_spicy}, {'Count' : each_menu_item.count}]
                    list_of_pork.append(a_list)
                elif each_menu_item.category == 'HOUSE SPECIAL':
                    a_list = [each_menu_item.name, {'Spicy' : each_menu_item.is_it_spicy}, {'Count' : each_menu_item.count}]
                    list_of_house_special.append(a_list)
                elif each_menu_item.category == 'POULTRY':
                    a_list = [each_menu_item.name, {'Spicy' : each_menu_item.is_it_spicy}, {'Count' : each_menu_item.count}]
                    list_of_poultry.append(a_list)
                elif each_menu_item.category == 'SIZZLING PLATES':
                    a_list = [each_menu_item.name, {'Spicy' : each_menu_item.is_it_spicy}, {'Count' : each_menu_item.count}]
                    list_of_sizzling_plates.append(a_list)
                elif each_menu_item.category == 'BEEF':
                    a_list = [each_menu_item.name, {'Spicy' : each_menu_item.is_it_spicy}, {'Count' : each_menu_item.count}]
                    list_of_beef.append(a_list)
                elif each_menu_item.category == 'VEGETABLE / TOFU':
                    a_list = [each_menu_item.name, {'Spicy' : each_menu_item.is_it_spicy}, {'Count' : each_menu_item.count}]
                    list_of_vege_tofu.append(a_list)
                elif each_menu_item.category == 'SEAFOOD':
                    a_list = [each_menu_item.name, {'Spicy' : each_menu_item.is_it_spicy}, {'Count' : each_menu_item.count}]
                    list_of_seafood.append(a_list)

        return render_template('menu.html', form=form,
                                appetizer = list_of_appetizers, soup = list_of_soups, 
                                pork = list_of_pork, house_special = list_of_house_special, 
                                poultry = list_of_poultry, sizzling_plates = list_of_sizzling_plates, 
                                beef = list_of_beef, vege_tofu = list_of_vege_tofu, 
                                seafood = list_of_seafood)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/reviews')
def reviews():
    return render_template('reviews.html')

@app.route('/contact')
def contact():
    form = ContactForm()
    return render_template('contact.html', form = form)

if __name__ == '__main__':
    app.run(debug=True)
