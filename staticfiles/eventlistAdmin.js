const events = [
  {
    id: 1,
    name: "Sustainable Coffee Workshop",
    date: "2023-12-01",
    time: "6:00 PM",
    venue: "Café A",
    price: 25,
    image:
      "https://cdn.pixabay.com/photo/2014/07/21/19/20/lobby-398845_640.jpg",
  },
  {
    id: 2,
    name: "Coffee and Dessert Pairing Night",
    date: "2023-12-02",
    time: "7:00 PM",
    venue: "Café B",
    price: 30,
    image:
      "https://plus.unsplash.com/premium_photo-1661964071015-d97428970584?q=80&w=1920&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
  },
  {
    id: 3,
    name: "Coffee and Dessert Pairing Night",
    date: "2023-12-02",
    time: "7:00 PM",
    venue: "Café B",
    price: 30,
    image:
      "https://plus.unsplash.com/premium_photo-1661306437817-8ab34be91e0c?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
  },
  {
    id: 4,
    name: "Coffee and Dessert Pairing Night",
    date: "2023-12-02",
    time: "7:00 PM",
    venue: "Café B",
    price: 30,
    image:
      "https://images.unsplash.com/photo-1528605248644-14dd04022da1?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
  },
  {
    id: 5,
    name: "Coffee and Dessert Pairing Night",
    date: "2023-12-02",
    time: "7:00 PM",
    venue: "Café B",
    price: 30,
    image:
      "https://images.unsplash.com/photo-1527529482837-4698179dc6ce?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
  },
  {
    id: 6,
    name: "Coffee and Dessert Pairing Night",
    date: "2023-12-02",
    time: "7:00 PM",
    venue: "Café B",
    price: 30,
    image:
      "https://images.unsplash.com/photo-1531058020387-3be344556be6?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
  },
  // Add more events here...
];

// Loop through the events and create a card for each
events.forEach((event) => {
  // Create the card structure dynamically
  const eventCard = document.createElement("div");
  eventCard.classList.add("col-md-4", "mb-4"); // Bootstrap column and margin classes

  // Insert the card HTML
  eventCard.innerHTML = `
        <div class="card">
          <img src="${event.image}" class="card-img-top" alt="${event.name}">
          <div class="card-body">
            <h5 class="card-title">${event.name}</h5>
            <div class="event-details" id="details-${event.id}" style="display: none;">
              <p class="card-text">
                <strong>Date:</strong> ${event.date}<br>
                <strong>Time:</strong> ${event.time}<br>
                <strong>Venue:</strong> ${event.venue}<br>
                <strong>Price:</strong> $${event.price}
              </p>
            </div>
            <button class="btn btn-secondary toggle-details" data-id="${event.id}">View Details</button>
            <button style="background-color:"red" class="btn btn-primary book-now" data-id="${event.id}">Delete</button> 
          </div>
        </div>
      `;

  // Append the event card to the container
  document.getElementById("event-listing-container").appendChild(eventCard);
});

// Add event listeners to all "View Details" buttons
document.querySelectorAll(".toggle-details").forEach((button) => {
  button.addEventListener("click", function () {
    const eventId = this.getAttribute("data-id");
    const detailsElement = document.getElementById(`details-${eventId}`);

    // Toggle the visibility of the event details
    if (detailsElement.style.display === "none") {
      detailsElement.style.display = "block";
      this.textContent = "Hide Details";
    } else {
      detailsElement.style.display = "none";
      this.textContent = "View Details";
    }
  });
});
