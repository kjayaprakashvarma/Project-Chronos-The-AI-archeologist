def search_web(query: str, top_k: int = 3):
    """
    Returns sample contextual links (demo version).
    Later you can connect an actual search API.
    """
    results = [
        ("SMH meaning", "https://www.dictionary.com/e/slang/smh/", "Definition of SMH (Shaking my head)"),
        ("MySpace Top 8 feature", "https://en.wikipedia.org/wiki/Myspace#Features", "Explains the 'Top 8' friends list drama"),
        ("Chat slang meanings", "https://en.wikipedia.org/wiki/Internet_slang", "Common internet abbreviations like G2G, TTYL"),
    ]
    return results[:top_k]
