import argparse
from mrcwrightc118.PokemonLookup import find


parser = argparse.ArgumentParser()
parser.add_argument('-id', dest="id", action='store', required=True, help="The ID of the pokemon to get the name for")

parsed_args = parser.parse_args()

def start():
    find.name(parsed_args.id)