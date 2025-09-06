# Short URL Service

A simple Python Flask API service with two endpoints.

## API Endpoints

### GET /
Returns a simple "Hello World" message.

**Response:**

Hello World


### POST /message
Logs an incoming message to the console.

**Request Body:**
json
{
  "message": "Your message here"
}


**Response:**
json
{
  "status": "success", 
  "message": "Message logged successfully"
}


## Running Locally

1. Install dependencies:

pip install -r requirements.txt


2. Run the application:

python app.py


The API will be available at `http://localhost:5000`

## Testing

Run the unit tests:

python -m unittest test_app.py -v


## Docker

Build and run with Docker:

docker build -t shorturlsvc .
docker run -p 5000:5000 shorturlsvc


## CI/CD

The project includes a GitHub Actions workflow that:
- Runs unit tests
- Builds a Docker image
- Pushes to Docker Hub

The workflow is triggered on:
- Manual dispatch (`workflow_dispatch`)
- Push to main branch

Make sure to set up the following secrets in your GitHub repository:
- `DOCKER_USERNAME`: Your Docker Hub username
- `DOCKER_PASSWORD`: Your Docker Hub password/token
