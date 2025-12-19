from importlib import import_module
from pathlib import Path

class Assistant:
    """Núcleo simple para un asistente virtual.

    Skills deben exponerse como una clase `Skill` con métodos
    `can_handle(text: str) -> bool` y `handle(text: str, **kwargs) -> str`.
    """
    def __init__(self, name: str = "Asistente"):
        self.name = name
        self.skills = []

    def register_skill(self, skill) -> None:
        self.skills.append(skill)

    def load_skills_from_package(self, package: str) -> None:
        pkg_path = Path(package.replace('.', '/'))
        if not pkg_path.exists():
            return
        for p in pkg_path.glob('*.py'):
            if p.stem.startswith('__'):
                continue
            modname = f"{package}.{p.stem}"
            try:
                mod = import_module(modname)
            except Exception:
                continue
            if hasattr(mod, 'Skill'):
                try:
                    self.register_skill(mod.Skill())
                except Exception:
                    pass

    def handle(self, text: str, **kwargs) -> str:
        text = (text or "").strip()
        for skill in self.skills:
            try:
                if skill.can_handle(text):
                    return skill.handle(text, **kwargs)
            except Exception:
                continue
        return f"No pude procesar: {text}"
