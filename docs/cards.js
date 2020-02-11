
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
var cardName =     document.getElementById('nameText');
var cardUser =     document.getElementById('userText');
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
var cardsDiv = document.getElementById('cards');
var cardsRef = db.ref('/cards_prod');

cardsRef.on('child_added', (data) => {
  var newDiv = document.createElement('div')
  newDiv.id = data.key;
  newDiv.className = "cardTile";
  newDiv.innerHTML = cardTemplate(data.val())
  cardsDiv.appendChild(newDiv);
});

cardsRef.on('child_changed', (data) => {
  var node = document.getElementById(data.key);
  node.innerHTML = cardTemplate(data.val());
});

cardsRef.on('child_removed', (data) => {
  var node = document.getElementById(data.key);
  node.parentNode.removeChild(node);
});



// Action on CARD
cardsDiv.addEventListener('click', (e) => 
{
  var cardNode = e.target.parentNode

  // Update card editor view
  if (e.target.classList.contains('edit')) 
  {
    cardName.value = cardNode.querySelector('.nameTile').innerText;
    cardIds.value  = cardNode.querySelector('.idsTile').innerText;
    cardUser.value  = cardNode.querySelector('.userTile').innerText;
    cardAction.value = cardNode.querySelector('.actionTile').innerText;
    cardData.value  = cardNode.querySelector('.dataTile').innerText;
    cardMode.value = cardNode.querySelector('.modeTile').innerText;
    cardComment.value  = cardNode.querySelector('.commentTile').innerText;
    cardHiddenId.value = cardNode.id;
  }

  // Delet card in database
  if (e.target.classList.contains('delete')) 
  {
    var id = cardNode.id;
    db.ref('cards_prod/' + id).remove();
  }
});

function cardTemplate({name, ids, user, action, data, mode, comment}) 
{
  return `
    <div class='nameTile'>${name}</div>
    <div class='idsLabel'>Ids:</div>
    <div class='idsTile'>${ids}</div>
    <div class='userLabel'>User:</div>
    <div class='userTile'>${user}</div>
    <div class='actionLabel'>Action:</div>
    <div class='actionTile'>${action}</div>
    <div class='dataLabel'>Data:</div>
    <div class='dataTile'>${data}</div>
    <div class='modeLabel'>Mode:</div>
    <div class='modeTile'>${mode}</div>
    <div class='commentLabel'>Comment:</div>
    <div class='commentTile'>${comment}</div>
    <button class='delete'>Delete</button>
    <button class='edit'>Edit</button>
  `
};
