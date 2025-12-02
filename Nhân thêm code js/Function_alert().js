function alertPrize(segment) {
    // Huỳnh Thiện Nhân
    document.getElementById("resultBox").innerText =
        "Bạn đã trúng: " + segment.text;

    statusButton("showReset")};