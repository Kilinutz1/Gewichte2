import requests

def get_weigts():
    url = 'https://bwinf.de/fileadmin/user_upload/gewichtsstuecke0.txt'
    result = requests.get(url)
    doc = result.content.decode("utf-8").split()
    weights = []
    for i in range(1, len(doc), 2):
        weights.append([doc[i], doc[i + 1]])
    return weights

def main():
    weights = get_weigts()
    return

if __name__ == '__main__':
    main()
