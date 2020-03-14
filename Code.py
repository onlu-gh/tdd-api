import requests
import json

"""
Feature #1
"""

def get_all_characters():
    url = 'https://rickandmortyapi.com/api/character/'

    r = requests.get(url)
    forms = json.loads(r.content.decode())['results']
    all_forms = []
    curr_form = []

    character_keys = ['id', 'name', 'status', 'species', 'gender']
    for i in range(len(forms)):
        curr_val = ''
        character = forms[i]
        for key in character_keys:
            if key in character:
                curr_val = str(character[key])
            else:
                curr_val = ''
            curr_form.append(curr_val.replace('\n', ' '))

        all_forms.append(curr_form)
        curr_form = []
    return all_forms
    #print(all_forms)


get_all_characters()