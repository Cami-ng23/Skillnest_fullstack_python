import re
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Usuario:
    def __init__(self, datos):
        self.id = datos['id']
        self.nombre = datos['nombre']
        self.apellido = datos['apellido']
        self.email = datos['email']
        self.password = datos['password']
        self.created_at = datos['created_at']
        self.updated_at = datos['updated_at']

    @classmethod
    def save(cls, datos):
        consulta_sql = """
            INSERT INTO usuarios (nombre, apellido, email, password) 
            VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s);
        """
        return connectToMySQL('esquema_usuarios').query_db(consulta_sql, datos)

    @classmethod
    def get_by_email(cls, email):
        consulta_sql = "SELECT * FROM usuarios WHERE email = %(email)s;"
        datos = {'email': email}
        resultados = connectToMySQL('esquema_usuarios').query_db(consulta_sql, datos)
        if len(resultados) < 1:
            return False
        return cls(resultados[0])

    @classmethod
    def get_by_id(cls, id):
        consulta_sql = "SELECT * FROM usuarios WHERE id = %(id)s;"
        datos = {'id': id}
        resultados = connectToMySQL('esquema_usuarios').query_db(consulta_sql, datos)
        if len(resultados) < 1:
            return False
        return cls(resultados[0])

    @staticmethod
    def validar_registro(datos):
        es_valido = True
        
        # Validar Nombre
        if len(datos['nombre'].strip()) < 2 or not datos['nombre'].isalpha():
            flash("El nombre debe tener al menos 2 caracteres y contener solo letras.", "registro")
            es_valido = False
            
        # Validar Apellido
        if len(datos['apellido'].strip()) < 2 or not datos['apellido'].isalpha():
            flash("El apellido debe tener al menos 2 caracteres y contener solo letras.", "registro")
            es_valido = False
            
        # Validar Email (Formato y Existencia)
        if not EMAIL_REGEX.match(datos['email']):
            flash("El formato de correo electrónico no es válido.", "registro")
            es_valido = False
        elif Usuario.get_by_email(datos['email']):
            flash("El correo electrónico ya se encuentra registrado.", "registro")
            es_valido = False
            
        # Validar Contraseña
        if len(datos['password']) < 8:
            flash("La contraseña debe tener al menos 8 caracteres.", "registro")
            es_valido = False
            
        # Confirmar Contraseña
        if datos['password'] != datos['confirm_password']:
            flash("Las contraseñas no coinciden.", "registro")
            es_valido = False
            
        return es_valido