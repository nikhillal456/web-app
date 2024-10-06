document.getElementById('dataForm').addEventListener('submit', async (e) => {
    e.preventDefault(); // Prevent the form from submitting normally
    const value1 = document.getElementById('value1').value;
    const value2 = document.getElementById('value2').value;

    // Send data to the backend with the correct URL for backend
    await fetch('http://localhost:5000/submit', { // Replace with your backend URL and port if needed
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ Value1: value1, Value2: value2 }), // Ensure field names match your database column names
    });

    // Clear the input fields
    document.getElementById('value1').value = '';
    document.getElementById('value2').value = '';
});

// Fetch data from the backend
document.getElementById('showDataBtn').addEventListener('click', async () => {
    const response = await fetch('http://localhost:5000/data'); // Adjust the URL for your backend
    const data = await response.json();

    const dataDisplay = document.getElementById('dataDisplay');
    dataDisplay.innerHTML = ''; // Clear previous data
    data.forEach(entry => {
        const div = document.createElement('div');
        div.textContent = `Value 1: ${entry.Value1}, Value 2: ${entry.Value2}`; // Ensure these match your database column names
        dataDisplay.appendChild(div);
    });
});

