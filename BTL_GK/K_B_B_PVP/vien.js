 //A. Tính góc từng giải
const GOC_MOI_GIAI = 360 / 8;   // 45°

//B. Hàm quay ngẫu nhiên
function startSpin() {
    let randomAngle = Math.random() * 360;

    theWheel.animation.stopAngle = randomAngle;
    theWheel.startAnimation();
}

// C. Hàm chỉ định góc (Stop Angle)
function stopAngle(viTriGiai) {
    const start = viTriGiai * 45;
    const offset = Math.random() * 44;
    return start + offset;
}