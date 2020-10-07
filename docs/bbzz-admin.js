import { LitElement, html, css } from 'https://unpkg.com/lit-element@2.4.0/lit-element.js?module';
import 'https://unpkg.com/@material/mwc-button@0.18.0/mwc-button.js?module';
import 'https://unpkg.com/@material/mwc-tab-bar@0.18.0/mwc-tab-bar.js?module';

import './bbzz-cards.js';
import './bbzz-configs.js';
import {FirebaseMixin} from "./bbzz-firebase-mixin.js";

class BBZZAdmin extends FirebaseMixin(LitElement) {

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

        this.initFirebase();
    }

    tabClicked(e){
        this.selectedTab = e.detail.index;
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