from curso import Curso

class GestorCurso:
    
    def getEstudiantesByCurso(self, id):
        curso = Curso.query.filter_by(id=id).first()
        estudiantes = curso.getEstudiantes()
        formattedEstudiantes = []
        for estudiante in estudiantes:
            addEstudiante = {
                'id': estudiante.getId(),
                'nombre': estudiante.getNombre(),
                'apellido': estudiante.getApellido(),
                'dni': estudiante.getDni(),
                'direccion': estudiante.getDireccion(),
                'telefono': estudiante.getTelefono(),
                'email': estudiante.getEmail(),
                'fechaNacimiento': estudiante.getFechaNacimiento(),
                'curso': estudiante.getCurso(),
                'padre': estudiante.getPadre(),
            }
            formattedEstudiantes.append(addEstudiante)
        return formattedEstudiantes