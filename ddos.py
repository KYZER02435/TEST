import requests
from concurrent.futures import ThreadPoolExecutor
import time

def make_request(url):
    """Function to perform a GET request to the specified URL."""
    while True:  
        try:
            response = requests.get(url)
            print(f"Response Code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Request failed: {e}")
        time.sleep(0.1)  

def main():
    url = input("Enter the URL to test: ").strip()
    num_threads = int(input("Enter the number of threads: ").strip())

    if not url.startswith('http://') and not url.startswith('https://'):
        print("Invalid URL. Please enter a URL starting with 'http://' or 'https://'.")
        return

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(make_request, url) for _ in range(num_threads)]
        
        for future in futures:
            future.result()  

    print("Load testing completed.")  

if __name__ == '__main__':
    main()
