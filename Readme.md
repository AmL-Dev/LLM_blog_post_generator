# LLM Blog post generator

## Description

This app automatically produces blog posts on specified topics for specific readers using the Llama 2 model.

## Built Using

- [Python](https://www.python.org/)
- [langchain](https://pypi.org/project/langchain/)
- [streamlit](https://pypi.org/project/streamlit/)
- [Llama 2 model](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main)

## Installation

### Prerequisites

- Download the [llama-2-7b-chat.ggmlv3.q8_0.bin](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/resolve/main/llama-2-7b-chat.ggmlv3.q8_0.bin) model and save it in **models/** folder
- [Optinal] Create a python virtual environment with the required libraries:

```console
conda create -p venv python==3.9 --y
conda activate venv/
pip install -r requirements.txt
```

### Run project

1. Execute the app:

```console
streamlit run app.py
```

2. Write your input in the UI and submit

3. The blog post is generated

## Sources

[Llama 2 7B Chat - GGML](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML)

[Complete-Langchain-Tutorials](https://github.com/krishnaik06/Complete-Langchain-Tutorials/tree/main)
