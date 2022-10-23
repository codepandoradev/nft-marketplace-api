from typing import Final

ALLOWED_NFT_CONTENT_EXTENSIONS: Final[set[str]] = {'png', 'gif', 'webp', 'mp4', 'mp3'}
NFT_TITLE_MAX_LENGTH: Final[int] = 30
NFT_TITLE_REGEX: Final[str] = '^[a-zA-Z ]+$'
