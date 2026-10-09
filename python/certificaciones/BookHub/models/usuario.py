import re


class Usuario:
    """Modelo de usuario: representación y validación de datos."""
    EMAIL_REGEX = re.compile(r"^[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}$")

    def __init__(self, id, nombre, apellido, email, password=None, created_at=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password
        self.created_at = created_at

    @classmethod
    def validar_registro(cls, form):
        """Devuelve (datos_limpios, lista_de_errores)."""
        datos = {
            "nombre": (form.get("nombre") or "").strip(),
            "apellido": (form.get("apellido") or "").strip(),
            "email": (form.get("email") or "").strip().lower(),
        }
        password = form.get("password") or ""
        confirmar = form.get("confirmar_password") or ""
        errores = []

        if not all([datos["nombre"], datos["apellido"], datos["email"], password, confirmar]):
            errores.append("Debes completar todos los campos.")
        if datos["nombre"] and len(datos["nombre"]) < 2:
            errores.append("El nombre debe tener al menos 2 caracteres.")
        if datos["apellido"] and len(datos["apellido"]) < 2:
            errores.append("El apellido debe tener al menos 2 caracteres.")
        if datos["email"] and not cls.EMAIL_REGEX.match(datos["email"]):
            errores.append("El correo no tiene un formato válido.")
        if password:
            if len(password) < 8 or not re.search(r"[A-Za-z]", password) or not re.search(r"\d", password):
                errores.append("La contraseña debe tener al menos 8 caracteres, una letra y un número.")
        if password and confirmar and password != confirmar:
            errores.append("Las contraseñas no coinciden.")
        return datos, errores, password

    @classmethod
    def validar_login(cls, form):
        email = (form.get("email") or "").strip().lower()
        password = form.get("password") or ""
        errores = []
        if not email or not password:
            errores.append("Debes completar todos los campos.")
        return email, password, errores
