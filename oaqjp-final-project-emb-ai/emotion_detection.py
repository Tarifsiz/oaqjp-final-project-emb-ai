import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: Received status code {response.status_code}. Details: {response.text}"
            
    except requests.exceptions.RequestException as e:
        return f"Connection error: {e}"
