document.getElementById('votingForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    var selectedCandidate = document.querySelector('input[name="vote"]:checked');
    if (!selectedCandidate) {
        document.getElementById('message').innerHTML = "<p>Please select a candidate.</p>";
        return;
    }

    var voteValue = selectedCandidate.value;
    // Here you can implement logic to store the vote, such as sending it to a server.
    // For simplicity, let's just display a message indicating the vote has been submitted.
    document.getElementById('message').innerHTML = "<p>Vote for " + voteValue + " submitted successfully!</p>";
});
