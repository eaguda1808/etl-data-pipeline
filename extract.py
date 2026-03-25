import requests

def fetch_data():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    data = fetch_data()
    print(data[:2])  # preview