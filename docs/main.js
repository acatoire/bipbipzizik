var config = {
  apiKey: "AIzaSyBDpWYywapzpuYJerHNe1aVNPsQGULBMN0",
  authDomain: "bipbipzizik.firebaseapp.com",
  databaseURL: "https://bipbipzizik.firebaseio.com",
  storageBucket: "bipbipzizik.appspot.com",
};

firebase.initializeApp(config);
var db = firebase.database();

// CREATE CARD

var cardForm = document.getElementById('cardForm');
var hiddenId   = document.getElementById('hiddenId');
var name = document.getElementById('name');
var ids = document.getElementById('ids');
var action = document.getElementById('action');
var data = document.getElementById('data');
var mode = document.getElementById('mode');
var comment = document.getElementById('comment');

cardForm.addEventListener('submit', (e) => {
  e.preventDefault();

  if (!name.value || !ids.value) return null

  var id = hiddenId.value || Date.now()

  db.ref('cards_prod/' + id).set({
    name: name.value,
    ids: ids.value,
    action: action.value,
    data: data.value,
    mode: mode.value,
    comment: comment.value
  });

  hiddenId.value = '';
  name.value = '';
  ids.value  = '';
  action.value  = '';
  data.value  = '';
  mode.value  = '';
  comment.value  = '';
});

// READ CARDS

var cards = document.getElementById('cards');
var cardsRef = db.ref('/cards_prod');

cardsRef.on('child_added', (data) => {
  var li = document.createElement('li')
  li.id = data.key;
  li.innerHTML = cardTemplate(data.val())
  cards.appendChild(li);
});

cardsRef.on('child_changed', (data) => {
  var cardNode = document.getElementById(data.key);
  cardNode.innerHTML = cardTemplate(data.val());
});

cardsRef.on('child_removed', (data) => {
  var cardNode = document.getElementById(data.key);
  cardNode.parentNode.removeChild(cardNode);
});

cards.addEventListener('click', (e) => {
  var cardNode = e.target.parentNode

  // UPDATE CARD
  if (e.target.classList.contains('edit')) {
    name.value = cardNode.querySelector('.name').innerText;
    ids.value  = cardNode.querySelector('.ids').innerText;
    action.value = cardNode.querySelector('.action').innerText;
    data.value  = cardNode.querySelector('.data').innerText;
    mode.value = cardNode.querySelector('.mode').innerText;
    comment.value  = cardNode.querySelector('.comment').innerText;
    hiddenId.value = cardNode.id;
  }

  // DELETE CARD
  if (e.target.classList.contains('delete')) {
    var id = cardNode.id;
    db.ref('cards_prod/' + id).remove();
  }
});

function cardTemplate({name, ids, action, data, mode, comment}) {
  return `
    <div class='nameLabel'>Name:</div>
    <div class='name'>${name}</div>
    <div class='idsLabel'>Ids:</div>
    <div class='ids'>${ids}</div>
    <div class='actionLabel'>Action:</div>
    <div class='action'>${action}</div>
    <div class='dataLabel'>Data:</div>
    <div class='data'>${data}</div>
    <div class='modeLabel'>Mode:</div>
    <div class='mode'>${mode}</div>
    <div class='commentLabel'>Comment:</div>
    <div class='comment'>${comment}</div>
    <button class='delete'>Delete</button>
    <button class='edit'>Edit</button>
  `
};
