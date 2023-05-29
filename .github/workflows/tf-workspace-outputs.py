import os
import requests
import json

def get_current_state_version_outputs(organization, workspace, token):
    # Set up the API endpoint URL
    api_url = f"https://app.terraform.io/api/v2/workspaces/{workspaceid}/current-state-version-outputs"

    # Prepare the headers with the Terraform Cloud API token
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/vnd.api+json"
    }

    # Send the API request
    response = requests.get(api_url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        json_response = response.json()

        # Extract the outputs from the JSON response
        outputs = json_response["data"]

        # Log the outputs as JSON to stdout
        print(json.dumps(outputs, indent=4))

    else:
        # Log the error message to stdout
        print(f"Error: {response.status_code} - {response.text}")

# Set up your Terraform Cloud credentials
organization = os.getenv('TF_CLOUD_ORGANIZATION')
workspace = os.getenv('WORKSPACE_NAME')
token = os.getenv('TF_API_TOKEN')
workspaceid = os.getenv('WORKSPACE_ID')

# Call the function to retrieve and log the current state version outputs as JSON
get_current_state_version_outputs(organization, workspace, token)
