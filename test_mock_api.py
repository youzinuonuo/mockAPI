import unittest
import requests
import json
import os
import time
import subprocess
import signal
import sys

class TestMockAPI(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """启动Mock API服务"""
        # 确保mock_data目录存在
        if not os.path.exists("mock_data"):
            os.makedirs("mock_data")
        
        # 创建测试用的JSON文件
        test_data = {
            "users": [
                {"id": 1, "name": "张三", "email": "zhangsan@example.com"},
                {"id": 2, "name": "李四", "email": "lisi@example.com"}
            ]
        }
        
        with open("mock_data/users.json", "w", encoding="utf-8") as f:
            json.dump(test_data, f, ensure_ascii=False)
            
        # 启动服务器进程
        cls.server_process = subprocess.Popen(
            [sys.executable, "mock_api_service.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        
        # 等待服务器启动
        time.sleep(2)
    
    @classmethod
    def tearDownClass(cls):
        """关闭Mock API服务"""
        cls.server_process.send_signal(signal.SIGTERM)
        cls.server_process.wait()
    
    def test_health_check(self):
        """测试健康检查接口"""
        response = requests.get("http://localhost:5000/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})
    
    def test_get_users(self):
        """测试获取用户列表"""
        response = requests.get("http://localhost:5000/users")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("users", data)
        self.assertEqual(len(data["users"]), 2)
        self.assertEqual(data["users"][0]["name"], "张三")
    
    def test_nonexistent_endpoint(self):
        """测试不存在的接口"""
        response = requests.get("http://localhost:5000/nonexistent")
        self.assertEqual(response.status_code, 404)
        self.assertIn("error", response.json())

def test_client_api():
    """测试客户信息API"""
    url = "http://localhost:5000/api/client"
    
    # 发送POST请求
    response = requests.post(url, json={"query": "some_data"})
    
    # 打印状态码和响应内容
    print(f"状态码: {response.status_code}")
    print(f"响应内容: {json.dumps(response.json(), ensure_ascii=False, indent=2)}")
    
    # 简单验证
    assert response.status_code == 200, "API请求失败"
    assert "clientId" in response.json(), "响应中缺少clientId字段"
    
    print("测试通过!")

if __name__ == "__main__":
    unittest.main()
    test_client_api() 