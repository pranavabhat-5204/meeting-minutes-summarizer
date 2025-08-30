# meeting-minutes-summarizer
# Meeting Minutes Summarizer

**Automatically convert meeting recordings or transcripts into concise summaries and action items—no deployment needed. Runs seamlessly on Google Colab or locally.**

##  Features

- **Speech-to-Text (Whisper):** Transcribe MP3, WAV, or MP4 (audio extracted) into text.
- **Summarization:** Generate concise meeting overviews using Hugging Face models (BART/T5).
-  **Action Item Detector:** Extract `will`, `must`, `should`, `deadline`, etc., to surface tasks and accountability.
-  **Dual Input Modes:** Upload audio/video file **or** paste raw transcript text.
-  **Run Anywhere:** Works in Google Colab or local setups—no API keys or deployment required.

---

##  Quick Start

### Option 1: Run in Google Colab (recommended)

1. Open the Colab notebook:


2. Execute the following cells in order:
- **Install dependencies**:
  ```bash
  !pip install openai-whisper transformers spacy
  !python -m spacy download en_core_web_sm
  !apt-get install -y ffmpeg
  ```
- **Load models** (Whisper, summarizer, spaCy).
- **Define helper functions**: `transcribe_audio`, `summarize_text`, `extract_action_items`, `meeting_minutes`.
- **Upload an audio/video file**, e.g., `meeting.mp4` or `meeting.mp3`:
  ```python
  from google.colab import files
  uploaded = files.upload()
  filename = list(uploaded.keys())[0]
  result = meeting_minutes(file_path=filename)
  ```
- Or input raw text:
  ```python
  sample_text = "...your transcript here..."
  result = meeting_minutes(transcript=sample_text)
  ```
- Review the printed output:
  - **Transcript**
  - **Summary**
  - **Action Items**

### Option 2: Run Locally (Linux / macOS)

1. Clone the repository:

git clone https://github.com/yourusername/meeting-minutes-summarizer.git
cd meeting-minutes-summarizer
