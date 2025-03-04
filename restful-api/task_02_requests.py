import requests
res=requests.get("https://jsonplaceholder.typicode.com/posts/")

def fetch_and_print_posts():
    if res.status_code == 200:
        API_Data = res.json()
        for key in API_Data:
            title = key['title']
            print(title)
    else:
        print(res.status_code)


# def fetch_and_save_posts():




fetch_and_print_posts()