

var buttons = document.getElementsByClassName('btn-package-item');

for (var i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener('click', function() {
      var user_id = "{{ User.id }}"
      redirectToURL("/calendar/"+user_id);
    });
  }
// Function to redirect to a specific URL
function redirectToURL(url) {
  window.location.href = url;
}
