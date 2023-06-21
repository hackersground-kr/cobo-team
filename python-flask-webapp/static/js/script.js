//버튼 토글함수
function toggleButton(button) {
  button.classList.add("disabled"); // 클릭한 버튼을 비활성화

  // 나머지 버튼을 찾아 활성화
  var otherButtonId = button.id === "button1" ? "button2" : "button1";
  var otherButton = document.getElementById(otherButtonId);
  otherButton.classList.remove("disabled");
  otherButton.classList.add("active");
}

// 오디오 파동 모양을 보여주는 함수
function visualizeAudio() {
  var canvas = document.getElementById("audio-wave");
  var ctx = canvas.getContext("2d");
  var waveWidth = canvas.width;
  var waveHeight = canvas.height;

  var audioContext = new (window.AudioContext || window.webkitAudioContext)();
  var analyser = audioContext.createAnalyser();

  // getUserMedia를 사용하여 마이크에 접근
  navigator.mediaDevices
    .getUserMedia({ audio: true })
    .then(function (stream) {
      var source = audioContext.createMediaStreamSource(stream);
      source.connect(analyser);

      analyser.fftSize = 256;
      var bufferLength = analyser.frequencyBinCount;
      var dataArray = new Uint8Array(bufferLength);

      function draw() {
        requestAnimationFrame(draw);

        analyser.getByteTimeDomainData(dataArray);

        ctx.fillStyle = "rgba(255, 255, 255, 0.1)";
        ctx.fillRect(0, 0, waveWidth, waveHeight);
        ctx.lineWidth = 2;
        ctx.strokeStyle = "rgb(0, 0, 255)";
        ctx.beginPath();

        var sliceWidth = (waveWidth * 1.0) / bufferLength;
        var x = 0;

        for (var i = 0; i < bufferLength; i++) {
          var v = dataArray[i] / 128.0;
          var y = (v * waveHeight) / 2;

          if (i === 0) {
            ctx.moveTo(x, y);
          } else {
            ctx.lineTo(x, y);
          }

          x += sliceWidth;
        }

        ctx.lineTo(waveWidth, waveHeight / 2);
        ctx.stroke();
      }

      draw();
    })
    .catch(function (err) {
      console.error("마이크에 접근하는 중 오류가 발생했습니다.", err);
    });
}

visualizeAudio();
