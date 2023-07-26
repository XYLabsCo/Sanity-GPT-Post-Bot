import openai
import re
import requests
import json
import uuid
import schedule
import time
import datetime
from slugify import slugify

def job():
    unique_key = str(uuid.uuid4())

    # Set the OpenAI API key
    openai.api_key = "YOUR-KEY-HERE"

    # Set the prompt for the GPT
    prompt = "YOUR-PROMPT-HERE'"

    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", #Choose your GPT model
    messages=[
            {
                "role": "system",
                "content": "You are a professional writer."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    # Extract the content of the last message from the assistant role
    output = response['choices'][0]['message']['content']

    # Extract the (title) and the rest of the text as the content
    match = re.match(r"(.*?)(\n.*)", output.strip(), re.DOTALL)
    title, content = match.groups()
    content = content.strip()

    # Prepare the blog post // Update to your own Sanity schema
    doc = {
        "_type": "post",
        "title": title,
        "slug": {
            "_type": "slug",
            "current": slugify(title)
        },
        "author": {
            "_type": "reference",
            "_ref": "2845f33a-f596-4234-82b2-e33e71a00a5a"
        },
        "categories": [
            {
                "_type": "reference",
                "_key": str(uuid.uuid4()),
                "_ref": "09a2198c-b1e3-4051-8246-87f464ee3218"
            }
        ],
        "publishedAt": datetime.datetime.now().isoformat(),
        "body": [
            {
                "_type": "block",
                "_key": unique_key,
                "children": [
                    {
                        "_type": "span",
                        "_key": str(uuid.uuid4()),
                        "text": content
                    }
                ],
                "markDefs": []
            }
        ]
    }

    # Set your Sanity project ID, dataset, and token
    project_id="PROJECT-ID"
    dataset="DATASET-NAME"
    token="API-KEY"

    # Create the headers for the request
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    # Make the request to the Sanity API
    response = requests.post(f"https://{project_id}.api.sanity.io/v2021-06-07/data/mutate/{dataset}", headers=headers, data=json.dumps({
        "mutations": [
            {
                "create": doc
            }
        ]
    }))

    # Print the status code and content of the response
    print("Status code:", response.status_code)
    print("Response content:", response.content)
    print("Post Created!")

# Run the job once immediately upon script start
job()

# Run job every 10 minutes, change to your requirements
schedule.every(10).minutes.do(job)

while True:
    # Checks whether a scheduled task is pending to run or not
    schedule.run_pending()
    time.sleep(1)

