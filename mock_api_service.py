import json
import os
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
# 启用CORS，允许所有来源的请求
CORS(app)

MOCK_DATA_DIR = "mock_data"

@app.route('/api/client', methods=['POST'])
def get_client_information():
    """返回客户信息的mock数据"""
    file_path = os.path.join(MOCK_DATA_DIR, "clientInformation.json")
    
    # 检查文件是否存在
    if not os.path.exists(file_path):
        return jsonify({"error": f"Mock数据文件不存在: {file_path}"}), 404
    
    # 读取并返回JSON数据
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            mock_data = json.load(f)
        return jsonify(mock_data)
    except Exception as e:
        return jsonify({"error": f"读取mock数据出错: {str(e)}"}), 500

if __name__ == '__main__':
    # 确保mock_data目录存在
    if not os.path.exists(MOCK_DATA_DIR):
        os.makedirs(MOCK_DATA_DIR)
        
    # 创建示例JSON文件(如果不存在)
    example_path = os.path.join(MOCK_DATA_DIR, "clientInformation.json")
    if not os.path.exists(example_path):
        with open(example_path, 'w', encoding='utf-8') as f:
            json.dump({
                "clientId": "12345",
                "name": "测试客户",
                "address": "北京市海淀区",
                "phone": "13800138000"
            }, f, ensure_ascii=False)
    
    app.run(debug=True, port=5000) 