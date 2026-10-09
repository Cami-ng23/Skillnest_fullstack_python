from datetime import datetime


class Libro:
    """Modelo de libro: constantes y validación de datos."""
    GENEROS = [
        "Novela", "Fábula", "Ciencia Ficción", "Desarrollo Personal", "Romance",
        "Fantasía", "Misterio", "Historia", "Biografía", "Poesía", "Otro",
    ]

    def __init__(self, id, titulo, autor, genero, fecha_publicacion, descripcion, usuario_id):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.fecha_publicacion = fecha_publicacion
        self.descripcion = descripcion
        self.usuario_id = usuario_id

    @classmethod
    def validar(cls, form):
        """Devuelve (datos_limpios, lista_de_errores). Se usa en crear y editar."""
        datos = {
            "titulo": (form.get("titulo") or "").strip(),
            "autor": (form.get("autor") or "").strip(),
            "genero": (form.get("genero") or "").strip(),
            "fecha_publicacion": (form.get("fecha_publicacion") or "").strip(),
            "descripcion": (form.get("descripcion") or "").strip(),
        }
        errores = []
        if not all(datos.values()):
            errores.append("Debes completar todos los campos.")
        if datos["titulo"] and len(datos["titulo"]) < 2:
            errores.append("El título debe tener al menos 2 caracteres.")
        if len(datos["titulo"]) > 150:
            errores.append("El título no puede superar los 150 caracteres.")
        if datos["autor"] and len(datos["autor"]) < 2:
            errores.append("El autor debe tener al menos 2 caracteres.")
        if len(datos["autor"]) > 100:
            errores.append("El autor no puede superar los 100 caracteres.")
        if datos["genero"] and datos["genero"] not in cls.GENEROS:
            errores.append("Selecciona un género válido.")
        if datos["fecha_publicacion"]:
            try:
                fecha = datetime.strptime(datos["fecha_publicacion"], "%Y-%m-%d").date()
                if fecha.year < 1:
                    raise ValueError
            except ValueError:
                errores.append("La fecha de publicación no es válida.")
        if datos["descripcion"] and len(datos["descripcion"]) < 10:
            errores.append("La descripción debe tener al menos 10 caracteres.")
        return datos, errores
