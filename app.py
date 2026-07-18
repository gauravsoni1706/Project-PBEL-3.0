import os
import joblib
import pandas as pd
import plotly.express as px

from flask import Flask, render_template, request, send_file, send_from_directory

app = Flask(__name__)

# Load trained model and scaler
model = joblib.load("models/fraud_model.pkl")
scaler = joblib.load("models/scaler.pkl")


# ---------------- HOME PAGE ---------------- #

@app.route("/")
def home():
    return render_template("index.html")


# ---------------- ABOUT PAGE ---------------- #

@app.route("/about")
def about():
    return render_template("about.html")


# ---------------- PREDICT PAGE ---------------- #

@app.route("/predict", methods=["GET", "POST"])
def predict():

    summary = None
    chart = None
    table = None

    if request.method == "POST":

        uploaded_file = request.files.get("file")

        if uploaded_file and uploaded_file.filename != "":

            # Read uploaded CSV
            df = pd.read_csv(uploaded_file)

            # Remove Class column if user uploads original dataset
            if "Class" in df.columns:
                df = df.drop(columns=["Class"])

            # Scale Time and Amount
            df[["Time", "Amount"]] = scaler.transform(
                df[["Time", "Amount"]]
            )

            # Predict
            prediction = model.predict(df)

            # Add prediction column
            df["Prediction"] = prediction

            fraud = int((prediction == 1).sum())
            genuine = int((prediction == 0).sum())

            summary = {
                "total": len(df),
                "fraud": fraud,
                "genuine": genuine,
                "accuracy": "99.95%",
                "precision": "97.18%",
                "recall": "72.63%",
                "f1": "83.13%"
            }

            # Create Pie Chart
            fig = px.pie(
                names=["Fraud", "Legitimate"],
                values=[fraud, genuine],
                title="Fraud Detection Summary",
                color=["Fraud", "Legitimate"],
                color_discrete_map={
                    "Fraud": "#dc3545",
                    "Legitimate": "#198754"
                }
            )

            chart = fig.to_html(full_html=False)

            # Create Preview Table
            preview = df.copy()

            preview["Prediction"] = preview["Prediction"].replace({
                0: "Legitimate",
                1: "Fraud"
            })

            table = preview.head(10).to_html(
                classes="table table-striped table-hover table-bordered",
                index=False
            )

            # Save prediction CSV
            df.to_csv("prediction_result.csv", index=False)

    return render_template(
        "predict.html",
        summary=summary,
        chart=chart,
        table=table
    )


# ---------------- DOWNLOAD RESULT ---------------- #

@app.route("/download")
def download():

    if os.path.exists("prediction_result.csv"):
        return send_file(
            "prediction_result.csv",
            as_attachment=True
        )

    return "No prediction file found."


# ---------------- RUN APP ---------------- #

if __name__ == "__main__":
    app.run(debug=True)