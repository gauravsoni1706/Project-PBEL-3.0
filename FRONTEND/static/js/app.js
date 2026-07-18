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

        const response = await fetch(
            "https://project-pbel-3-0.onrender.com",
            {
                method: "POST",
                body: formData
            }
        );

        const result = await response.json();

        console.log(result);

        // We'll display the results here in the next step.
    });
}