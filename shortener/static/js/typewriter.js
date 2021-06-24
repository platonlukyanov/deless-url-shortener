function type(element, delay=1000) {
    var text = element.innerText;
    element.innerText = text.slice(0, 1);
    console.log(element.innerText);
    var i = 1;
    setInterval(()=>{
        element.innerText = text.slice(0, i);
        if (element.innerText.length > text.length) {return true;}
        i++;
    }, delay);
    
}