# from flask import Flask, session, redirect, url_for, render_template_string, request

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'  # Change this to a random secret key

# @app.route('/', methods=['GET'])
# def index():
#     if 'visit_count' not in session:
#         session['visit_count'] = 0
#     if 'reset_count' not in session:
#         session['reset_count'] = 0
#     session['visit_count'] += 1
#     return render_template_string('''
#         <h1>Visit Count: {{ visit_count }}</h1>
#         <h2>Reset Count: {{ reset_count }}</h2>
#         <form action="{{ url_for('destroy_session') }}" method="post" style="display:inline;">
#             <button type="submit">Reset Count</button>
#         </form>
#         <form action="{{ url_for('add_two') }}" method="post" style="display:inline;">
#             <button type="submit">Sumar +2 visitas</button>
#         </form>
#         <form action="{{ url_for('add_custom') }}" method="post" style="display:inline;">
#             <input type="number" name="custom_number" min="1" required>
#             <button type="submit">Sumar visitas personalizadas</button>
#         </form>
#     ''', visit_count=session['visit_count'], reset_count=session['reset_count'])

# @app.route('/destroy_session', methods=['GET', 'POST'])
# def destroy_session():
#     session['reset_count'] = session.get('reset_count', 0) + 1
#     session.pop('visit_count', None)
#     return redirect(url_for('index'))

# @app.route('/add_two', methods=['POST'])
# def add_two():
#     if 'visit_count' not in session:
#         session['visit_count'] = 0
#     session['visit_count'] += 2
#     return redirect(url_for('index'))

# @app.route('/add_custom', methods=['POST'])
# def add_custom():
#     if 'visit_count' not in session:
#         session['visit_count'] = 0
#     try:
#         custom_number = int(request.form.get('custom_number', 0))
#         if custom_number > 0:
#             session['visit_count'] += custom_number
#     except ValueError:
#         pass
#     return redirect(url_for('index'))

# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, session, redirect, url_for, render_template_string, request

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Cambia esto por una clave secreta aleatoria

@app.route('/', methods=['GET'])
def index():
    # Comprobar si existe la propiedad en sesión antes de usarla
    if 'visit_count' not in session:
        session['visit_count'] = 0
    if 'reset_count' not in session:
        session['reset_count'] = 0
    session['visit_count'] += 1
    return render_template_string('''
        <h1>Visit Count: {{ visit_count }}</h1>
        <h2>Reset Count: {{ reset_count }}</h2>
        <form action="{{ url_for('destroy_session') }}" method="post" style="display:inline;">
            <button type="submit">Reset Count</button>
        </form>
        <form action="{{ url_for('add_two') }}" method="post" style="display:inline;">
            <button type="submit">Sumar +2 visitas</button>
        </form>
        <form action="{{ url_for('add_custom') }}" method="post" style="display:inline;">
            <input type="number" name="custom_number" min="1" required>
            <button type="submit">Sumar visitas personalizadas</button>
        </form>
    ''', visit_count=session['visit_count'], reset_count=session['reset_count'])

@app.route('/destroy_session', methods=['GET', 'POST'])
def destroy_session():
    # Comprobar si existe la propiedad antes de eliminarla
    if 'reset_count' in session:
        session['reset_count'] += 1
    else:
        session['reset_count'] = 1
    # Eliminar solo la propiedad visit_count
    if 'visit_count' in session:
        session.pop('visit_count')
    return redirect(url_for('index'))

@app.route('/add_two', methods=['POST'])
def add_two():
    if 'visit_count' in session:
        session['visit_count'] += 2
    else:
        session['visit_count'] = 2
    return redirect(url_for('index'))

@app.route('/add_custom', methods=['POST'])
def add_custom():
    if 'visit_count' not in session:
        session['visit_count'] = 0
    try:
        custom_number = int(request.form.get('custom_number', 0))
        if custom_number > 0:
            session['visit_count'] += custom_number
    except ValueError:
        pass
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)