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
        }
    }

    constructor() {
        super();
        this.user = null;

        const dbCardsReference = db.ref('/cards_prod');

        this.cards = [];

        dbCardsReference.on('child_added', (data) => {
            console.log("card added", data);

            const cardId = data.key;
            const cardData = data.val();

            this.cards.push({cardId, cardData});
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
                    ? html`<bbzz-cards .cards="${this.cards}"></bbzz-cards>`
                    : html`<bbzz-configs></bbzz-configs>`
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