from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de tramos horarios
tramos_horarios = [
    {'hora': '08:00 AM', 'disponible': True, 'motociclistas': 8},
    {'hora': '08:30 AM', 'disponible': True, 'motociclistas': 8},
    {'hora': '09:00 AM', 'disponible': True, 'motociclistas': 8},
    {'hora': '09:30 AM', 'disponible': True, 'motociclistas': 8},
    {'hora': '10:00 AM', 'disponible': True, 'motociclistas': 8},
    {'hora': '10:30 AM', 'disponible': True, 'motociclistas': 8},
    {'hora': '11:00 AM', 'disponible': True, 'motociclistas': 8},
    {'hora': '11:30 AM', 'disponible': True, 'motociclistas': 8},
    {'hora': '12:00 PM', 'disponible': True, 'motociclistas': 8},
    {'hora': '12:30 PM', 'disponible': True, 'motociclistas': 8},
    {'hora': '01:00 PM', 'disponible': True, 'motociclistas': 8},
    {'hora': '01:30 PM', 'disponible': True, 'motociclistas': 8},
    {'hora': '02:00 PM', 'disponible': True, 'motociclistas': 8},
    {'hora': '02:30 PM', 'disponible': True, 'motociclistas': 8},
    {'hora': '03:00 PM', 'disponible': True, 'motociclistas': 8},
    {'hora': '03:30 PM', 'disponible': True, 'motociclistas': 8},
    {'hora': '04:00 PM', 'disponible': True, 'motociclistas': 8},
    {'hora': '04:30 PM', 'disponible': True, 'motociclistas': 8},
    {'hora': '05:00 PM', 'disponible': True, 'motociclistas': 8},
    {'hora': '05:30 PM', 'disponible': True, 'motociclistas': 8},
    {'hora': '06:00 PM', 'disponible': True, 'motociclistas': 8},
    {'hora': '06:30 PM', 'disponible': True, 'motociclistas': 8},
    {'hora': '07:00 PM', 'disponible': True, 'motociclistas': 8},
    {'hora': '07:30 PM', 'disponible': True, 'motociclistas': 8},
    {'hora': '08:00 PM', 'disponible': True, 'motociclistas': 8},
    
    # Agrega los demás tramos horarios hasta las 08:00 PM
]

@app.route('/')
def index():
    return render_template('index.html', tramos_horarios=tramos_horarios)

@app.route('/reservar/<int:index>')
def reservar(index):
    tramo = tramos_horarios[index]
    if tramo['disponible'] and tramo['motociclistas'] > 0:
        tramo['motociclistas'] -= 1
        tramo['disponible'] = tramo['motociclistas'] > 0
    return redirect(url_for('index'))

@app.route('/liberar/<int:index>')
def liberar(index):
    tramo = tramos_horarios[index]
    
    # Verificar que no se exceda el límite de 8 motociclistas
    if tramo['motociclistas'] < 8:
        tramo['motociclistas'] += 1
        tramo['disponible'] = tramo['motociclistas'] > 0
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
