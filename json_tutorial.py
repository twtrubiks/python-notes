import json

if __name__ == "__main__":
    load_data = '''
    {
    "maps": [
        {
            "id": "blabla",
            "iscategorical": "0"
        },
        {
            "id": "blabla",
            "iscategorical": "0"
        }
    ],
    "masks": {
        "id": "twtrubiks"
    },
    "om_points": "value",
    "parameters": {
        "id": "valore"
    }
}

    '''
    data = json.loads(load_data)

    print('data[maps]: {}'.format(data['maps']))
    print('data[masks][id]: {}'.format(data['masks']['id']))
