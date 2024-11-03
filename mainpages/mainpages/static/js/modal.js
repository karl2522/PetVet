// Function to open the modal
function openModal() {
  document.getElementById("modal").style.display = "flex";
  console.log("Modal is clicked!")
}

// Function to close the modal
function closeModal() {
  document.getElementById("modal").style.display = "none";
}

// Open modal when the Set Appointment button is clicked
document.getElementById("addappointments-btn").onclick = openModal;

// Close modal when clicking outside the modal content
window.onclick = function(event) {
  const modal = document.getElementById("modal");
  if (event.target === modal) {
      closeModal();
  }
};
