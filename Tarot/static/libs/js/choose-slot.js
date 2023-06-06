var buttons = document.getElementsByClassName('btn-package-item');

for (var i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener('click', function() {
      window.location.href="/calendar/choose/checkout ";
    });
  }
// Function to redirect to a specific URL
function redirectToURL(url) {
  window.location.href = url;
}
