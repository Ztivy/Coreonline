# Documentación mínima

Cómo usar el esqueleto del asistente virtual

- Ejecutar la interfaz CLI:

```bash
python3 -m src.cli "Hola"
# o interactivo
python3 -m src.cli
```

- Ejecutar tests:

```bash
pip install -r requirements.txt
pytest -q
```

Estructura:

- `src/assistant.py`: Núcleo del asistente
- `src/skills/`: Skills (módulos) que el asistente carga
- `src/cli.py`: CLI de ejemplo
