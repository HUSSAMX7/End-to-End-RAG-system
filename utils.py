import json
import requests
from langdetect import detect

def call_llm(prompt, max_tokens=100):
    postData = {
        "prompt": prompt,
        "max_tokens": max_tokens,
        "temperature": 0.1,
        "model": "llama3:8b",
        "stream": False
    }

    ollamaUrl = "http://localhost:11434/api/generate"

    llmResponse = requests.post(ollamaUrl, json=postData)

    result = llmResponse.json()

    return result["response"]


def arabic_default_message(qestion):
    return """
    يبدو اني لم اتمكن من العثور على اجابت سؤال تعيده مره ثانية ؟ """


def english_default_message(qestion):
    return """
    I couldn't find an answer to your question, please repeat it again? """


def is_in_arabic(qestion):
    return detect(qestion) == "ar"

def get_default_language(qestion):
    if not is_in_arabic(qestion):
        return english_default_message(qestion)
    else:
        return arabic_default_message(qestion)
    
