class Skill:
    def can_handle(self, text: str) -> bool:
        t = (text or '').lower()
        return any(w in t for w in ('hola', 'buenos', 'buenas', 'buen', 'hi'))

    def handle(self, text: str, **kwargs) -> str:
        return '¡Hola! Soy tu asistente. ¿En qué puedo ayudarte hoy?'
