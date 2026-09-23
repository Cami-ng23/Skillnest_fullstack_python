# El juego del destino

Aplicación web básica creada con Flask para practicar:

- Rutas en Flask.
- Formularios.
- Método POST.
- Sesiones.
- Redirecciones.
- Plantillas HTML con Jinja2.
- Archivos estáticos CSS.

## Estructura

```text
juego_destino/
├── server.py
├── requirements.txt
├── templates/
│   ├── index.html
│   └── futuro.html
└── static/
    └── style.css
```

## Ejecutar

Instalar Flask:

```bash
pip install -r requirements.txt
```

Ejecutar:

```bash
python server.py
```

Abrir en el navegador:

```text
http://127.0.0.1:5000/
```

## Rutas

- `/` muestra el formulario.
- `/enviar` recibe los datos mediante POST, los guarda en sesión y redirige a `/futuro`.
- `/futuro` muestra los datos y una predicción aleatoria.
