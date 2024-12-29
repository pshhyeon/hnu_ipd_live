#ifndef HTML_H
#define HTML_H

const char* htmlHomePage PROGMEM = R"rawliteral(
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>doorLock</title>
    <script src="https://code.jquery.com/jquery-3.7.1.js"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" />
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css" />

    <style>
      body {
        margin: 0;
        background-color: #2f2f2f;
        display: flex;
        justify-content: center;
        align-items: center;
        overflow: hidden;
      }
      .device {
        width: 1280px;
        height: 800px;
        background-color: #2f2f2f;
        border-radius: 20px;
        padding: 20px;
        display: flex;
      }
      .screen {
        width: 100%;
        height: 300px;
        background-color: #ffffff;
        border: 2px solid #333;
        border-radius: 10px;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 2rem;
        font-weight: bold;
        color: #333;
        text-align: center;
      }
      .instructions {
        font-size: 1rem;
        color: #ccc;
        line-height: 1.6;
        margin-top: 20px;
      }
      .brand {
        color: #fff;
        font-size: 2rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
      }
      .keypad {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 15px;
      }
      .key {
        width: 120px;
        height: 90px;
        font-size: 1.8rem;
        font-weight: bold;
        text-align: center;
        line-height: 90px;
        border-radius: 15px;
      }
    </style>
  </head>
  <body>
    <div class="device container">
      <div class="row flex-grow-1">
        <div class="col-6 d-flex flex-column justify-content-between ps-5">
          <div class="screen mt-5" id="screen">LIVE</div>
          <div class="instructions mb-5">
            <h2 class="text-white">사용 방법</h2>
            <button class="btn btn-primary" onclick="sendCommand()">문열림</button>
            <h5>세대 호출: 세대 호수 + <i class="fa-solid fa-phone"></i></h5>
            <h5>경비 호출: <i class="fa-solid fa-bell"></i></h5>
            <h5>호출 취소: <i class="fa-solid fa-xmark"></i></h5>
            <h5>비밀번호 입력: 세대 호수 + # + 비밀번호 + #</h5>
          </div>
        </div>
        <div class="col-6 d-flex flex-column align-items-center ps-5">
          <div class="brand mt-5">LIVE</div>
          <div class="keypad mt-5">
            <button class="btn btn-secondary key" onclick="appendInput('1')">1</button>
            <button class="btn btn-secondary key" onclick="appendInput('2')">2</button>
            <button class="btn btn-secondary key" onclick="appendInput('3')">3</button>
            <button class="btn btn-secondary key" onclick="appendInput('4')">4</button>
            <button class="btn btn-secondary key" onclick="appendInput('5')">5</button>
            <button class="btn btn-secondary key" onclick="appendInput('6')">6</button>
            <button class="btn btn-secondary key" onclick="appendInput('7')">7</button>
            <button class="btn btn-secondary key" onclick="appendInput('8')">8</button>
            <button class="btn btn-secondary key" onclick="appendInput('9')">9</button>
            <button class="btn btn-secondary key" onclick="appendInput('*')">*</button>
            <button class="btn btn-secondary key" onclick="appendInput('0')">0</button>
            <button class="btn btn-secondary key" onclick="appendInput('#')">#</button>
            <button class="btn btn-warning key" onclick="callManager()"><i class="fa-solid fa-bell"></i></button>
            <button class="btn btn-primary key" onclick="startInput()"><i class="fa-solid fa-phone"></i></button>
            <button class="btn btn-danger key" onclick="clearInput()"><i class="fa-solid fa-xmark"></i></button>
          </div>
        </div>
      </div>
    </div>

    <script>
      let input = ""; // 입력값 저장
      let stage = "LIVE"; // 현재 단계
      let enteredHouse = ""; // 입력된 세대 호수
      const correctCombination = "10011234"; // 올바른 값
      const screen = document.getElementById("screen");

      function updateScreen() {
        if (stage === "CALL") {
          screen.textContent = `세대호수: ${input.padEnd(4, "_")}`;
        } else if (stage === "PASSWORD") {
          screen.textContent = `비밀번호: ${input.padEnd(4, "_").replace(/./g, "*")}`;
        } else {
          screen.textContent = stage; // LIVE, OPEN, 비밀번호 틀림 등 상태
        }
      }

      function appendInput(value) {
        if (stage === "CALL" && input.length < 4) {
          input += value;
          if (input.length === 4) {
            enteredHouse = input;
            input = "";
            stage = "PASSWORD";
          }
          updateScreen();
        } else if (stage === "PASSWORD" && input.length < 4) {
          input += value;
          if (input.length === 4) {
            verifyInput();
          }
          updateScreen();
        }
      }

      function startInput() {
        stage = "CALL";
        input = "";
        updateScreen();
      }

      function clearInput() {
        stage = "LIVE";
        input = "";
        enteredHouse = "";
        updateScreen();
      }

      function verifyInput() {
        const fullInput = enteredHouse + input; // 세대호수와 비밀번호 조합
        if (fullInput === correctCombination) {
          stage = "OPEN";
          sendCommand();
          updateScreen();
          setTimeout(clearInput, 2000);
        } else {
          stage = "비밀번호 틀림";
          updateScreen();
          setTimeout(clearInput, 2000);
        }
      }

      function callManager() {
        alert("관리실 호출 중...");
      }

      // websocket setting
      var webSocketDoorUrl = "ws://" + window.location.hostname + "/door";
        var websocketDoor;

        function initDoorWebSocket() {
            websocketDoor = new WebSocket(webSocketDoorUrl);
            websocketDoor.onopen = function(event) {
                console.log("WebSocket connected");
            };
            websocketDoor.onclose = function(event) {
                console.log("WebSocket disconnected");
                setTimeout(initDoorWebSocket, 2000);
            };
            websocketDoor.onerror = function(event) {
                console.error("WebSocket error:", event);
            };
            websocketDoor.onmessage = function(event) {
                console.log("Message received:", event.data);
            };
        }

        function sendCommand() {
            if (websocketDoor && websocketDoor.readyState === WebSocket.OPEN) {
                console.log("Sending command...");
                websocketDoor.send("move");
            } else {
                console.error("WebSocket is not connected.");
            }
        }

        window.onload = initDoorWebSocket;
      // /websocket setting


    </script>
  </body>
</html>

)rawliteral";

#endif
