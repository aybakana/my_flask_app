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
    app.run(port=5000)
