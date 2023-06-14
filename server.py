# Import the Secret Manager client library.
from google.cloud import secretmanager
from os import environ

# GCP project in which to store secrets in Secret Manager.
project_id = environ.get("PROJECT_ID")

# ID of the secret to create.
secret_id = environ.get("SECRET_ID")

# Create the Secret Manager client.
client = secretmanager.SecretManagerServiceClient()

# Build the parent name from the project.
parent = f"projects/{project_id}"

# Access the secret version.
response = client.access_secret_version(
    request={"name": f"{parent}/secrets/{secret_id}/versions/latest"}
)

payload = response.payload.data.decode("UTF-8")
print(f"Name: {response.name}, Payload: {payload}")

from sanic import Sanic

app = Sanic("MyHelloWorldApp")


@app.route("/")
async def hello_world(request):
    response = client.access_secret_version(
        request={"name": f"{parent}/secrets/{secret_id}/versions/latest"}
    )

    return response.payload.data.decode("UTF-8")

