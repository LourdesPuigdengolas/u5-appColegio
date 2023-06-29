from preceptor import Preceptor

class GestorPreceptor:
    
    def getCursosByPreceptorId(self, id):
        preceptor = Preceptor.query.filter_by(id=id).first()
        cursos = preceptor.getCursos()
        formattedCursos = []
        for curso in cursos:
            addCurso = {
                'id': curso.getId(),
                'anio': curso.getAnio(),
                'division': curso.getDivision(),
            }
            formattedCursos.append(addCurso)
        return formattedCursos