import requests
from bs4 import BeautifulSoup

# URL local de tu página con Live Server
URL = "http://127.0.0.1:5500/index.html"

# ID del valor que queremos extraer del HTML
TARGET_ID = "usd-eur-rate"


def obtener_html(url):
    """
    Realiza una petición HTTP y devuelve el contenido HTML de la página.
    Maneja errores de conexión y códigos HTTP incorrectos.
    """
    try:
        respuesta = requests.get(url)
    except requests.exceptions.ConnectionError:
        raise Exception(f"No se pudo conectar a {url}. ¿Está Live Server encendido?")
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error realizando la solicitud: {e}")

    if respuesta.status_code != 200:
        raise Exception(f"Error HTTP {respuesta.status_code} al acceder a la página.")

    return respuesta.text


def extraer_valor(html, element_id):
    """
    Parsea el HTML, busca el elemento con el id indicado
    y devuelve su texto. Maneja el caso de elemento no encontrado.
    """
    soup = BeautifulSoup(html, "html.parser")
    elemento = soup.find(id=element_id)

    if not elemento:
        raise Exception(f"No se encontró el elemento con id '{element_id}' en la página.")

    return elemento.get_text(strip=True)


def main():
    try:
        html = obtener_html(URL)
        valor = extraer_valor(html, TARGET_ID)
        print(f"Valor encontrado para '{TARGET_ID}': {valor}")
    except Exception as error:
        print(f"❌ Error: {error}")


if __name__ == "__main__":
    main()