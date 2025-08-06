from flask import Flask, request
from youtube_transcript_api import YouTubeTranscriptApi
import json

app = Flask(__name__)

@app.route("/transcript", methods=["GET"])
def extract_transcript_details():
    video_id = request.args.get("video_id")
    if not video_id:
        return json.dumps({"error": "Missing video_id parameter"}), 400

    try:
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
        return json.dumps(transcript_text)
    except Exception as e:
        return json.dumps({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
