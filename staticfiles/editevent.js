// Get the event ID from the URL (assuming it’s passed as a query parameter)
const urlParams = new URLSearchParams(window.location.search);
const eventId = urlParams.get('id'); // Example: ?id=123

// Fetch the event data from your server
fetch(`api/events/${eventId}`) // Adjust the URL to match your API endpoint
    .then(response => response.json())
    .then(event => {
        // Populate the form fields with the existing event data
        document.getElementById('eventName').value = event.name;
        document.getElementById('eventDate').value = event.date; // Format as YYYY-MM-DD
        document.getElementById('eventTime').value = event.time; // Format as HH:MM
        document.getElementById('chefName').value = event.chefName;
        document.getElementById('chefBio').value = event.chefBio;
        document.getElementById('eventTheme').value = event.theme;
        document.getElementById('eventPrice').value = event.price;
        document.getElementById('seatCapacity').value = event.seatCapacity;
        document.getElementById('eventVenue').value = event.venue;
    })
    .catch(error => console.error('Error fetching event data:', error));

// Handle form submission
document.getElementById('editEventForm').addEventListener('submit', function(e) {
    e.preventDefault(); // Prevent the default form submission

    // Gather updated event data from the form
    const updatedEvent = {
        name: document.getElementById('eventName').value,
        date: document.getElementById('eventDate').value,
        time: document.getElementById('eventTime').value,
        chefName: document.getElementById('chefName').value,
        chefBio: document.getElementById('chefBio').value,
        theme: document.getElementById('eventTheme').value,
        price: document.getElementById('eventPrice').value,
        seatCapacity: document.getElementById('seatCapacity').value,
        venue: document.getElementById('eventVenue').value
    };

    // Send the updated data back to the server
    fetch(`api/events/${eventId}`, {
        method: 'PUT', // Or 'PATCH', depending on your API
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(updatedEvent)
    })
    .then(response => {
        if (response.ok) {
            // Optionally redirect or show a success message
            alert('Event updated successfully!');
            window.location.href = 'events-page.html'; // Redirect to events list page
        } else {
            alert('Failed to update the event.');
        }
    })
    .catch(error => console.error('Error updating event:', error));
});
