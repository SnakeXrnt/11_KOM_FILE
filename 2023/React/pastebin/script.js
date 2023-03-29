$(document).ready(function() {
    $('#load-button').on('click', function() {
      var pasteId = $('#paste-id').val();
      var apiUrl = 'http://api.allorigins.win/get?url=https://pastebin.com/raw/' + pasteId;
      $.ajax({
        url: apiUrl,
        method: 'GET',
        success: function(response) {
          $('#paste-container').text(response);
        },
        error: function() {
          $('#paste-container').text('Error: could not load paste.');
        }
      });
    });
  });
  