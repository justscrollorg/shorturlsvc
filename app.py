from flask import Flask, request, jsonify
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    """Simple GET endpoint that returns Hello World from Germany"""
    return "Hello World from Germany"

@app.route('/message', methods=['POST'])
def log_message():
    """POST endpoint that logs incoming message to console"""
    try:
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({"error": "Missing 'message' field in request body"}), 400
        
        message = data['message']
        logger.info(f"Received message: {message}")
        
        return jsonify({"status": "success", "message": "Message logged successfully"}), 200
    
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
