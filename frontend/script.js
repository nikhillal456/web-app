document.getElementById("valueForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent default form submission
    const value1 = document.getElementById("value1").value;
    const value2 = document.getElementById("value2").value;

    // Simple validation
    if (value1 && value2) {
        console.log("Values submitted:", value1, value2);
        // Here, you can send the data to the backend
    } else {
        alert("Please fill in both fields.");
    }
});

