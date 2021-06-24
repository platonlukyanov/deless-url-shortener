var light_theme_css = document.getElementById("light-theme");
var dark_theme_css = document.getElementById("dark-theme");
var light_theme_css_inner = light_theme_css.outerHTML;
var dark_theme_css_inner = dark_theme_css.outerHTML;
dark_theme_css.parentNode.removeChild(dark_theme_css);
function darkTheme() {
    try {
        var light_theme_css = document.getElementById("light-theme");
        light_theme_css.parentNode.removeChild(light_theme_css);
    }
    catch {};
    document.head.innerHTML += dark_theme_css_inner;
    var changer = document.getElementById("theme-changer");
    changer.src = changer.src.replace("light", "dark");
}
function lightTheme() {
    try {
        var dark_theme_css = document.getElementById("dark-theme"); 
        dark_theme_css.parentNode.removeChild(dark_theme_css);
    }
    catch {};
    document.head.innerHTML += light_theme_css_inner;
    var changer = document.getElementById("theme-changer");
    changer.src = changer.src.replace("dark", "light");
}