import requests
import csv

res=requests.get("https://jsonplaceholder.typicode.com/posts/")

def fetch_and_print_posts():
    if res.status_code == 200:
        API_Data = res.json()
        for key in API_Data:
            title = key['title']
            print(title)
    else:
        print(res.status_code)


def fetch_and_save_posts():
        csv_file = "posts.csv"
        if res.status_code == 200:
            with open(csv_file, "w") as f:
                filenames = ['id','title','body'] 
                API_Data = res.json()
                with open(csv_file, "w") as f:
                    writer=csv.DictWriter(f,fieldnames=filenames )
                    writer.writeheader()
                    for key in API_Data:
                        id = key['id']
                        title = key['title']
                        body = key['body']
                        writer.writerow({'id':id, 'title':title, 'body':body})
        else:
            print(res.status_code)





fetch_and_print_posts()
fetch_and_save_posts()