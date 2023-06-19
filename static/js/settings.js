$(document).ready(function() {
    $('.edit-icon').click(function(e) {
      e.preventDefault(); // Prevent the link's default behavior

      var input = $(this).prev('input'); // Get the corresponding input element

      if (input.prop('disabled')) {
        input.prop('disabled', false); // Enable the input
        input.focus(); // Set focus on the input field
      } else {
        input.prop('disabled', true); // Disable the input
      }
    });
  });
  
  document.addEventListener("DOMContentLoaded", function() {
    var usernameInput = document.getElementById("username-input");
    var aboutInput = document.getElementById("about-input");
    var saveButton = document.getElementById("save-button");

    var originalUsername = usernameInput.value;
    var originalAbout = aboutInput.value;

    // Show the save button if changes are made
    function showSaveButton() {
      saveButton.classList.remove("hidden");
    }

    // Hide the save button if no changes are made
    function hideSaveButton() {
      saveButton.classList.add("hidden");
    }

    // Listen for input events on the username and about fields
    usernameInput.addEventListener("input", function() {
      if (usernameInput.value !== originalUsername || aboutInput.value !== originalAbout) {
        showSaveButton();
      } else {
        hideSaveButton();
      }
    });

    aboutInput.addEventListener("input", function() {
      if (usernameInput.value !== originalUsername || aboutInput.value !== originalAbout) {
        showSaveButton();
      } else {
        hideSaveButton();
      }
    });
  });