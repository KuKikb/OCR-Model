var img,x,y,x1,y1;
function setScreenshotUrl(url) {
    img = url;
    document.getElementById('target').src = url;
    setTimeout(afterLoad, 200); // takes for new page to load properly, before further actions can be done
}

function afterLoad() {
    document.getElementById("target").addEventListener("mousedown", upper);
    document.getElementById("target").addEventListener("mouseup", lower);
}

function upper(e) {
    x = e.offsetX;
    y = e.offsetY;
}

function lower(e) {
    x1 = e.offsetX;
    y1 = e.offsetY;
    send()
}

function send() {
    const data = {img,x,y,x1,y1};
    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'text/plain'
        },
        body: JSON.stringify(data) 
    };
    fetch('http://127.0.0.1:8000/snip/',options);
    document.getElementById("result").innerHTML = "Completed!";
}