function myEventHandler(e, text) {
    e.stopPropagation();
    console.log(text);
}
