class Favorito:
    """Relación N:M entre usuario y libro."""

    def __init__(self, id, usuario_id, libro_id, created_at=None):
        self.id = id
        self.usuario_id = usuario_id
        self.libro_id = libro_id
        self.created_at = created_at
