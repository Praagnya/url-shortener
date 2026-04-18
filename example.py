import secrets

secrets_db = {}


def generate_short_code(url: str):
    """Takes a URL and gives a secret code"""
    for code, url in secrets_db.items():
        if url in secrets.values: 
            return secrets_db[url]
    else:
        secret_code = secrets.token_urlsafe(6)
        secrets_db[secret_code] = url
    return secrets_db[secret_code]

url = "https://example.com"
code = generate_short_code(url)

print("URL:", url)
print("Short code:", code)
print("DB:", secrets_db)