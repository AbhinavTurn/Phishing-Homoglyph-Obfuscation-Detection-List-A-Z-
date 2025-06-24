import re

homoglyphs = {
    'a': ['а', '@', '4'],
    'e': ['е', '3'],
    'i': ['1', 'l', '!', 'і'],
    'o': ['0', 'о'],
    's': ['5', '$'],
    'c': ['с'],
    'g': ['9', 'ɡ'],
    'l': ['1', '|'],
    't': ['7'],
}

def normalize(text):
    for real_char, glyphs in homoglyphs.items():
        for g in glyphs:
            text = text.replace(g, real_char)
    return text.lower()

suspicious_domains = ["g00gle.com", "faceb00k.com", "micros0ft.com"]

for domain in suspicious_domains:
    print(f"Original: {domain} => Normalized: {normalize(domain)}")
