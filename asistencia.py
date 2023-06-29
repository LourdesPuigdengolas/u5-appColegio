from run import db

class Asistencia(db.Model):
    __tablename__ = 'asistencia'

    id: int = db.Column(db.Integer, primary_key=True)
    fecha: str = db.Column(db.String(80), nullable=False)
    codigoclase: int = db.Column(db.Integer, nullable=False)
    asistio: bool = db.Column(db.Boolean, nullable=False)
    justificacion: str = db.Column(db.String(80), nullable=False)
    idEstudiante: int = db.Column(db.Integer, db.ForeignKey('estudiante.id'), nullable=False)

    def __init__(self, fecha, codigoClase, asistio, justificacion, idEstudiante):
        self.fecha = fecha
        self.codigoclase = codigoClase
        self.asistio = asistio
        self.justificacion = justificacion
        self.idEstudiante = idEstudiante

    def getId(self):
        return self.id
    
    def getFecha(self):
        return self.fecha

    def getCodigoClase(self):
        return self.codigoclase
    
    def getAsistio(self):
        return self.asistio
    
    def getJustificacion(self):
        return self.justificacion
    
    def getIdEstudiante(self):
        return self.idEstudiante