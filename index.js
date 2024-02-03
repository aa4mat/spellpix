import addOnUISdk from "https://new.express.adobe.com/static/add-on-sdk/sdk.js";


addOnUISdk.ready.then(() => {
    console.log("addOnUISdk is ready for use.");

    const clickMeButton = document.getElementById("clickMe");
    const imageInput = document.getElementById('imageInput');

    clickMeButton.addEventListener("click", () => {
        // Simulate a click on the file input when the button is clicked
        imageInput.click();
    });

    // Event listener for file input to handle the image after selection
    imageInput.addEventListener('change', function() {
        if (this.files && this.files[0]) {
            var img = document.createElement('img');
            img.src = URL.createObjectURL(this.files[0]);
            img.onload = function() {
                URL.revokeObjectURL(img.src);
            };

            // Append the image or handle it as needed
            document.querySelector('.container').appendChild(img);
        }
    });

    // Optionally, disable the button initially and enable it after specific conditions are met
    clickMeButton.disabled = false;
});
