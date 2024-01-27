from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

universidades_data = [
    {
        'nombre': 'Universidad de Buenos Aires - UBA',
        'imagen': 'https://www.cbc.uba.ar/archivos/2-5f9b1c6cdee00_602ff90223c9f.jpg',
        'enlace': ['https://resizer.iproimg.com/unsafe/880x/filters:format(webp)/https://assets.iprofesional.com/assets/jpg/2014/09/407382.jpg', 'https://uba.ar/storage/RqYIA4XUCdG7Hnc07uAvX8Gaw0wP1ibB57xRq39L.jpg', 'https://diarioandino-s2.cdn.net.ar/st2i1700/2023/06/diarioandino2/images/53/55/535581_919827bec22d4f6d17376e8c04de3664f910245d510e537d55f34bcedb287eb0/lg.webp', 'https://www.sociales.uba.ar/wp-content/uploads/tapa26.jpg', ''],
        'tipo': 'Pública',
        'ranking': '1',
        'descripcion': 'La Universidad de Buenos Aires (UBA) es una institución educativa pública de Argentina, considerada una de las más prestigiosas de América Latina. Fue fundada en 1821 y ofrece una amplia variedad de carreras en diferentes áreas del conocimiento.',
        'carreras': ['Informática', 'Biología', 'Matemáticas', 'Física', 'Química', '...', 'Otras Carreras'],
        'campus': {
            'libreria': ['Librería A', 'Librería B', 'Librería C'],
            'dormitorios': ['Dormitorio 1', 'Dormitorio 2', 'Dormitorio 3'],
            'laboratorios': ['Laboratorio de Informática', 'Laboratorio de Biología', 'Laboratorio de Física'],
            'instalacion_deportiva': ['Cancha de Fútbol', 'Pista de Atletismo', 'Gimnasio'],
            'cafeterias': ['Cafetería Principal', 'Cafetería del Campus', 'Cafetería de Ciencias'],
         },
        'contacto': {
            'ubicacion': ['Av. Córdoba, 3501, Buenos Aires, Argentina.'],
            'telefono': ['(5411)-4964-4600.'],
            'email': ['informes@palermo.edu'],
            'web': ['https://www.palermo.edu/'],
        },
        'sedes': ['Facultad de Ciencias Exactas y Naturales, UBA - Av. Int. Cantilo, Buenos Aires',	'UBA, Facultad de Ingeniería - Av. Gral. Las Heras 2214, C1126 CABA', 'Facultad de Ciencias Sociales - UBA -Marcelo Torcuato de Alvear 2230, C1122AAJ CABA','Facultad de Medicina de la Universidad de Buenos Aires - Paraguay 2155, C1121 ABG, Buenos Aires','Facultad de Ciencias Económicas - Av. Córdoba 2122, C1113 CABA','Universidad de Buenos Aires - Viamonte 430, C1053 CABA','Facultad de Filosofía y Letras - UBA - Puan 480, C1420 CABA','Uba sede de San Miguel - Gelly y Obes 1351, B1663FMF San Miguel, Provincia de Buenos Aires',	'Sede UBA - Moreno - ISFT N°179, Martín Fierro 250, B1744 Moreno, Provincia de Buenos Aires'],
    },
    {
    'nombre': 'Universidad Nacional de Córdoba - UNC',
    'imagen': 'https://www.unc.edu.ar/sites/default/files/UNC_Campus_Virtual_cursos_0_4.jpg',
    'tipo': 'Pública',
    'ranking': '2',
    'descripcion': 'La Universidad Nacional de Córdoba (UNC) es una institución educativa pública ubicada en la ciudad de Córdoba, Argentina. Fundada en 1613, es la universidad más antigua del país. Ofrece una amplia gama de carreras y cuenta con múltiples sedes y facultades.',
    'carreras': ['Ingeniería Civil', 'Medicina', 'Derecho', 'Arquitectura', 'Ciencias Económicas', '...', 'Otras Carreras'],
    'campus': {
        'libreria': ['Librería X', 'Librería Y', 'Librería Z'],
        'dormitorios': ['Residencia A', 'Residencia B', 'Residencia C'],
        'laboratorios': ['Laboratorio de Ciencias', 'Laboratorio de Ingeniería', 'Laboratorio de Medicina'],
        'instalacion_deportiva': ['Cancha de Tenis', 'Piscina Olímpica', 'Gimnasio'],
        'cafeterias': ['Cafetería Principal UNC', 'Cafetería del Campus', 'Cafetería de Ciencias'],
     },
    'contacto': {
        'ubicacion': ['Av. Haya de la Torre s/n, Ciudad Universitaria, Córdoba, Argentina.'],
        'telefono': ['(54 351) 5353838'],
        'email': ['info@unc.edu.ar'],
        'web': ['https://www.unc.edu.ar/'],
    },
    'sedes': ['Facultad de Ciencias Exactas, Físicas y Naturales', 'Facultad de Medicina', 'Facultad de Derecho y Ciencias Sociales', '...', 'Otras Facultades'],
},
{
    'nombre': 'Universidad Nacional de La Plata - UNLP',
    'imagen': 'https://perio.unlp.edu.ar/wp-content/uploads/2022/08/UNLP-e1660823710783.jpg',
    'tipo': 'Pública',
    'ranking': '3',
    'descripcion': 'La Universidad Nacional de La Plata (UNLP) es una universidad pública ubicada en la ciudad de La Plata, Buenos Aires, Argentina. Fundada en 1905, es una de las principales instituciones educativas del país. Ofrece diversas carreras y cuenta con múltiples facultades y sedes.',
    'carreras': ['Ingeniería Informática', 'Ciencias Biológicas', 'Psicología', 'Comunicación Social', 'Arquitectura', '...', 'Otras Carreras'],
    'campus': {
        'libreria': ['Librería L', 'Librería M', 'Librería N'],
        'dormitorios': ['Residencia X', 'Residencia Y', 'Residencia Z'],
        'laboratorios': ['Laboratorio de Informática', 'Laboratorio de Biología', 'Laboratorio de Psicología'],
        'instalacion_deportiva': ['Cancha de Fútbol', 'Pista de Atletismo', 'Gimnasio'],
        'cafeterias': ['Cafetería Principal UNLP', 'Cafetería del Campus', 'Cafetería de Ciencias'],
     },
    'contacto': {
        'ubicacion': ['Av. 7 No. 776, La Plata, Buenos Aires, Argentina.'],
        'telefono': ['(54 221) 422-2222'],
        'email': ['info@unlp.edu.ar'],
        'web': ['https://www.unlp.edu.ar/'],
    },
    'sedes': ['Facultad de Informática', 'Facultad de Ciencias Naturales y Museo', 'Facultad de Psicología', '...', 'Otras Facultades'],
}

    # Agrega más universidades según tu necesidad
]

