import requests

def fetchrandomquote():
    url="https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
    res=requests.get(url)
    data=res.json()
    joke=data["data"]["content"]
    print(joke)


def main():
    fetchrandomquote()
if __name__=="__main__":
    main()