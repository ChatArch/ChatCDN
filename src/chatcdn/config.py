"Typed environment configuration for ChatCDN."

from chatenv import BaseEnvConfig, EnvField


class ChatcdnConfig(BaseEnvConfig):
    "ChatCDN ChatEnv configuration."

    _title = "ChatCDN Configuration"
    _aliases = ["chatcdn"]
    _storage_dir = "Chatcdn"

    @classmethod
    def test(cls) -> None:
        """Validate schema registration without external side effects."""

        print(f"Testing {cls._title}...")
        print("Schema loaded; no network test is required.")

    CHATCDN_API_KEY = EnvField(
        "CHATCDN_API_KEY",
        desc="API key",
        is_sensitive=True,
    )


__all__ = ["ChatcdnConfig"]