carreras_data = [
    {
        'nombre': 'Ingenieria Informatica',
        'duracion': '4 años',
        'salario': ' ARS 327,048 - ARS 524,133 mensuales.',
        'descripcion': 'La Criminología se centra en el estudio de eventos delictivos, aplicando técnicas y métodos criminológicos e investigativos. Los profesionales en esta área toman acciones importantes ante diversos delitos.',
        'imagen': 'https://universidadeuropea.com/resources/media/images/que-es-ingenieria-informatica-1200x630.original.jpg',
        
    }

    # Agrega más universidades según tu necesidad
]

@app.route('/')
def home():
    universidad = {
        'titulo': 'Universidad de Buenos Aires - UBA',
        'imagen': 'img.jpg',
        'descripcion': 'UBA es una universidad argentina.',
        'carreras': ['Informatica', 'Biologia', '...'],
    }
    return render_template('index.html', universidad=universidad)

@app.route('/universidades')
def mostrar_universidades():
    return render_template('universidades.html', universidades=universidades_data)

@app.route('/universidad/<nombre>')
def universidad(nombre):
    universidad_seleccionada = next((uni for uni in universidades_data if uni['nombre'] == nombre), None)

    if universidad_seleccionada:
        return render_template('universidad.html', universidad=universidad_seleccionada)
    else:
        return render_template('universidad_no_encontrada.html')
    
@app.route('/carreras')
def mostrar_carreras():
    return render_template('carreras.html',)

if __name__ == '__main__':
    app.run(debug=True)