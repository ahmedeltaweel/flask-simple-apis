from json import dumps, loads


def get_items():
    file = open('test.json', 'r')
    items = file.read()
    file.close()
    return loads(items)


def update_file(content):
    file = open('test.json', 'w')
    items = file.write(dumps(content))
    file.close()
