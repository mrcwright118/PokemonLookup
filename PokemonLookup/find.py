import requests

def name(id):
    base_url = "https://pokeapi.co/api/v2/pokemon"
    get_url = f"{base_url}/{id}"
    response = requests.get(get_url)

    __check_response(response)

    name = response.json()['species']['name']
    print(name)
    return name

def __check_response(res):
    if res.status_code != 200:
        raise Exception("Status Code was not 200. \n" \
                        f"Error: {res.text}")
