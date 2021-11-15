import requests

def get_quote():
    url = "https://breaking-bad-quotes.herokuapp.com/v1/quotes"

    response = requests.get(url)

    if response.status_code != 200:
        return "No quote found"

    response = response.json()[0]

    return f'"{response["quote"]}" \n > {response["author"]}'

if __name__=="__main__":
    print(get_quote())