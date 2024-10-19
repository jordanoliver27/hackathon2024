document.getElementById('addressForm').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent the form from submitting the traditional way
    const address = event.target.address.value;

    fetch('/get_info', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ address })
    })
    .then(response => response.json())
    .then(data => {
        const resultsDiv = document.getElementById('results');
        resultsDiv.innerHTML = '';  // Clear previous results

        if (data.error) {
            resultsDiv.innerHTML = `<p>Error: ${data.error}</p>`;
        } else {
            // Process and display the results for officials
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

            // Display election information
            const electionsDiv = document.createElement('div');
            electionsDiv.innerHTML = '<h2>Elections Information</h2>';
            if (data.elections.length > 0) {
                data.elections.forEach(election => {
                    const electionInfo = document.createElement('div');
                    electionInfo.innerHTML = `
                        <h3>${election.name}</h3>
                        <p>Date: ${new Date(election.electionDay).toLocaleDateString()}</p>
                        <p>Type: ${election.type}</p>
                    `;
                    electionsDiv.appendChild(electionInfo);
                });
            } else {
                electionsDiv.innerHTML += '<p>No upcoming elections found.</p>';
            }
            resultsDiv.appendChild(electionsDiv);
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
