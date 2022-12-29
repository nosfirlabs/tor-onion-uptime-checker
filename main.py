import requests

def check_tor_uptime(url):
    # Set the TOR proxy
    proxies = {
        "http": "socks5h://localhost:9050",
        "https": "socks5h://localhost:9050"
    }

    # Send a request to the URL through the TOR proxy
    try:
        response = requests.get(url, proxies=proxies)
        print(f"TOR URL is up, status code: {response.status_code}")
    except requests.exceptions.RequestException:
        print("TOR URL is down")

# Example usage
check_tor_uptime("http://duskgytldkxiuqc6.onion/")
