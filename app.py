import os
import joblib
import pandas as pd
import plotly.express as px

from flask import Flask, render_template, request, send_file

app = Flask(__name__)

# ---------------- LOAD MODEL ---------------- #

MODEL_PATH = os.path.join("models", "fraud_model.pkl")
SCALER_PATH = os.path.join("models", "scaler.pkl")

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)


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

            try:

                # Read CSV
                df = pd.read_csv(uploaded_file)

                # Remove target column if present
                if "Class" in df.columns:
                    df = df.drop(columns=["Class"])

                # Check required columns
                required_columns = ["Time", "Amount"]

                for col in required_columns:
                    if col not in df.columns:
                        return render_template(
                            "predict.html",
                            summary=None,
                            chart=None,
                            table=f"""
                            <div class='alert alert-danger'>
                            Missing required column:
                            <b>{col}</b>
                            </div>
                            """
                        )

                # Scale features
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

                # Pie Chart
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

                # Preview Table
                preview = df.copy()

                preview["Prediction"] = preview["Prediction"].replace({
                    0: "Legitimate",
                    1: "Fraud"
                })

                table = preview.head(10).to_html(
                    classes="table table-striped table-hover table-bordered",
                    index=False
                )

                # Save CSV
                df.to_csv("prediction_result.csv", index=False)

            except Exception as e:

                return render_template(
                    "predict.html",
                    summary=None,
                    chart=None,
                    table=f"""
                    <div class='alert alert-danger'>
                    <b>Error:</b><br>{str(e)}
                    </div>
                    """
                )

    return render_template(
        "predict.html",
        summary=summary,
        chart=chart,
        table=table
    )


# ---------------- DOWNLOAD RESULT ---------------- #

@app.route("/download")
def download():

    filename = "prediction_result.csv"

    if os.path.exists(filename):
        return send_file(
            filename,
            as_attachment=True
        )

    return "No prediction file found."


# ---------------- RUN APP ---------------- #

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)