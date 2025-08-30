!pip install openai-whisper transformers spacy
!python -m spacy download en_core_web_sm
!apt-get install ffmpeg

import whisper
from transformers import pipeline
import spacy


whisper_model = whisper.load_model("base")   # <-- defines whisper_model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
nlp = spacy.load("en_core_web_sm")
def transcribe_audio(file_path: str) -> str:

    converted = "converted.wav"
    !ffmpeg -i "{file_path}" -vn -ar 16000 -ac 1 -ab 192k -f wav "{converted}" -y
    result = whisper_model.transcribe(converted)
    return result["text"]

def summarize_text(text: str, max_len: int = 150, min_len: int = 50) -> str:
    
    summary = summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)
    return summary[0]['summary_text']

def extract_action_items(text: str):
    
    doc = nlp(text)
    tasks = []
    for sent in doc.sents:
        if any(token.text.lower() in ["will", "must", "should", "assigned", "deadline", "due"]
               for token in sent):
            tasks.append(sent.text)
    return tasks

def meeting_minutes(file_path=None, transcript=None):
    if file_path:
        transcript = transcribe_audio(file_path)

    summary = summarize_text(transcript)
    action_items = extract_action_items(transcript)

    return {
        "Transcript": transcript,
        "Summary": summary,
        "Action Items": action_items
    }
