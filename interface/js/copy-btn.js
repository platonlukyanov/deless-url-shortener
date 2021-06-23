var copy_btn = document.getElementById("copy-image");
        var copied = false;
        copy_btn.onpointermove = ()=> {
            if (!copied) {
                copy_btn.src = "images/copy-btn/copy-filled.svg";
            }
            
        }
        copy_btn.onpointerleave = ()=> {
            if (!copied) {
                copy_btn.src = "images/copy-btn/copy.svg";
            }
        }
        copy_btn.onclick = ()=> {
            if (!copied) {
                selectText('target-link');
                document.execCommand('copy');
                copy_btn.src = "images/copy-btn/done.svg";
                copied = true;
                removeSelection();
            }
        }