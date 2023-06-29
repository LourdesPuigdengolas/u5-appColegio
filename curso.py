from run import db

class Curso(db.Model):
    __tablename__ = 'curso'

    id: int = db.Column(db.Integer, primary_key=True)
    anio: int = db.Column(db.Integer, nullable=False)
    division: str = db.Column(db.Integer, nullable=False)
    idpreceptor: int = db.Column(db.Integer, db.ForeignKey('preceptor.id'), nullable=False)
    estudiantes = db.relationship('Estudiante', backref='curso', lazy=True)

    def __init__(self, id, anio, division, idpreceptor):
        self.id = id
        self.anio = anio
        self.division = division
        self.idpreceptor = idpreceptor
    
    def getId(self):
        return self.id
    def getAnio(self):
        return self.anio
    def getDivision(self):
        return self.division
    def getIdPreceptor(self):    
        return self.idpreceptor
    def getEstudiantes(self):
        return self.estudiantes
