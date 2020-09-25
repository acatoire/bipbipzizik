import { LitElement, html, css } from 'https://unpkg.com/lit-element@2.4.0/lit-element.js?module';
import 'https://unpkg.com/@material/mwc-button@0.18.0/mwc-button.js?module';
import 'https://unpkg.com/@material/mwc-tab-bar@0.18.0/mwc-tab-bar.js?module';

import './bbzz-cards.js';
import './bbzz-configs.js';

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

class BBZZAdmin extends LitElement {

    static get properties() {
        return {
            selectedTab : {type: Number},
            user : {type : Object},
            cards : {type: Array},
            configs : {type: Array},
        }
    }

    constructor() {
        super();
        this.user = null;
        this.cards = [];
        this.configs = [];

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
            const otherCards = this.cards.filter(card => card.cardId === cardId);

            this.cards = [...otherCards, {cardId, cardData}];
        });

        dbCardsReference.on('child_removed', (data) => {
            console.log("child_removed", data.key);
            this.cards = this.cards.filter(card => card.cardId != data.key);
        });

        /*
        Routines to keep configs in sync
         */
        dbConfigReference.on('child_added', (data) => {
            console.log("config child added");
            const configId = data.key;
            const configData = data.val();
            this.configs = [...this.configs, {configId, configData}]
        });

        dbConfigReference.on('child_changed', (data) => {
            console.log("config child changed", data.key);
            const configId = data.key;
            const configData = data.val();

            const item = this.configs.find(config => {
                return config.configId === configId
            });
            const otherConfigs = this.configs.filter(config => config.configId === configId);

            this.configs = [...otherConfigs, {configId, configData}];
        });

        dbConfigReference.on('child_removed', (data) => {
            console.log("config child removed", data.key);
            this.configs = this.configs.filter(config => config.configId != data.key);
        });
    }

    tabClicked(e){
        this.selectedTab = e.detail.index;
    }

    logIn(){
        console.log("Logging in");
        firebase.auth().signInWithPopup(provider).then((result) =>{
            console.log("logged in");
            this.user = result.user;
        }).catch((error) =>{
            console.log("Error when logging in", error);
        });

    }

    logout(){
        console.log("Logging out");
        firebase.auth().signOut().then(() =>{
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

    render() {
        return html`
            <div class='container'>
              <div class='header'>
                <h1>BipBipZiZik admin interface</h1>
                <h4>Lets config everything</h4>
                <div class="login-button">
                    ${this.user
                        ? html`
                            <p>Logged in as ${this.user.email}</p>
                            <mwc-button raised label="Logout" icon="login" @click="${this.logout}"></mwc-button>
                        `
                        : html`<mwc-button raised label="LogIn with Google" icon="login" @click="${this.logIn}"></mwc-button>`
                    }
                </div>
              </div>
              <div class="app">
                <mwc-tab-bar @MDCTabBar:activated=${this.tabClicked}> 
                  <mwc-tab label="Cards"></mwc-tab>
                  <mwc-tab label="Configs"></mwc-tab>
                </mwc-tab-bar>
                
                ${this.selectedTab === 0
                    ? html`<bbzz-cards .cards="${this.cards}" @bbzz-card-save="${this.saveCardToFirebase}" @bbzz-card-remove-admin="${this.deleteCardFromFirebase}"></bbzz-cards>`
                    : html`<bbzz-configs .configs="${this.configs}" @bbzz-config-save="${this.saveConfigToFirebase}" @bbzz-config-remove-admin="${this.deleteConfigFromFirebase}"></bbzz-configs>`
                }
              </div>
            </div>
    `;
    }

    static get styles() {
        return css`
            div, input, a, button, ul, li {
              box-sizing: border-box;
            }

            .container {
              max-width: 100%;
              width: 760px;
              margin: 0 auto;
            }
      
              .header {
              text-align: center;
              padding-top: 50px;
            }
    
            .header h1,
            .header h4 {
              font-weight: normal;
              margin: 10px 0;
            }
            
            .header img {
              border-radius: 50%;
              box-shadow: 0 1px 1px rgba(0,0,0,.1),0 1px 1px rgba(0,0,0,.1);
            }
        `;
        }
}

customElements.define('bbzz-admin', BBZZAdmin);