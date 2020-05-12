

@speedTest(iterations=10)
def search():
    import requests
    s = requests.get('https://google.com/')
    return s
search()
