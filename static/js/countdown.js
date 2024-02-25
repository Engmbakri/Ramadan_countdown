$(document).ready(function () {
    function updateCountdown() {
        $.get('/get_time_remaining')
            .done(function (data) {
                const countdownElement = $('#countdown');
                countdownElement.text('Time Remaining: ' + data.time_remaining);
            })
            .fail(function (error) {
                console.error('Error fetching time remaining:', error);
            });
    }

    // Update the countdown every second
    setInterval(updateCountdown, 1000);
});
