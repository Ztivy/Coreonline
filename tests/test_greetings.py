from src.assistant import Assistant
from src.skills.greetings import Skill


def test_greeting_skill():
    a = Assistant()
    a.register_skill(Skill())
    res = a.handle('Hola, ¿qué tal?')
    assert 'Hola' in res or '¡' in res
