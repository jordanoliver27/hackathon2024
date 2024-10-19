document.getElementById('addressForm').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent the form from submitting the traditional way
    const address = event.target.address.value;

    fetch('/get_representatives', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ address })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Response Data:', data);  // Debug: log the response data

        const resultsDiv = document.getElementById('results');
        resultsDiv.innerHTML = '';  // Clear previous results

        if (data.error) {
            resultsDiv.innerHTML = `<p>Error: ${data.error}</p>`;
        } else {
            // Process and display the results
            if (data.officials && data.officials.length > 0) {
                data.officials.forEach(official => {
                    const officialDiv = document.createElement('div');
                    officialDiv.innerHTML = `
                        <h2>${official.name}</h2>
                        <p>Party: ${official.party}</p>
                        <p>Phone: ${official.phones ? official.phones.join(', ') : 'No phone available'}</p>
                        <p>Website: <a href="${official.urls[0]}" target="_blank">${official.urls[0]}</a></p>
                    `;
                    resultsDiv.appendChild(officialDiv);
                });
            } else {
                resultsDiv.innerHTML = '<p>No officials found for this address.</p>';
            }
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('results').innerHTML = `<p>Error: ${error.message}</p>`;
    });
});
