import requests
import csv

def fetch_and_print_posts():
    """
    Fetch posts from JSONPlaceholder and print their titles.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    # Send a GET request to the API
    response = requests.get(url)

    # Print the status code
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        # Parse the response body as JSON
        posts = response.json()
        # Iterate and print titles
        for post in posts:
            print(post.get('title'))

def fetch_and_save_posts():
    """
    Fetch posts and save specific fields (id, title, body) to a CSV file.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        # Structure the data: keep only id, title, and body
        # Using a list comprehension for efficiency
        data_to_save = [
            {'id': post['id'], 'title': post['title'], 'body': post['body']}
            for post in posts
        ]

        # Write to CSV
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write header and rows
            writer.writeheader()
            writer.writerows(data_to_save)
