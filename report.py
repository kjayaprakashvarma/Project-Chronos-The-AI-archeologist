import datetime

def make_report(original: str, reconstructed: str, sources: list) -> str:
    """
    Saves a formatted Reconstruction Report to a file.
    """
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"reconstruction_report_{timestamp}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write("--- RECONSTRUCTION REPORT ---\n\n")
        f.write("[Original Fragment]\n")
        f.write(f"> {original}\n\n")
        f.write("[AI-Reconstructed Text]\n")
        f.write(f"> {reconstructed}\n\n")
        f.write("[Contextual Sources]\n")
        for title, url, snippet in sources:
            f.write(f"* {title}: {url}\n  - {snippet}\n")

    return filename
