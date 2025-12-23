import requests

def hello_with_requests():
	response = requests.get("https://api.github.com")
	if response.status_code == 200:
		print("Hello, GitHub API! Status:", response.status_code)
	else:
		print("Failed to reach GitHub API. Status:", response.status_code)

if __name__ == "__main__":
	hello_with_requests()
