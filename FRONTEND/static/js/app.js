const form = document.getElementById("uploadForm");

if (form) {
    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        const fileInput = document.getElementById("csvFile");

        if (!fileInput.files.length) {
            alert("Please select a CSV file.");
            return;
        }

        const formData = new FormData();
        formData.append("file", fileInput.files[0]);

        try {

            // Loading state
            const submitBtn = form.querySelector("button");
            submitBtn.disabled = true;
            submitBtn.innerText = "Predicting...";

            const response = await fetch(
                "https://project-pbel-3-0.onrender.com/predict",
                {
                    method: "POST",
                    body: formData
                }
            );

            const result = await response.json();

            submitBtn.disabled = false;
            submitBtn.innerText = "Predict Fraud";

            if (!response.ok || !result.success) {
                alert(result.error || "Prediction failed.");
                return;
            }

            // Show Result Section
            document.getElementById("resultSection").style.display = "block";

            // Summary
            document.getElementById("total").innerText =
                result.summary.total;

            document.getElementById("fraud").innerText =
                result.summary.fraud;

            document.getElementById("genuine").innerText =
                result.summary.genuine;

            document.getElementById("accuracy").innerText =
                result.summary.accuracy;

            document.getElementById("precision").innerText =
                result.summary.precision;

            document.getElementById("recall").innerText =
                result.summary.recall;

            document.getElementById("f1").innerText =
                result.summary.f1;

            // Chart
            document.getElementById("chartContainer").innerHTML =
                result.chart;

            // Table
            document.getElementById("tableContainer").innerHTML =
                result.table;

            // Download Button
            document.getElementById("downloadBtn").href =
                "https://project-pbel-3-0.onrender.com/download";

            // Scroll to results
            document.getElementById("resultSection").scrollIntoView({
                behavior: "smooth"
            });

        } catch (error) {

            console.error(error);

            alert("Unable to connect to the server.");

            const submitBtn = form.querySelector("button");
            submitBtn.disabled = false;
            submitBtn.innerText = "Predict Fraud";
        }
    });
}