import requests
import json

def test_client_api():
    """Test if client API can be called successfully"""
    url = "http://localhost:5000/api/client"
    
    try:
        # 创建会话并禁用环境变量中的代理设置
        session = requests.Session()
        session.trust_env = False
        
        # 使用会话发送POST请求
        response = session.post(url, json={"query": "some_data"})
        
        # 打印状态码和响应内容
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