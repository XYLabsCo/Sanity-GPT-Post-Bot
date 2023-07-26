# OpenAI GPT-based Blog Post Generator

This Python script utilizes the OpenAI GPT model (in this case, gpt-3.5-turbo) to generate blog posts and automatically upload them to a Sanity.io project. This tool could be helpful for content creators, marketers, and developers looking for an automated solution to create and upload blog content.

## Requirements

- Python 3.6+
- OpenAI Python v0.27.0
- python-slugify
- schedule
- requests

You can install these requirements with pip:

```bash
pip install openai python-slugify schedule requests

## Setup & Usage
First, you need to clone this repository to your local machine. You can do this with the following command:

```bash
git clone <repository-url>

Then navigate to the project directory:

```bash
cd <project-directory>

Replace the placeholder values in the code with your specific details. For instance, you should replace:

- "YOUR-KEY-HERE" with your OpenAI API key.
- "YOUR-PROMPT-HERE" with the prompt you want the GPT model to expand on.
- "PROJECT-ID", "DATASET-NAME", and "API-KEY" with your Sanity project ID, dataset, and token.

Then, you can run the script using Python:

```bash
python <script-name>.py

## How it works
The script works as follows:

- It sends a chat completion request to OpenAI's GPT model.
- Extracts the content of the last message from the assistant role.
- Uses regex to extract the title and the rest of the text as content.
- Prepares a blog post according to the Sanity schema.
- Makes a request to the Sanity API to upload the post.
- The function job() runs immediately upon script start and then every 10 minutes.
Please make sure to adjust the timing and prompts to your own requirements.

## Caution
Make sure to keep your OpenAI API key, Sanity API key, and all other sensitive data secure.
This script will continue to run and post to your Sanity project every 10 minutes. Make sure to monitor it to avoid flooding your project with posts.
The OpenAI API usage can result in costs. Be aware of your usage and manage it accordingly.

## License
This project is licensed under the terms of the MIT license.