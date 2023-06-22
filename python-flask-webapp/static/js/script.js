// 버튼 토글 함수
function toggleButton(button) {
  $(button).toggleClass("active");
}

$(document).ready(function () {
  // 버튼 클릭 이벤트 핸들러 등록
  $("#myButton").click(function () {
    $(this).toggleClass("active");
    executeMyPythonFunction();
  });
});

function executeMyPythonFunction() {
  // 파이썬 함수를 호출하는 AJAX 요청
  $.ajax({
    url: "/execute-python-function", // Flask 애플리케이션의 라우트 경로
    type: "GET",
    success: function (response) {
      // 파이썬 함수 실행에 대한 응답 처리
      console.log(response);
    },
    error: function (error) {
      // 오류 처리
      console.log(error);
    },
  });
}
