# 🛡️ AI-Powered Financial Fraud Detection System

An AI-powered web application that detects fraudulent credit card transactions using Machine Learning. Users can upload a CSV file containing transaction data, and the system predicts whether each transaction is legitimate or fraudulent.

---

## 🌐 Live Demo

**Frontend (Netlify)**  
https://ai-fraud-detectionn.netlify.app

**Backend API (Render)**  
https://project-pbel-3-0.onrender.com

---

## 📌 Features

- 🔍 Detects fraudulent credit card transactions
- 📂 Upload CSV datasets
- 🤖 Machine Learning prediction using Random Forest
- 📊 Interactive dashboard with prediction summary
- 📈 Pie chart visualization
- 📋 Preview of prediction results
- 📥 Download prediction results as CSV
- 🌐 Fully deployed online using Netlify & Render

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3
- Bootstrap 5
- JavaScript

### Backend
- Python
- Flask
- Flask-CORS
- Gunicorn

### Machine Learning
- Scikit-learn
- Random Forest Classifier
- Pandas
- NumPy
- Joblib

### Visualization
- Plotly

### Deployment
- Netlify (Frontend)
- Render (Backend)

---

## 📂 Project Structure

```
AI-Fraud-Detection/
│
├── BACKEND/
│   ├── app.py
│   ├── requirements.txt
│   ├── Procfile
│   ├── models/
│   │   ├── fraud_model.pkl
│   │   └── scaler.pkl
│   └── utils/
│
├── FRONTEND/
│   ├── index.html
│   ├── predict.html
│   └── static/
│       ├── css/
│       └── js/
│
├── dataset/
│
└── README.md
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/gauravsoni1706/Project-PBEL-3.0.git
```

Go to project directory

```bash
cd Project-PBEL-3.0
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r BACKEND/requirements.txt
```

Run Backend

```bash
cd BACKEND
python app.py
```

Run Frontend

```bash
cd FRONTEND
python -m http.server 5500
```

Open

```
http://127.0.0.1:5500
```

---

## 📊 Model Performance

| Metric | Value |
|---------|-------|
| Accuracy | 99.95% |
| Precision | 97.18% |
| Recall | 72.63% |
| F1 Score | 83.13% |

---

## 📷 Application Workflow

1. Open the website.
2. Navigate to the Prediction page.
3. Upload a CSV dataset.
4. Click **Predict Fraud**.
5. View:
   - Total Transactions
   - Fraudulent Transactions
   - Legitimate Transactions
   - Accuracy
   - Precision
   - Recall
   - F1 Score
   - Prediction Chart
   - Prediction Table
6. Download the prediction results.

---

## 📸 Screenshots

Add screenshots of:

- Home Page
- Prediction Page
- Prediction Results
- Pie Chart
- Downloaded CSV

---

## 🔮 Future Enhancements

- User Authentication
- Drag & Drop CSV Upload
- Deep Learning Models
- Real-time Fraud Detection
- REST API Documentation
- Multiple ML Model Comparison
- Cloud Database Integration

---

## 👨‍💻 Author

**Gaurav Soni**

GitHub:
https://github.com/gauravsoni1706

---

## 📜 License

This project is developed for educational and academic purposes.

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.