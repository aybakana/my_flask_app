from flask import Flask, request, jsonify
import whisper

app = Flask(__name__)
model = whisper.load_model("base")

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    file = request.files['file']
    file.save("input_audio.wav")
    result = model.transcribe("input_audio.wav")
    return jsonify({"transcription": result["text"]})

if __name__ == '__main__':
    # Use the PORT environment variable or default to 5000
    port = int(os.environ.get('PORT', 5000))
    # Bind to 0.0.0.0 so the service is accessible on Render
    app.run(host='0.0.0.0', port=port)
