
/*

const myAPI = "[ae077128449cf88203196cd19fcc1cab]";
function onGeoOk(position) {
  const lat = position.coords.latitude;
  const lng = position.coords.longitude;
  // 현재의 위도와 경도를 받아온다.
  const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lng}&appid=${myAPI}&units=metric`;
  fetch(url)
    .then((respnse) => respnse.json())
    .then((data) => {
      const weatherCon = document.querySelector("#weather");
      const weather = document.querySelector("#weather span:first-child");
      const city = document.querySelector("#weather span:last-child");
      const weatherImg = document.querySelector("#weatherIcon");
      const weatherIcon = data.weather[0].icon;
      const weatherUrl = `http://openweathermap.org/img/wn/${weatherIcon}@2x.png`;
      city.innerHTML = ` ${data.name}`;
      weather.innerHTML = `${Math.round(data.main.temp)}º`;
      weatherCon.appendChild(weather);
      weatherCon.appendChild(city);
      document.getElementById("weatherIcon").src = weatherUrl; // 추가했습니다
      console.log(data);
    });
}


function onGeoErr() {
  alert("위치를 찾을 수 없습니다.");
}


navigator.geolocation.getCurrentPosition(onGeoOk, onGeoErr);

*/


/*

var xhr = new XMLHttpRequest();
var url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'; /*URL*/
// var queryParams = '?' + encodeURIComponent('serviceKey') + '='+'서비스키'; /*Service Key*/
// 7JzJfbGzrqIWFyiDpLndHmGL0e59B73hFzqtEZ9vh7APDxYsFEhoflGKPLULny6uZNEYKFAZXh1NqUYGJ0Oc4g==
var queryParams = '?' + encodeURIComponent('serviceKey') + '='
	+'7JzJfbGzrqIWFyiDpLndHmGL0e59B73hFzqtEZ9vh7APDxYsFEhoflGKPLULny6uZNEYKFAZXh1NqUYGJ0Oc4g%3D%3D'; /*Service Key*/
queryParams += '&' + encodeURIComponent('pageNo') + '=' + encodeURIComponent('1'); /**/
queryParams += '&' + encodeURIComponent('numOfRows') + '=' + encodeURIComponent('1000'); /**/
queryParams += '&' + encodeURIComponent('dataType') + '=' + encodeURIComponent('XML'); /**/
queryParams += '&' + encodeURIComponent('base_date') + '=' + encodeURIComponent('20210628'); /**/
queryParams += '&' + encodeURIComponent('base_time') + '=' + encodeURIComponent('0600'); /**/
queryParams += '&' + encodeURIComponent('nx') + '=' + encodeURIComponent('55'); /**/
queryParams += '&' + encodeURIComponent('ny') + '=' + encodeURIComponent('127'); /**/
xhr.open('GET', url + queryParams);
xhr.onreadystatechange = function () {
    if (this.readyState == 4) {
        alert('Status: '+this.status+'nHeaders: '+JSON.stringify(this.getAllResponseHeaders())+'nBody: '+this.responseText);
    }
};

xhr.send('');

*/