from run import db

class Padre(db.Model):
    __tablename__ = 'padre'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    apellido = db.Column(db.String(80), nullable=False)
    correo = db.Column(db.String(120), unique=True, nullable=False)
    clave = db.Column(db.String(120), nullable=False)
    estudiantes = db.relationship('Estudiante', backref='padre', lazy=True)

    def __init__(self, nombre, apellido, correo, clave):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.clave = clave
    
    def getIdPadre(self):
        return self.id
    def getNombre(self):
        return self.nombre
    def getApellidoPadre(self):
        return self.apellido
    def getCorreo(self):
        return self.correo
    def getClave(self):
        return self.clave
    def getEstudiantes(self):
        return self.estudiantes