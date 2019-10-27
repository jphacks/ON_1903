let user_id = 0;
let isContinue = true;

window.onload = function () {
    getNewJinn();
};

function getNewJinn() {
    const request = new XMLHttpRequest();

    request.open('GET', 'http://localhost:5000/jinn/new', true);
    request.responseType = 'json';

    request.onload = function () {
        const resp = this.response;
        console.log(resp);
        user_id = resp.user_id;
        getQuestion();
    };

    request.send();
}

function onClick(elmnt, choice) {
  if (isContinue) {
    console.log(choice);
    postChoice(choice);
  }
}

function getQuestion() {
  const request = new XMLHttpRequest();

  request.open('GET', `http://localhost:5000/jinn/${user_id}/question`, true);
  request.responseType = 'json';

  request.onload = function () {
      const resp = this.response;
      console.log(resp);
      isContinue =  resp.continue;
      document.getElementById('question').innerText = resp.question;
  };

  request.send();
}

function postChoice(choice) {
  const request = new XMLHttpRequest();

  const data = {answer: choice};

  request.open('POST', `http://localhost:5000/jinn/${user_id}/answer`, true);
  request.setRequestHeader("Content-Type", "application/json");

  request.onload = function () {
      const resp = this.response;
      console.log(resp);
      getQuestion();
  };

  request.send(JSON.stringify(data));
}
