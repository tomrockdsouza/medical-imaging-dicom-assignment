# Medical Imaging Coding Assessment

## Getting Started

To run this project, follow these steps:

1. Navigate to the project folder.

`cd project-folder`

Start the project using Docker Compose.

`docker-compose up -d`

This will create and start the necessary containers in the background.

To delete all resources after running and testing the project, run the following command:

`docker-compose down -v --rmi local`

Configuration
You can configure the server threshold value in the docker-compose.yml file.

Usage
Once the container is up and running, you can access the project at http://localhost.

API Documentation
The detailed information on how to use the API can be found in the Swagger OpenAPI documentation available at http://localhost/docs.

