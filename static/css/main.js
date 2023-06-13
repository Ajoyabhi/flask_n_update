document.addEventListener("DOMContentLoaded", function () {
  var animationList = document.getElementById("animation-list");
  var firstTimeRendered = localStorage.getItem("firstTimeRendered");

  if (!firstTimeRendered) {
    animationList.style.visibility = "hidden";
    localStorage.setItem("firstTimeRendered", true);
  } else {
    animationList.style.visibility = "visible";
  }
});

function showSpinner() {
  var button = document.getElementById("analyzeButtonText");
  var spinnerContainer = document.getElementById("spinnerContainer");

  // Hide the button text and display the spinner
  button.style.display = "none";
  spinnerContainer.style.display = "block";

  setTimeout(function () {
    // Simulating task completion
    hideSpinner();
  }, 5000);
}

function hideSpinner() {
  var button = document.getElementById("analyzeButtonText");
  var spinnerContainer = document.getElementById("spinnerContainer");

  // Hide the spinner and display the button text
  spinnerContainer.style.display = "none";
  button.style.display = "block";
}


 // Function to open the popup
function openPopup() {
    document.getElementById('popupContainer').style.display = 'flex';
}

  // Function to close the popup
function closePopup() {
    document.getElementById('popupContainer').style.display = 'none';
}

  // Event listener for the open popup button
document.getElementById('openPopupButton').addEventListener('click', openPopup);
