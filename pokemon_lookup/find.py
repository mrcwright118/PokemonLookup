"""Fiind Module

Contains functions that use the PokeAPI
"""



import requests

def name(_id):
    """Gets the name of the pokemon for the ID passed in
    
    Keyword arguments:
    id -- id of pokemon
    Return: name of pokemon
    """

    base_url = "https://pokeapi.co/api/v2/pokemon"
    get_url = f"{base_url}/{_id}"
    response = requests.get(get_url,timeout=30)

    __check_response(response)

    pokemon_name = response.json()['species']['name']
    print(pokemon_name)
    return pokemon_name

def __check_response(res):
    """Check HTTP request
    
    Keyword arguments:
    res -- response from the requests library
    Return: raises exception if it wasn't a 200
    """

    if res.status_code != 200:
        raise requests.exceptions.HTTPError("Status Code was not 200. \n" \
                        f"Error: {res.text}")
