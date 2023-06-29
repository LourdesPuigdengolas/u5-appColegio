from preceptor import Preceptor
import hashlib

class GestorLogin():
    __email = None
    __password = None

    def __init__(self, email, password):
        self.__email = email
        self.__password = password

    def verifyUserAndGetId(self):
        clave = self.cipherPassword()
        # busca en la base de datos si existe un preceptor
        #  con el correo y clave (cifrada) ingresados
        preceptor = Preceptor.query.filter_by(
            correo=self.__email,
            clave=clave
            ).first()
        if preceptor:
            return preceptor.id
        return None
        

    def cipherPassword(self):
        # cifrado de la clave utilizando md5
        result = hashlib.md5(bytes(self.__password, encoding='utf-8'))
        # muestra la clave cifrada en hexadecimal, esta es la que se guarda en base de datos
        return result.hexdigest()