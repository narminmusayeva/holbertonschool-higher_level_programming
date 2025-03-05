import requests
import csv


def fetch_and_print_posts():
    res=requests.get("https://jsonplaceholder.typicode.com/posts/")
    print(f"Status Code: {res.status_code}")

    
    if res.status_code == 200:
        API_Data = res.json()
        for key in API_Data:
            title = key['title']
            print(title)
    else:
        print(f"Failed to fetch data")



def fetch_and_save_posts():
        res=requests.get("https://jsonplaceholder.typicode.com/posts/")
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
                print("CSV file created successfully.")
        else:
            print(f"Failed to fetch data")