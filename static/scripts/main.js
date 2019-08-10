var header = document.querySelector('h1');
var messageContainer = document.querySelector('#message-container');
var button = document.querySelector('button');
var messageCount = 0;

//Header
var headerNames = ['Slice of P', 'Slice of π', 'Slice of Pranaw', 'Slice of Grapdpa', 'Slice of Sidhu']
var headerState = 0;

header.onclick = function () {
    "use strict";
    headerState++;
    if (headerState == headerNames.length) {
        headerState = 0;
    }
    header.textContent = headerNames[headerState]
};

button.onclick = function () {
    "use-strict";
    // alert('New message');
    var message = document.createElement('p');
    message.textContent = 'Message' + messageCount;
    messageContainer.appendChild(message);
    messageCount++;
}


