function CopyButton(copy_btn, base_image, pointer_image, done_image) {
    var copied = false;
    copy_btn.onpointermove = () => {
        if (!copied) {
            copy_btn.src = pointer_image;
        }

    }
    copy_btn.onpointerleave = () => {
        if (!copied) {
            copy_btn.src = base_image;
        }
    }
    copy_btn.onclick = () => {
        if (!copied) {
            selectText('target-link');
            document.execCommand('copy');
            copy_btn.src = done_image;
            copied = true;
            removeSelection();
        }
    }
}
