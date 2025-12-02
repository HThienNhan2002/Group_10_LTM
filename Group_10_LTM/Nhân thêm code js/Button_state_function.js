function statusButton(status) {
    // Huỳnh Thiện Nhân
    const spin = document.getElementById("spinButton");
    const reset = document.getElementById("resetButton");

    if (status === "spinning") {
        spin.style.display = "none";
        reset.style.display = "none";
    } else if (status === "showReset") {
        reset.style.display = "block";
    } else {
        spin.style.display = "block";
        reset.style.display = "none";
    }
}
