window.onload = () => {
    const video = document.querySelector("#camera");
    const canvas = document.querySelector("#picture");
    const shutter = document.querySelector("#shutter");
    const a = document.querySelector("#download")
    const ctx = canvas.getContext("2d");
    video.setAttribute("style", "margin-bottom:40px")
    a.style.display = "none"

    /** カメラ設定 */
    const constraints = {
        audio: false,
        video: {
            width: { ideal: 1080 },
            height: { ideal: 1920 },
            // フロントカメラを利用する
            facingMode: "user"
        }
    };

    /**
     * カメラ起動
     */
    const getLocalMediaStream = (mediaStream) => {
        // const mediaRecorder = new MediaRecorder(mediaStream);
        // console.log(mediaRecorder)
        video.srcObject = mediaStream;
        video.play();
    }

    /**
     * カメラ映像取得エラー
     */
    const handleCameraError = (err) => {
        console.log(err.name + ": " + err.message);
    }

    /**
     * カメラを<video>と同期
     */
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        console.log('success')
        navigator.mediaDevices.getUserMedia(constraints)
            .then(getLocalMediaStream)
            .catch(handleCameraError);
        console.log()
    } else {
        console.log("not supported.")
    }

    /**
     * シャッターボタン（写真撮影時）
     */
    shutter.addEventListener("click", () => {
        video.pause()
        setTimeout(() => {
            video.play();
        }, 500);
        ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

        canvas.toBlob((blob) => {
            console.log(blob)
            a.href = URL.createObjectURL(blob)
            a.style.display = "block"


            // console.log('url:', a.href)

            // let newImg = document.createElement("img")
            // newImg.src = a.href
            // document.body.appendChild(newImg)
        })

        URL.revokeObjectURL(a.href)
    });
}