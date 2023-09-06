document.addEventListener('DOMContentLoaded', function () {
    const fileInput = document.getElementById('csvFileInput');
    const uploadButton = document.getElementById('uploadButton');

    uploadButton.addEventListener('click', function () {
        const file = fileInput.files[0];
        if (file) {
            const formData = new FormData();
            formData.append('csvFile', file);

            fetch('/upload.php', {
                method: 'POST',
                body: formData,
            })
            .then(response => {
                if (response.ok) {
                    alert('File uploaded successfully.');
                } else {
                    alert('File upload failed.');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An error occurred while uploading the file.');
            });
        } else {
            alert('Please select a CSV file to upload.');
        }
    });
});