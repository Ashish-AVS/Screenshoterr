console.log('Background script loaded.')


  chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    handleMessage(message);
  });


// Write a function to handle the message from popup.js
function handleMessage(request) {
    console.log('Message from the popup script:');
    const {screenshotUrl} = request;
    fetch('http://localhost:5000/api', {
        method: 'POST',
        body: JSON.stringify({ timestamp: Date.now().toLocaleString(),screenshotUrl: screenshotUrl }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(function(response) {
        console.log(response);
        return response.json();
    }).then(function(data) {
        console.log(data);
    }).catch(function(err) {
        console.log(err);
    });
}
