Build the Docker image with:

docker build -t app .


Run the Docker container locally with:

docker run -p 8000:80 app

Build and run with docker compose:

docker compose up

To stop with docker compose:

docker compose down