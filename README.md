# Website Summarizer 📚

A web application that generates concise summaries of web pages using OpenAI's GPT-4 API and Streamlit.

## Features

- Clean and user-friendly interface
- Handles various website structures
- Provides summary statistics (original length, summary length, reduction percentage)
- Advanced text cleaning and processing
- Markdown-formatted summaries

## Requirements

- Python 3.11+
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/websummarizer.git
cd websummarizer
```

2. Set up the environment using either conda:
```bash
conda env create -f environment.yml
conda activate llms
```

Or using pip:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

Run the Streamlit app:
```bash
streamlit run streamlit_ui.py
```

Then open your browser and navigate to `http://localhost:8501`

## How It Works

1. The application takes a URL as input
2. Fetches the webpage content using requests and BeautifulSoup
3. Cleans and processes the text
4. Uses OpenAI's GPT-4 to generate a concise summary
5. Displays the results with statistics

## Project Structure

- `streamlit_ui.py`: Frontend interface built with Streamlit
- `websummarizer.py`: Core summarization logic and API handling
- `environment.yml`: Conda environment configuration
- `requirements.txt`: Python package dependencies

## License

MIT License

## Contributing

Feel free to open issues or submit pull requests to improve the project.

