let user_id = 0;
let isContinue = true;
let api_config = "https://radiant-basin-04347.herokuapp.com/";

window.onload = function () {
    getNewJinn();
};

function getNewJinn() {
    const request = new XMLHttpRequest();

    request.open('GET', `${api_config}jinn/new`, true);
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

  request.open('GET', `${api_config}jinn/${user_id}/question`, true);
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

  request.open('POST', `${api_config}jinn/${user_id}/answer`, true);
  request.setRequestHeader("Content-Type", "application/json");

  request.onload = function () {
      const resp = this.response;
      console.log(resp);
      getQuestion();
  };

  request.send(JSON.stringify(data));
}
