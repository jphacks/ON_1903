function onClick(elmnt, choice) {
  console.log(choice);

  const request = new XMLHttpRequest();

  request.open('GET', 'http://localhost:5000', true);
  request.responseType = 'json';

  request.onload = function () {
      const resp = this.response;
      console.log(resp);
  };

  request.send();
}

function requestQuestion() {
  const request = new XMLHttpRequest();

  request.open('GET', 'http://localhost:5000/q', true);
  request.responseType = 'json';

  request.onload = function () {
      const resp = this.response;
      console.log(resp);
      document.getElementById('question').innerText = resp.question
  };

  request.send();
}

function postChoice() {
  const request = new XMLHttpRequest();

  const data = {choice: 0};

  request.open('GET', 'http://localhost:5000/choice', true);
  request.setRequestHeader("Content-Type", "application/json");

  request.onload = function () {
      const resp = this.response;
      console.log(resp);
  };

  request.send(JSON.stringify(data));
}
