var buttons = document.getElementsByClassName('btn-package-item');

for (var i = 0; i < buttons.length; i++) {
  buttons[i].addEventListener('click', function() {
    var user_id = this.getAttribute('data-user-id'); // Gọi hàm getUserID() để lấy giá trị user_id từ nguồn khác
    redirectToURL("/calendar/choose/checkout/" + user_id);
  });
}

// Function to get the user ID from another source
function getUserID() {
  // Thực hiện các thao tác để lấy giá trị user_id từ nguồn khác
  // Ví dụ: return giá trị user_id từ một đối tượng, biến, hoặc hàm khác
}

// Function to redirect to a specific URL
function redirectToURL(url) {
  window.location.href = url;
}
