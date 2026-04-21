from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'marcos_portafolio_2024_secreto'

MI_NOMBRE = "Marcos Fernando Tonconi Valencia"
MI_CORREO = "valenciamaxfernando@gmail.com"
MI_TELEFONO = "+591 76549227"
MI_UBICACION = "Bolivia"
MI_CARGO = "Desarrollador Python"
MI_DESCRIPCION = "Apasionado por el desarrollo web y la creación de soluciones innovadoras"
MI_GITHUB = "https://github.com/MarcValencia2006"

class ContactoForm(FlaskForm):
    nombre = StringField('Tu Nombre', validators=[DataRequired(message='El nombre es requerido'), Length(min=2, max=50)])
    email = EmailField('Tu Email', validators=[DataRequired(message='El email es requerido'), Email(message='Email inválido')])
    mensaje = TextAreaField('Mensaje', validators=[DataRequired(message='El mensaje es requerido'), Length(min=10, max=500)])
    enviar = SubmitField('Enviar Mensaje')

proyectos = [
    {
        'id': 1,
        'titulo': 'Sistema de Gestión de Inventario',
        'descripcion': 'Aplicación web completa para gestión de inventario con Flask y MySQL',
        'tecnologias': ['Python', 'Flask', 'MySQL', 'Bootstrap'],
        'url': 'https://github.com/MarcValencia2006/proyecto1'
    },
    {
        'id': 2,
        'titulo': 'API REST para Tienda Online',
        'descripcion': 'API robusta con autenticación JWT y documentación automática',
        'tecnologias': ['Python', 'FastAPI', 'JWT', 'PostgreSQL'],
        'url': 'https://github.com/MarcValencia2006/proyecto2'
    },
    {
        'id': 3,
        'titulo': 'Dashboard de Análisis de Datos',
        'descripcion': 'Dashboard interactivo con gráficos en tiempo real y reportes',
        'tecnologias': ['Python', 'Pandas', 'Plotly', 'Flask'],
        'url': 'https://github.com/MarcValencia2006/proyecto3'
    },
    {
        'id': 4,
        'titulo': 'Aplicación de Tareas con Flask',
        'descripcion': 'Gestor de tareas con autenticación de usuarios y base de datos',
        'tecnologias': ['Python', 'Flask', 'SQLite', 'Bootstrap'],
        'url': 'https://github.com/MarcValencia2006/proyecto4'
    }
]

habilidades = [
    {'nombre': 'Python', 'nivel': 90, 'icono': 'fab fa-python', 'color': '#3776AB'},
    {'nombre': 'Flask', 'nivel': 85, 'icono': 'fas fa-flask', 'color': '#000000'},
    {'nombre': 'JavaScript', 'nivel': 80, 'icono': 'fab fa-js', 'color': '#F7DF1E'},
    {'nombre': 'HTML5/CSS3', 'nivel': 95, 'icono': 'fab fa-html5', 'color': '#E34F26'},
    {'nombre': 'SQL', 'nivel': 85, 'icono': 'fas fa-database', 'color': '#4479A1'},
    {'nombre': 'Git/GitHub', 'nivel': 88, 'icono': 'fab fa-git-alt', 'color': '#F05032'},
    {'nombre': 'Bootstrap', 'nivel': 90, 'icono': 'fab fa-bootstrap', 'color': '#7952B3'},
    {'nombre': 'REST APIs', 'nivel': 82, 'icono': 'fas fa-plug', 'color': '#FF6C37'}
]

@app.context_processor
def inject_personal_data():
    return {
        'current_year': datetime.datetime.now().year,
        'mi_nombre': MI_NOMBRE,
        'mi_correo': MI_CORREO,
        'mi_telefono': MI_TELEFONO,
        'mi_ubicacion': MI_UBICACION,
        'mi_cargo': MI_CARGO,
        'mi_descripcion': MI_DESCRIPCION,
        'mi_github': MI_GITHUB
    }

@app.route('/')
def index():
    return render_template('index.html', proyectos=proyectos[:3])

@app.route('/proyectos')
def proyectos_page():
    return render_template('proyectos.html', proyectos=proyectos)

@app.route('/habilidades')
def habilidades_page():
    return render_template('habilidades.html', habilidades=habilidades)

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    form = ContactoForm()
    if form.validate_on_submit():
        flash(f'¡Gracias {form.nombre.data}! Tu mensaje ha sido recibido. Te responderé pronto a {form.email.data}', 'success')
        return redirect(url_for('contacto'))
    return render_template('contacto.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)