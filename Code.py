import requests
import json

"""
# Feature #1
"""


def get_characters(spec=-1):
    url = 'https://rickandmortyapi.com/api/character/'

    if (type(spec) == int and spec != -1) or type(spec) == list:
        url += str(spec).replace(' ', '')

    r = requests.get(url)
    forms = json.loads(r.content.decode())
    if type(spec) == int and spec == -1:
        forms = forms['results']
    elif type(spec) == int and spec != -1:
        forms = [forms]
    all_forms = []
    curr_form = []

    character_keys = ['id', 'name', 'status', 'species', 'gender']
    for i in range(len(forms)):
        curr_val = ''
        character = forms[i]
        if 'id' not in character:
            continue
        for key in character_keys:
            if key in character:
                curr_val = str(character[key])
            else:
                curr_val = ''
            curr_form.append(curr_val.replace('\n', ' '))

        all_forms.append(curr_form)
        curr_form = []
    return all_forms

