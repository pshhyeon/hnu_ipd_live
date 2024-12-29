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

</head>
<body>

<header>
	<a href="/live/builtInHome">&lt;</a>
	<p>비밀번호 발급</p>
</header>


<p>lock icon</p>
<p>화면을 벗어나면 비밀번호가 초기화 되요!</p>

<form action="/live/createPassword" method="post">
	<input type="number" min="0" max="9" maxlength="1" name="firstNum" required="" data-firstNum="">
	<input type="number" min="0" max="9" maxlength="1" name="firstNum" required="" data-seccondNum="">
	<input type="number" maxlength="1" disabled>
	<input type="number" maxlength="1" disabled>
	<input type="number" maxlength="1" disabled>
	<input type="number" maxlength="1" disabled>
</form>

<a href="#">다음으로</a>

<footer>

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