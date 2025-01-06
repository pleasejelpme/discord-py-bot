import re

def format_wiki_text(text: str) -> str:
    no_brackets_text = re.sub(r'\[.*?\]', '', text)
    clean_text = re.sub(' +', ' ', no_brackets_text).strip()
    return clean_text