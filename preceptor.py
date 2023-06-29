from run import db

class Preceptor(db.Model):
    __tablename__ = 'preceptor'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    apellido = db.Column(db.String(80), nullable=False)
    correo = db.Column(db.String(120), unique=True, nullable=False)
    clave = db.Column(db.String(120), nullable=False)
    cursos = db.relationship('Curso', backref='preceptor', lazy=True)

    def __init__(self, nombre, apellido, correo, clave):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.clave = clave
    
    def getidPrece(self):
        return self.id
    def getNombre(self):
        return self.nombre
    def getApellidoPrece(self):
        return self.apellido
    def getCorreo(self):
        return self.correo
    def getClave(self):
        return self.clave
    def getCursos(self):
        return self.cursos
