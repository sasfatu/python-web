from flask import Flask, jsonify
from datetime import datetime
import requests

app = Flask(__name__)

def check_database():
  return False

def check_external_service():
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        return response.status_code == 200
    except:
        return False
    
@app.route('/api/v1/details')
def get_details():
    date_time = datetime.now().isoformat()
    return jsonify({
        'name': 'Python App',
        'version': '1.0.0',
        'description': 'A simple Python web application',
        'datetime': date_time
    })

@app.route('/health', methods=['GET'])
def health_check():
    db_status = check_database()
    api_status = check_external_service()

    return jsonify({
        'database': 'up' if db_status else 'down',
        'external_api': 'up' if api_status else 'down'
    })

if __name__ == "__main__":
    # app.run(debug=True)
    app.run( host='0.0.0.0', port=5050, debug=True )