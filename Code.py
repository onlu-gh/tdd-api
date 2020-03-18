import requests
import json

"""
# Feature #1
"""


def get_characters(spec=-1):
    url = 'https://rickandmortyapi.com/api/character/'

    if spec != -1:
        if (type(spec) == int and spec != -1) or \
                (type(spec) == list and len(spec) != 0
                 and type(spec[0]) == int):
            url += str(spec).replace(' ', '') + '/'
        elif type(spec) == list and len(spec) != 0 and spec[0] == '?':
            url += '?' + spec[1]
            for f in spec[2:]:
                url += '&' + f
        else:
            return 'error'

    r = requests.get(url)
    forms = json.loads(r.content.decode())
    if type(forms) == dict and 'error' in forms:
        return 'error'

    if (type(spec) == int and spec == -1) or \
            (type(spec) == list and len(spec) != 0 and spec[0] == '?'):
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


"""
# Feature #2
"""


def get_episodes(spec=-1):
    url = 'https://rickandmortyapi.com/api/episode/'

    if spec != -1:
        if (type(spec) == int and spec != -1) or \
                (type(spec) == list and len(spec) != 0
                 and type(spec[0]) == int):
            url += str(spec).replace(' ', '') + '/'
        elif type(spec) == list and len(spec) != 0 and spec[0] == '?':
            url += '?' + spec[1]
            for f in spec[2:]:
                url += '&' + f
        else:
            return 'error'

    r = requests.get(url)
    forms = json.loads(r.content.decode())
    if type(forms) == dict and 'error' in forms:
        return 'error'

    if (type(spec) == int and spec == -1) or \
            (type(spec) == list and len(spec) != 0 and spec[0] == '?'):
        forms = forms['results']
    elif type(spec) == int and spec != -1:
        forms = [forms]

    all_forms = []
    curr_form = []

    episode_keys = ['id', 'name', 'air_date', 'episode']
    for i in range(len(forms)):
        curr_val = ''
        episode = forms[i]
        if 'id' not in episode:
            continue
        for key in episode_keys:
            if key in episode:
                curr_val = str(episode[key])
            else:
                curr_val = ''
            curr_form.append(curr_val.replace('\n', ' '))

        all_forms.append(curr_form)
        curr_form = []
    return all_forms
