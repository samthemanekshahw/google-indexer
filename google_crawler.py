import requests
import random
import time

# Function to ping Googlebot by sending GET requests with various headers
def ping_google_crawler(url):
    """Simulate a request to the URL as if Googlebot is crawling it."""
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        'Mozilla/5.0 (Linux; Android 9; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36'
    ]
    
    headers = {
        'User-Agent': random.choice(user_agents),
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            print(f"Successfully pinged Googlebot with: {url}")
        else:
            print(f"Failed to ping {url}. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error with URL {url}: {e}")

# Function to read URLs from the file
def read_urls(file_path):
    """Read URLs from a file."""
    with open(file_path, 'r') as file:
        urls = [line.strip() for line in file.readlines()]
    return urls

def main():
    # Read URLs from file
    urls = read_urls('url.txt')
    
    # Loop through all URLs and perform actions
    for url in urls:
        ping_google_crawler(url)
        
        # Delay between requests to avoid overwhelming servers
        time.sleep(random.uniform(1, 2))

if __name__ == "__main__":
    main()
