
// from https://github.com/VoloshinS/firebase-crud-example

var config = {
  apiKey: "AIzaSyBDpWYywapzpuYJerHNe1aVNPsQGULBMN0",
  authDomain: "bipbipzizik.firebaseapp.com",
  databaseURL: "https://bipbipzizik.firebaseio.com",
  storageBucket: "bipbipzizik.appspot.com",
};

firebase.initializeApp(config);
var db = firebase.database();



// CREATE CARD
var cardForm =     document.getElementById('cardForm');
var cardHiddenId = document.getElementById('hiddenIdText');
var cardName =     document.getElementById('cardNameText');
var cardIds =      document.getElementById('idsText');
var cardAction =   document.getElementById('actionText');
var cardData =     document.getElementById('dataText');
var cardMode =     document.getElementById('modeText');
var cardComment =  document.getElementById('commentText');

cardForm.addEventListener('submit', (e) => 
{
  e.preventDefault();

  //Prevent empty card
  if (!cardName.value || !cardIds.value || !cardAction.value || !cardData.value)
  {
    return null
  } 

  var id = cardHiddenId.value || Date.now()

  db.ref('cards_prod/' + id).set(
    {
      name: cardName.value,
      ids: cardIds.value,
      action: cardAction.value,
      data: cardData.value,
      mode: cardMode.value,
      comment: cardComment.value
    }
  );

  cardHiddenId.value = '';
  cardName.value =     '';
  cardIds.value  =     '';
  cardAction.value  =  '';
  cardData.value  =    '';
  cardMode.value  =    '';
  cardComment.value  = '';
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



// Action on CARD
cards.addEventListener('click', (e) => 
{
  var cardNode = e.target.parentNode

  // Update card editor view
  if (e.target.classList.contains('edit')) 
  {
    cardName.value = cardNode.querySelector('.name').innerText;
    cardIds.value  = cardNode.querySelector('.ids').innerText;
    cardAction.value = cardNode.querySelector('.action').innerText;
    cardData.value  = cardNode.querySelector('.data').innerText;
    cardMode.value = cardNode.querySelector('.mode').innerText;
    cardComment.value  = cardNode.querySelector('.comment').innerText;
    cardHiddenId.value = cardNode.id;
  }

  // Delet card in database
  if (e.target.classList.contains('delete')) 
  {
    var id = cardNode.id;
    db.ref('cards_prod/' + id).remove();
  }
});

function cardTemplate({name, ids, action, data, mode, comment}) 
{
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
