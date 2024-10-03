from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from the backend!'

# New route to handle form data
@app.route('/submit', methods=['POST'])
def submit_form():
    # Get the form data sent via POST
    name = request.form.get('name')

    # Return a simple message with the submitted data
    return f'Thank you, {name}, for submitting the form!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
