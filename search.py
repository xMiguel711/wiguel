import requests

def search_web(query):
    url = f"https://duckduckgo.com/?q={query}&format=json"
    try:
        response = requests.get(url)
        data = response.json()
        if "AbstractText" in data and data["AbstractText"]:
            return data["AbstractText"]
        return "No encontré información útil en la web."
    except:
        return "Error al buscar en la web."
