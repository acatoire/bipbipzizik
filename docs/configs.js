
// from https://github.com/VoloshinS/firebase-crud-example

var config = {
  apiKey: "AIzaSyBDpWYywapzpuYJerHNe1aVNPsQGULBMN0",
  authDomain: "bipbipzizik.firebaseapp.com",
  databaseURL: "https://bipbipzizik.firebaseio.com",
  storageBucket: "bipbipzizik.appspot.com",
};

firebase.initializeApp(config);
var db = firebase.database();



// CREATE CONFIG
var configForm =     document.getElementById('configForm');
var configHiddenId = document.getElementById('hiddenIdText');
var configName =     document.getElementById('NameText');
var configUser =     document.getElementById('userText');
var configId =       document.getElementById('idText');
var configIp =       document.getElementById('sonosIpText');
var configPort =     document.getElementById('sonosPortText');
var configRoom =     document.getElementById('roomText');
var configMode =     document.getElementById('multiReadText');
var configTimeout =  document.getElementById('timeoutText');

configForm.addEventListener('submit', (e) => 
{
  e.preventDefault();

  //Prevent empty Config
  if (!configName.value || !configUser.value || !configName.value || !configId.value)
  {
    return null
  } 

  var id = configHiddenId.value || Date.now()

  db.ref('config_prod/' + id).set(
    {
      app_name: configName.value,
      app_owner: configUser.value,
      app_id: configId.value,
      sonos_server_ip: configIp.value,
      sonos_server_port: configPort.value,
      room_name: configRoom.value,
      multi_read_mode: configMode.value,
      card_timeout: configTimeout.value
    }
  );

  configName =     '';
  configUser =     '';
  configId =       '';
  configIp =       '';
  configPort =     '';
  configRoom =     '';
  configMode =     '';
  configTimeout =  '';
});


// READ CONFIGS
var configDiv = document.getElementById('configs');
var configRef = db.ref('/config_prod');

configRef.on('child_added', (data) => {
  var newDiv = document.createElement('div')
  newDiv.id = data.key;
  newDiv.className = "configTile";
  newDiv.innerHTML = configTemplate(data.val())
  configDiv.appendChild(newDiv);
});

configRef.on('child_changed', (data) => {
  var node = document.getElementById(data.key);
  node.innerHTML = configTemplate(data.val());
});

configRef.on('child_removed', (data) => {
  var node = document.getElementById(data.key);
  node.parentNode.removeChild(node);
});



// Action on config
configDiv.addEventListener('click', (e) => 
{
  var node = e.target.parentNode

  // Update editor view
  if (e.target.classList.contains('edit')) 
  {
    node.value = node.querySelector('.nameTile').innerText;

    configName.value =     node.querySelector('.nameTile').innerText;
    configUser.value =     node.querySelector('.userTile').innerText;
    configId.value =       node.querySelector('.idTile').innerText;
    configIp.value =       node.querySelector('.ipTile').innerText;
    configPort.value =     node.querySelector('.portTile').innerText;
    configRoom.value =     node.querySelector('.roomTile').innerText;
    configMode.value =     node.querySelector('.modeTile').innerText;
    configTimeout.value =  node.querySelector('.timeoutTile').innerText;
    configHiddenId.value = node.id;
  }

  // Delet config in database
  if (e.target.classList.contains('delete')) 
  {
    var id = node.id;
    db.ref('config_prod/' + id).remove();
  }
});

function configTemplate({app_name, app_owner, app_id, sonos_server_ip, 
                         sonos_server_port, room_name, multi_read_mode, card_timeout}) 
{
  return `
    <div class='nameTile'>${app_name}</div>
    <div class='userLabel'>User:</div>
    <div class='userTile'>${app_owner}</div>
    <div class='idLabel'>Id:</div>
    <div class='idTile'>${app_id}</div>
    <div class='ipLabel'>Ip:</div>
    <div class='ipTile'>${sonos_server_ip}</div>
    <div class='portLabel'>Port:</div>
    <div class='portTile'>${sonos_server_port}</div>
    <div class='roomLabel'>Room:</div>
    <div class='roomTile'>${room_name}</div>
    <div class='modeLabel'>Mode:</div>
    <div class='modeTile'>${multi_read_mode}</div>
    <div class='timeoutLabel'>Timeout:</div>
    <div class='timeoutTile'>${card_timeout}</div>
    <button class='delete'>Delete</button>
    <button class='edit'>Edit</button>
  `
};
