def normalize(text: str) -> str:
    """
    Clean and normalize user text.
    """
    return text.strip().lower().replace("\n", " ")
