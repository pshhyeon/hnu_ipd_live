<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/functions" prefix="fn" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>page</title>
<script src="${pageContext.request.contextPath }/resources/js/jQuery-3.7.1.js"></script>
<link rel="stylesheet" href="${pageContext.request.contextPath }/resources/bootstrap-5.3.3/dist/css/bootstrap.css">
<script src="${pageContext.request.contextPath }/resources/bootstrap-5.3.3/dist/js/bootstrap.js"></script>
<script src="${pageContext.request.contextPath }/resources/js/weather.js"></script>

</head>
<body>

<header>
	<p>hi here!</p>
	<p>alram badge</p>
	<a>setting badge</a>
</header>


<p>반가워요, 다현님! <br> 오늘은 좀 흐리네요 </p>
<img id="weatherIcon" src="" />
<div id="weather">
	<span></span> <span></span>
</div>

<a href="/live/passwordPage">일회용 비밀번호 발급 <br> lock icon </a>

<br><br><br><br>

<button>긴급신고1<p>icon</p></button>
<button>긴급신고2<p>icon</p></button>
<button>긴급신고3<p>icon</p></button>
<button>긴급신고4<p>icon</p></button>

<footer>
	<button>홈<p>icon</p></button>
	<button>생활<p>icon</p></button>
	<button>소식<p>icon</p></button>
	<button>마이<p>icon</p></button>
</footer>

</body>

<script type="text/javascript">

$(function(){
	
}); // /$(function(){})

</script>
 
</html>

<!-- 비밀번호 재발급 화면 에서 구성 -->
<!-- Pin Entry Screen -->
<!-- <div class="container my-4"> -->
<!--     <div class="pin-container text-center"> -->
<!--         <h2>비밀번호 발급</h2> -->
<!--         <p>화면을 벗어나면 비밀번호가 초기화 돼요</p> -->
<!--         <div> -->
<!--             <span class="pin-box">8</span> -->
<!--             <span class="pin-box">1</span> -->
<!--             <span class="pin-box"></span> -->
<!--             <span class="pin-box"></span> -->
<!--             <span class="pin-box"></span> -->
<!--         </div> -->
<!--         <button class="next-button mt-3">다음으로</button> -->
<!--     </div> -->
<!-- </div> -->




<!-- 	<p>비밀번호 재발급 페이지</p> -->
<!-- 	<button class="btn btn-primary" id="create-password">button</button> -->
<!-- 

<script type="text/javascript">
$(function(){
	$("#create-password").on("click", function(){
		$.ajax({
	        url: "/test/clickTest.do",
	        type: "POST",
// 			data: { 
// 				chatRoomNo: selectedChatRoomNo,
// 				emplArrToStr : emplArrToStr
// 			},
	        dataType: "text",	// 서버에서 전달 받는 데이터
	        success: function(res) {
				alert(res);
			},
		    error: function(error) {
		        console.log(error);
		        alert("Error");
		    }
		});
	});
	
})
</script>
 -->