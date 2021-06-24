function getCookie(name) {
    let matches = document.cookie.match(new RegExp(
      "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
    ));
    return matches ? decodeURIComponent(matches[1]) : undefined;
  }
function setCookie(name, value) {
    let updatedCookie = encodeURIComponent(name) + "=" + encodeURIComponent(value);
    document.cookie = updatedCookie;
}
function deleteCookie(name) {
    setCookie(name, "", {
      'max-age': -1
    })
  }

function changeThemeByName(newColorScheme) {
    if (newColorScheme === "dark") {
        current_theme = "dark";
        darkTheme();
    }
    else if (newColorScheme === "light") {
        current_theme = "light";
        lightTheme();
    }
}

var current_theme;
var theme_changer  = document.getElementById("theme-changer");
if (getCookie("scheme")) {
    changeThemeByName(getCookie("scheme"));
}
else {
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        darkTheme();
        current_theme = "dark";
    }
    else {
        current_theme = "light";
        lightTheme();
    }
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
        var newColorScheme = e.matches ? "dark" : "light";
        changeThemeByName(newColorScheme);
    });

}
theme_changer.addEventListener('click', ()=> {
    var newColorScheme = current_theme === "light" ? "dark" : "light";
    changeThemeByName(newColorScheme);
    setCookie("scheme", newColorScheme);
})