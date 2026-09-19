from emotion_detection import emotion_detector
import json

test_text = "I love this new technology."

print(f"Analyzing text: '{test_text}'...\n")

analysis_result = emotion_detector(test_text)

print(json.dumps(analysis_result, indent=4))
