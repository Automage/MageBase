var header = document.querySelector('h1');
var messageContainer = document.querySelector('#message-container');
var button = document.querySelector('button');
var messageCount = 0;
//myHeading.textContent = '!';
//alert("WWWOO");
header.onclick = function () {
    "use strict";
    if (header.textContent === 'PhilSoc') {
        header.textContent = 'And I love you so';
    } else {
        header.textContent = 'PhilSoc';
    }
};

button.onclick = function () {
    "use-strict";
   // alert('New message');
    var message = document.createElement('p');
    message.classList.add('message');
    message.textContent = 'Message' + messageCount;
    messageContainer.appendChild(message);
    messageCount++;
}


