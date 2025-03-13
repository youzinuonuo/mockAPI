import requests
import json

def test_client_api():
    """Test if client API can be called successfully"""
    url = "http://localhost:5000/api/client"
    
    try:
        # Send POST request
        response = requests.post(url, json={"query": "some_data"})
        
        # Print status code and response content
        print(f"Status code: {response.status_code}")
        print(f"Response content: {json.dumps(response.json(), ensure_ascii=False, indent=2)}")
        
        if response.status_code == 200:
            print("API call successful!")
        else:
            print(f"API call failed, status code: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("Connection failed, please make sure the server is running")
    except Exception as e:
        print(f"Error during test: {str(e)}")

if __name__ == "__main__":
    test_client_api()