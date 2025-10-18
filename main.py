import os
import sys
from dotenv import load_dotenv
from gemini_client import reconstruct_text
from search_client import search_web
from report import make_report

# Load environment variables from .env file
load_dotenv()

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py \"<fragment text>\"")
        sys.exit(1)

    fragment = sys.argv[1]
    print("\n--- PROJECT CHRONOS: The AI Archeologist ---")
    print("Original Fragment:", fragment)

    # Step 1: Reconstruct using Gemini
    reconstructed = reconstruct_text(fragment)
    print("\nAI-Reconstructed Text:\n", reconstructed)

    # Step 2: Search web using reconstructed text
    print("\nFetching contextual sources...")
    sources = search_web(reconstructed, top_k=3)

    # Step 3: Generate Reconstruction Report
    report_path = make_report(fragment, reconstructed, sources)
    print(f"\n✅ Reconstruction Report generated: {report_path}\n")

if __name__ == "__main__":
    main()
