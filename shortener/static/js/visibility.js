function addPasswordOnOff(input, visibility_element, path_visible="images/visibility/visible.svg", path_unvisible="images/visibility/unvisible.svg") {
    var status = path_unvisible;
    console.log(status)
    visibility_element.onclick = ()=> {
        if (status === path_visible) {
            console.log("make unvisible");
            input.type = "password";
            visibility_element.src = path_unvisible;
            status = path_unvisible;
        }
        else if (status === path_unvisible) {
            console.log("make visible");
            input.type = "text";
            visibility_element.src = path_visible;
            status = path_visible;
        }
    }

}