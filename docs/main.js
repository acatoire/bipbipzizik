var config = {
  apiKey: "AIzaSyBDpWYywapzpuYJerHNe1aVNPsQGULBMN0",
  authDomain: "bipbipzizik.firebaseapp.com",
  databaseURL: "https://bipbipzizik.firebaseio.com",
  storageBucket: "bipbipzizik.appspot.com",
};

firebase.initializeApp(config);
var db = firebase.database();

// CREATE REWIEW

var cardForm = document.getElementById('cardForm');
var name = document.getElementById('name');
var name = document.getElementById('ids');
var hiddenId   = document.getElementById('hiddenId');

cardForm.addEventListener('submit', (e) => {
  e.preventDefault();

  if (!name.value || !ids.value) return null

  var id = hiddenId.value || Date.now()

  db.ref('cards_prod/' + id).set({
    name: name.value,
    ids: ids.value
  });

  name.value = '';
  ids.value  = '';
  hiddenId.value = '';
});

// READ REVEIWS

var cards = document.getElementById('cards');
var cardsRef = db.ref('/cards_prod');

cardsRef.on('child_added', (data) => {
  var li = document.createElement('li')
  li.id = data.key;
  li.innerHTML = cardTemplate(data.val())
  cards.appendChild(li);
});

cardsRef.on('child_changed', (data) => {
  var reviewNode = document.getElementById(data.key);
  reviewNode.innerHTML = cardTemplate(data.val());
});

cardsRef.on('child_removed', (data) => {
  var reviewNode = document.getElementById(data.key);
  reviewNode.parentNode.removeChild(reviewNode);
});

cards.addEventListener('click', (e) => {
  var reviewNode = e.target.parentNode

  // UPDATE REVEIW
  if (e.target.classList.contains('edit')) {
    name.value = reviewNode.querySelector('.name').innerText;
    ids.value  = reviewNode.querySelector('.ids').innerText;
    hiddenId.value = reviewNode.id;
  }

  // DELETE REVEIW
  if (e.target.classList.contains('delete')) {
    var id = reviewNode.id;
    db.ref('cards_prod/' + id).remove();
  }
});

function cardTemplate({name, ids}) {
  return `
    <div class='fullName'>${name}</div>
    <div class='message'>${ids}</div>
    <button class='delete'>Delete</button>
    <button class='edit'>Edit</button>
  `
};
