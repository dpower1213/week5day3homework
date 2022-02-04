from flask import render_template, request, redirect, url_for
import requests
from app import app
from .forms import PokemonForm, RegistrationForm, LoginForm
# from .models from User
# from flask_login import current_user 
# login_user, logout_user, login_reuqired


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate_on_submit():
        name_first=form.name_first.data.title()
        name_last=form.name_last.data.title()
        email=form.email.data.lower()
        password=form.password.data
    
    error_string="Oooppps, that was awful......awful entertaining"
    return render_template('registration.html.j2',form=form, error=error_string)
    # return redirect(url_for('login'))
    # return render_template('registration.html.j2',form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data.lower(),
        password = form.password.data
    #            # }
    #         # new_user_object = User()
    #         # new_user_object.from_dict(new_user_data)
    #     except:
    #         error_string="Oooppps, that was awful......awful entertaining"
    #         return render_template('login.html.j2',form=form, error=error_string)
    #     return redirect(url_for('login'))
    return render_template('login.html.j2',form=form)   



@app.route('/pokemon', methods = ['GET', 'POST'])
def pokemon():
    form = PokemonForm()
    if request.method == 'POST' and form.validate_on_submit():
        #contact the api and get the info for the pokemon from the form
        name = request.form.get('name')
        print('hello', name)
        url = f"https://pokeapi.co/api/v2/pokemon/{name}"
        response = requests.get(url)
        if response.ok:
            data = response.json()            
            poke_dict = {
                'name':data['forms'][0]['name'],
                'order':data['order'],
                'ability':data['abilities'][0]['ability']['name'],
                'base_experience':data['base_experience'],
                'front_shiny':data['sprites']['front_shiny'],
                'stat_name1':data['stats'][0]['stat']['name'],
                'stat_rating1':data['stats'][0]['base_stat'],
                'stat_name2':data['stats'][1]['stat']['name'],
                'stat_rating2':data['stats'][1]['base_stat'],
                'stat_name3':data['stats'][2]['stat']['name'],
                'stat_rating3':data['stats'][2]['base_stat']
            }
            return render_template('pokemon.html.j2', poke = poke_dict, form=form)
        else:
            error_string = "pokemon always causin trouble"
            return render_template('pokemon.html.j2', error = error_string, form=form)
    return render_template('pokemon.html.j2', form=form)
    
@app.route('/')
def index():
    return render_template('index.html.j2')