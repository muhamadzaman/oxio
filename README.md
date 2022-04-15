# Setup
- The app/service is built using Flask (python)
- Make sure you have python 3 installed in your system
- Navigate to the directory containing app.py
- Create a python virtual environment:
```
python3 -m venv venv
```
- Activate the virtual environment:
```
source venv/bin/activate
```
- Install requirements:
```
pip install -r requirements.txt
```
- Run the server using:
```
flask run
```
- The server is up now on http://127.0.0.1:5000
- The endpoint of interest is http://127.0.0.1:5000/v1/phone-numbers
- The endpoint can be access with params such as http://127.0.0.1:5000/v1/phone-numbers?phoneNumber=12125690123&countryCode=US
- Run test using (make sure you are in the same directory as app.py)
```
pytest
```

## Additional Notes
- Flask was used to build the app. It was ideal to build a small service like this since its a lightweight micro-framework. This app/endpoint can be seen as a small microservice and flask is practical for building microservices like this since it is lightweight and does not come with a lot of overheads out of the box
- For deploying to production, AWS Lambda is a good choice due to the fact that this is a small microservice and can be invoked whenever needed. By choosing AWS Lambda, we will also control the cost since it only charges per invocation.
- Additional improvements is to have more robust validation checks and potentially add more information about the phone number by consuming third party APIs
