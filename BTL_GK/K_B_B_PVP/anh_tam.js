//  A. Xử lý âm thanh khi quay
function playSound() {
    let audio = new Audio("tick.mp3");
    audio.play();
}

//  B. Reset vòng quay
function resetWheel() {
    theWheel.stopAnimation(false);
    theWheel.rotationAngle = 0;
    theWheel.draw();
    statusButton("default");
}

// C. Khóa nút khi đang quay
let isSpinning = false;

function lockWhenSpin() {
    isSpinning = true;
    document.getElementById("spinButton").disabled = true;
}

function unlockWhenFinish() {
    isSpinning = false;
    document.getElementById("spinButton").disabled = false;
}