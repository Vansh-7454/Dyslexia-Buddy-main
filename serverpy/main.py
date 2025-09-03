from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
import jiwer
import librosa
import joblib
import numpy as np

# ---------------- Step 2: Ensure upload folder exists ----------------
UPLOAD_DIR = "temp_uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# ---------------- FastAPI App ----------------
app = FastAPI()
model0 = joblib.load("dyslexia_model.pkl")

# ---------------- CORS Middleware ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- GET / route ----------------
@app.get("/")
async def root():
    return {"message": "App is working"}

# ---------------- POST /transcribe/ route ----------------
@app.post("/transcribe/")
async def transcribe_audio(file: UploadFile = File(...)):
    import whisper

    # 1️⃣ Save uploaded file
    file_path = os.path.join(UPLOAD_DIR, f"temp_{file.filename}")
    with open(file_path, "wb") as f:
        f.write(await file.read())

    # 2️⃣ Load audio safely with librosa
    try:
        audio, sr = librosa.load(file_path, sr=None)
    except Exception as e:
        return {"error": f"Librosa failed to load audio: {str(e)}"}

    # 3️⃣ Load Whisper model
    model = whisper.load_model("tiny")  # tiny is fast for testing

    # 4️⃣ Transcribe audio
    result = model.transcribe(file_path)

    # 5️⃣ Optional: delete file after use
    os.remove(file_path)

    # 6️⃣ Calculate error rate
    actualtext = 'The fox ran fast through the fog.He saw five frogs near a log.One frog fell and flipped on a rock.“Funny frog!” said the fox, with a smile.The wind whooshed, and all frogs hopped away'
    transcribedtext = result["text"]
    error_rate = jiwer.wer(actualtext, transcribedtext)

    # 7️⃣ Detect pauses
    pauses = librosa.effects.split(audio, top_db=20)
    long_pauses = [pause[1] - pause[0] for pause in pauses if (pause[1] - pause[0]) > 2]

    # 8️⃣ Reading speed
    words = len(transcribedtext.split())
    duration_seconds = librosa.get_duration(y=audio, sr=sr)
    reading_speed = (words / duration_seconds) * 60

    # 9️⃣ Predict using dyslexia model
    input_data = np.array([[reading_speed, error_rate, len(long_pauses)]])
    prediction = model0.predict(input_data)[0]

    # 10️⃣ Return results
    return {
        "text": result["text"],
        "prediction": prediction
    }

# ---------------- Run server ----------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Use environment port if exists
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
