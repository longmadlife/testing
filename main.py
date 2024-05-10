# from flask import Flask, request, jsonify,render_template
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# uabval = ""

# @app.route('/', methods=['POST','GET', 'OPTIONS'])
# def home():
#     return render_template('index.html')

# def receive_data():
#     if request.method == 'GET':
#         # Read data from the text file
#         with open(r'uab_values.txt', 'r') as f:
#             uab_values = f.readlines()
#         # Remove newline characters and create a list of uab values
#         uab_values = [value.strip() for value in uab_values]
#         return jsonify({'uab_value': uab_values[0]})
    
#     if request.method == 'OPTIONS':
#         # Handle CORS preflight request
#         return '', 204

#     data = request.get_json()
#     uab_value = data.get('uab')

#     uabval = uab_value
#     print('Received uab value from client:', uab_value)
#     with open(r'uab_values.txt', 'w') as f:
#         f.write(uab_value + '\n')

#     # Respond to the client
#     return jsonify({'message': 'Data received and saved successfully'})
    

# if __name__ == '__main__':
#     app.run(host='0.0.0.0',debug=True, port=5000)
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Apply CORS to all routes

@app.route('/', methods=['POST', 'GET', 'OPTIONS'])
def handle_requests():
    if request.method == 'GET':
        # Serve the homepage
        return render_template('index.html')
    
    elif request.method == 'OPTIONS':
        # Handle CORS preflight request
        return '', 204

    elif request.method == 'POST':
        # Handle POST requests for UAB values
        try:
            data = request.get_json()
            uab_value = data.get('uab', 'No UAB value provided')  # Default message if 'uab' not found
            print('Received uab value from client:', uab_value)
            
            # Append new UAB value to the file
            with open('uab_values.txt', 'a') as f:
                f.write(uab_value + '\n')
            
            return jsonify({'message': 'Data received and saved successfully'})
        
        except Exception as e:
            return jsonify({'error': str(e)}), 500  # Return server error status code

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)

