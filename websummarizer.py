import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from openai import OpenAI
from typing import Type

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")
elif not api_key.startswith("sk-"):
    raise ValueError("Invalid API key format. Please ensure it starts with 'sk-'.")
else:
    print("API key is valid and loaded successfully.")

# Some websites need you to use proper headers when fetching them:
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

openai = OpenAI()


class ReadersDigest:

    def __init__(self, url):
        """Initialize the ReadersDigest class with a URL."""
        self.url = url
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")

        # Extract title
        self.title = soup.title.string if soup.title else "No title found"
        # Remove unwanted elements
        for element in soup.find_all(['script', 'style', 'img', 'input', 'iframe', 'nav', 'footer']):
            element.decompose()
            
        self.text = " ".join(soup.get_text().split())


    def define_system_prompt(self):
        """Define the system prompt for the OpenAI API."""

        return f"""
        You are a helpful assistant that analyzes the contents of a website and summarizes web pages,
        ignoring text that might be navigation related. Respond in markdown. 
        Your task is to summarize the content of the web page at the following URL: {self.url}.
        The title of the page is: {self.title}.
        The content of the page is as follows:
        {self.text}
        """
    
    def define_user_prompt(self, website):
        """Define the user prompt for the OpenAI API."""
        user_prompt = f'''You are looking at a website titled {website.title}'''
        user_prompt += f'''\n\nThe content of the page is as follows:\n{website.text} 
        \n\nPlease provide a very brief summary of this website in markdown. 
        If it includes news or announcements, then summarize these too..'''
        
        return user_prompt

    def summarize(self, website: 'ReadersDigest'):
        """Summarize the content of the web page using OpenAI API."""

        messages = [
            {"role": "system", "content": self.define_system_prompt()},
            {"role": "user", "content": self.define_user_prompt(website)}
        ]

        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )
        return response.choices[0].message.content.strip()
    
# if __name__ == "__main__":
#     url = "https://medium.com/@senendu5/what-really-is-the-voting-population-of-nigeria-b4e86d976765"
#     website = ReadersDigest(url)
#     summary = website.summarize(website)
#     print(summary)