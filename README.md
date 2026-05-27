🌿 Kisan Mitra AI (किसान मित्र)Your Digital Farming Companion – Real-time crop disease diagnosis powered by an optimized, 
lightweight ONNX computer vision engine.

📌 Project OverviewKisan Mitra AI empowers smallholder farmers with instant botanical insights.
By uploading a photo of an infected leaf, the system reads visual array layers,
running rapid inference against a deep learning backend to return crop disease classifications and actionable remediation plans.
To bypass memory bottlenecks on free cloud hosting tiers,
the core model has been compiled from heavy TensorFlow structures into a highly streamlined ONNX (Open Neural Network Exchange) format.

🌟 Key Features:
📸 Leaf Diagnostic Scanner: Interactive web workspace with an animated laser scanner visual effect.
🔬 High-Speed Inference: Uses a light ONNX runtime engine to deliver disease types and confidence intervals instantly.
🌱 Actionable Remediation: Provides localized biological cause summaries and step-by-step agricultural workflows.
🌾 Verified Crop Coverage: Built-in validation algorithms for high-value regional crops: Tomatoes, Potatoes, Corn/Maize, and Apples.

🛠️ Technology Stack 
Layer                 Component                Purpose 
Frontend UI    HTML5, CSS3, JavaScript (ES6+)  Fully responsive dashboard layout with asynchronous API fetch.
Icons & Brand Native Vector Inline SVGs        High-fidelity customized cultural branding assets.
Backend Core  Python, Flask, Gunicorn          High-performance production WSGI web API routing gateway.
Inference Engine ONNX Runtime (.onnx)          Ultra-lightweight matrix mathematical engine (<30MB RAM footprint).
Hosting       (API)Render (PaaS Deployment)    Cloud computing deployment host environment.
Hosting (UI)  Vercel / GitHub Pages            Global CDN static layout delivery.

📁 Repository Structure
📁 kisan-mitra-backend/
├── .gitignore               # Excludes python cache and heavy local weights
├── .python-version          # Locks the cloud server to a stable Python 3.11 engine
├── app.py                   # Flask API routing and ONNX inference logic
├── crop_disease_model.onnx  # Optimized, lightweight model weights
├── index.html               # Frontend dashboard user interface
├── requirements.txt         # Memory-optimized production library dependencies
└── train.py                 # Initial Deep Learning training pipeline algorithm (TensorFlow base)
💻 Architecture & Optimization (app.py & requirements.txt)

🧠 ONNX Memory Optimization
Instead of running heavy TensorFlow libraries (tf.keras.models.load_model),
which require over 400MB of RAM and crash free servers, app.py instantiates an onnxruntime.InferenceSession.
This model consumes less than 30MB of RAM, making it completely immune to Out-Of-Memory (OOM) deployment crashes.

📋 Clean Production Dependencies
The requirements.txt manifest strips out massive analytical frameworks,
utilizing only pre-compiled wheels for fast installation:
Flask==3.0.3
flask-cors==5.0.1
gunicorn==23.0.0
onnxruntime==1.17.1
numpy==1.26.4
pillow==11.1.0
werkzeug==3.0.4

⚓ Dynamic Port Binding
The backend uses dynamic configuration environment flags to cleanly switch between production routing and local hosting setups:Pythonimport os
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    
🚀 Local Installation
Clone the project:
git clone https://github.com/RajS45/kisan-mitra-backend.git
cd kisan-mitra-backend
Setup virtual environment & install packages:
python -m venv venv
# On Windows:
venv\Scripts\activate
pip install -r requirements.txt
Run local server:Bashpython app.py
The local endpoint will listen at http://127.0.0.1:5000/predict.

🌐 Cloud Deployment (Render Settings)
Runtime Environment: Python
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app
Environment Variables: Set PYTHON_VERSION = 3.11.10 to ensure pre-compiled ONNX wheel compatibility.
