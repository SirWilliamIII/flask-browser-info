from flask import Flask, request, render_template, jsonify, make_response
from dotenv import load_dotenv
import os
import base64


load_dotenv()
encoded_key = os.getenv('PRIVATE_KEY')
private_key = base64.b64decode(encoded_key).decode('utf-8')

app = Flask(__name__)


@app.route('/', methods=['GET'])
def fingerprint():
    client_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    accept_language = request.headers.get('Accept-Language')
    referer = request.headers.get('Referer', 'None')
    cookies = request.headers.get('Cookie', 'None')

    # Create a simple fingerprint
    fingerprint = {
        'ip': client_ip,
        'user_agent': user_agent,
        'accept_language': accept_language,
        'referer': referer,
        'cookies': cookies,
    }
    response = make_response("Cookie is set")
    response.set_cookie('client_id', 'unique_id', max_age=30*24*60*60)
    print(response.get_data)
    
    print(f"Client fingerprint: {fingerprint}")
    return jsonify(fingerprint)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

