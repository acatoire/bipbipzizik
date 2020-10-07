const config = {
    apiKey: "AIzaSyBDpWYywapzpuYJerHNe1aVNPsQGULBMN0",
    authDomain: "bipbipzizik.firebaseapp.com",
    databaseURL: "https://bipbipzizik.firebaseio.com",
    projectId: "bipbipzizik",
    storageBucket: "bipbipzizik.appspot.com",
    messagingSenderId: "800598547799",
    appId: "1:800598547799:web:3ee8db578f5c76da60f212",
    measurementId: "G-LPM9CG1HWR"
};

firebase.initializeApp(config);
const db = firebase.database();
const provider = new firebase.auth.GoogleAuthProvider();

export const FirebaseMixin = superclass =>
    class FirebaseMixin extends superclass {
        initFirebase(){

            // Grabbing logged in user from the local sessions
            firebase.auth().onAuthStateChanged(user => {
                this.user = user;
            });

            const dbCardsReference = db.ref('/cards_prod');
            const dbConfigReference = db.ref('/config_prod');

            /*
            Routines to keep cards in sync
             */

            dbCardsReference.on('child_added', (data) => {
                console.log("child added");
                const cardId = data.key;
                const cardData = data.val();
                this.cards = [...this.cards, {cardId, cardData}]
            });

            dbCardsReference.on('child_changed', (data) => {
                console.log("child changed", data.key);

                const cardId = data.key;
                const cardData = data.val();

                // Find which item changed, and update the array
                const item = this.cards.find(card => {
                    return card.cardId === cardId
                });
                // Get all the other items
                const otherCards = this.cards.filter(card => card.cardId !== cardId);

                this.cards = [...otherCards, {cardId, cardData}];
            });

            dbCardsReference.on('child_removed', (data) => {
                console.log("child_removed", data.key);
                this.cards = this.cards.filter(card => card.cardId !== data.key);
            });

            /*
            Routines to keep configs in sync
             */
            dbConfigReference.on('child_added', (data) => {
                console.log("config child added");
                const configId = data.key;
                const configData = data.val();
                this.configs = [...this.configs, {configId, configData}];
            });

            dbConfigReference.on('child_changed', (data) => {
                console.log("config child changed", data.key);
                const configId = data.key;
                const configData = data.val();

                const item = this.configs.find(config => {
                    return config.configId === configId
                });
                const otherConfigs = this.configs.filter(config => config.configId !== configId);

                this.configs = [...otherConfigs, {configId, configData}];
            });

            dbConfigReference.on('child_removed', (data) => {
                console.log("config child removed", data.key);
                this.configs = this.configs.filter(config => config.configId !== data.key);
            });
        }

        logIn(){
            console.log("Logging in");
            return firebase.auth().signInWithPopup(provider).then((result) =>{
                console.log("logged in");
                this.user = result.user;
            }).catch((error) =>{
                console.log("Error when logging in", error);
            });
        }

        logout(){
            console.log("Logging out");
            return firebase.auth().signOut().then(() =>{
                console.log("logged out");
                this.user = null;
            }, (error) =>{
                console.log("Error while logging out", error);
            });
        }

        saveCardToFirebase(e){
            const cardToSave = e.detail.card;
            console.log("saving to firebase ", cardToSave);

            db.ref('cards_prod/' + cardToSave.cardId).set(
                cardToSave.cardData
            );
        }

        deleteCardFromFirebase(e){
            const cardToDelete = e.detail.card;
            console.log("Removing", cardToDelete);
            db.ref('cards_prod/' + cardToDelete.cardId).remove();
        }

        saveConfigToFirebase(e){
            const configToSave = e.detail.config;
            console.log("saving to firebase ", configToSave);

            db.ref('config_prod/' + configToSave.configId).set(
                configToSave.configData
            );
        }

        deleteConfigFromFirebase(e){
            const configToDelete = e.detail.config;
            console.log("Removing", configToDelete);
            db.ref('config_prod/' + configToDelete.configId).remove();
        }
    };