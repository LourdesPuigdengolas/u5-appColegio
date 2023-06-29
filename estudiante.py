from run import db

class Estudiante(db.Model):
    __tablename__ = 'estudiante'

    id: int = db.Column(db.Integer, primary_key=True)
    nombre: str = db.Column(db.String(80), nullable=False)
    apellido: str = db.Column(db.String(80), nullable=False)
    dni: str = db.Column(db.String(80), nullable=False)
    idCurso: int = db.Column(db.Integer, db.ForeignKey('curso.id'), nullable=False)
    idPadre: int = db.Column(db.Integer, db.ForeignKey('padre.id'), nullable=False)
    asistencias = db.relationship('Asistencia', backref='estudiante', lazy=True)

    def __init__(self, id, nombre, apellido, dni, idCurso, idPadre):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.idCurso = idCurso
        self.idPadre = idPadre
    
    def getIdEstud(self):
        return self.id
    def getNombre(self):
        return self.nombre
    def getApellidoEstud(self):
        return self.apellido
    def getDni(self):
        return self.dni
    def getIdCurso(self):
        return self.idCurso
    def getIdPadre(self):
        return self.idPadre
    def getAsistencias(self):
        return self.asistencias