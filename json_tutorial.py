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

    data_dump = json.dumps(data)
    print('json.dumps:', data_dump)

    # 排除空格
    print(json.dumps(data, separators=(",", ":")))

    ascii_data = {"name": "你好", "age": 10}
    # 将 ensure_ascii 设置为 False，以保留非 ASCII 字符
    print(json.dumps(ascii_data, ensure_ascii=False))
    print(json.dumps(ascii_data, ensure_ascii=True)) # dafault True