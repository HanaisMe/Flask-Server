## Mocking API

Setup
- (Flask) `$ pip3 install flask`
- (Flask-RESTful) `pip3 install flask-restful`

Run REST API
1. `$ cd ../flask-mockAPI` (Your directory)
2. `$ python3 mock_server.py`

Request via terminal
- GET
    - `$curl http://127.0.0.1:5000/`
    - `$curl -v http://127.0.0.1:5000/`
- POST
    - `$curl -H "Content-Type: application/json" -X POST -d '{"item": "Ginger Ale", "price": "2000 won"}' http://127.0.0.1:5000/`
    
References
- https://palletsprojects.com/p/flask/
- https://flask.palletsprojects.com/en/1.1.x/
- https://flask-restful.readthedocs.io/en/latest/
