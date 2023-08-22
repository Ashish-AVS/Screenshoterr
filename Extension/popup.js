function captureScreenshot(){
    chrome.tabs.captureVisibleTab(null, {}, function(screenshotUrl) {
        // send screenshotUrl message to background.js
        chrome.runtime.sendMessage({screenshotUrl: screenshotUrl}, function(response) {
            console.log(response);
        });
    })

}


document.getElementById("capture").addEventListener("click", () => {
    const intervalId = setInterval(captureScreenshot, 5 * 1000);
    setTimeout(function() {
        clearInterval(intervalId); // Clear the interval
        console.log("Interval cleared after 5 minutes");
    }, 300000); // 5 minutes in milliseconds
});




