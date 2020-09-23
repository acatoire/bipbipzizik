import { LitElement, html, css } from 'https://unpkg.com/lit-element@2.4.0/lit-element.js?module';
import 'https://unpkg.com/@material/mwc-formfield@0.18.0/mwc-formfield.js?module';
import 'https://unpkg.com/@material/mwc-textfield@0.18.0/mwc-textfield.js?module';

import './bbzz-card.js';

class BBZZCards extends LitElement {
    static get properties() {
        return {
            cards: {type:Array},
            editedCard : {type: Object}
        }
    }

    constructor() {
        super();
        this.cards = [];
        this.editedCard = {
            cardId : Date.now(),
            cardData : {
                name: "",
                mode: "",
                ids: "",
                data: "",
                comment: "",
                action: "",
                user: ""
            }
        };
    }

    catchEditEvent(e){
        this.editedCard = e.detail.card;
        this.requestUpdate();
    }

    catchRemoveEvent(e){
        // We just forward to the admin element, who has the database connection
        let event = new CustomEvent('bbzz-card-remove-admin', {
            detail: {
                card: e.detail.card
            }
        });
        this.dispatchEvent(event);
    }

    saveCard(){
        //We send the edited card or created card to the admin view, which is the only one with the firebase access
        console.log(this.editedCard);
        let event = new CustomEvent('bbzz-card-save', {
            detail: {
                card: this.editedCard
            }
        });
        this.dispatchEvent(event);
        this.editedCard = {
            cardId : Date.now(),
            cardData : {
                name: "",
                mode: "",
                ids: "",
                data: "",
                comment: "",
                action: "",
                user: ""
            }
        };
    }

    render() {
        return html`
      <div class='container'>
        <div class='header'>
          <img src="img/card.png" height="150" alt="">
          <h1>BipBipZiZik Cards editor</h1>
          <h4>
            This page allows to edit all cards.<br>
            Edit existing card or create a new one.
          </h4>
        </div>
        <h2>Cards</h2>
        <h4>CREATE/UPDATE</h4>
            <div class="edit-card">
                <mwc-textfield outlined label="Name" value="${this.editedCard.cardData.name}" @change=${(e) => this.editedCard.cardData.name = e.target.value}"></mwc-textfield>
                <mwc-textfield outlined label="User" .value="${this.editedCard.cardData.user}" @change=${(e) => this.editedCard.cardData.user = e.target.value}"></mwc-textfield>
                <mwc-textfield outlined label="Ids" .value="${this.editedCard.cardData.ids}" @change=${(e) => this.editedCard.cardData.ids = e.target.value}"></mwc-textfield>
                <mwc-textfield outlined label="Action" .value="${this.editedCard.cardData.action}" @change=${(e) => this.editedCard.cardData.action = e.target.value}"></mwc-textfield>
                <mwc-textfield outlined label="Data" .value="${this.editedCard.cardData.data}" @change=${(e) => this.editedCard.cardData.data = e.target.value}"></mwc-textfield>
                <mwc-textfield outlined label="Mode" .value="${this.editedCard.cardData.mode}" @change=${(e) => this.editedCard.cardData.mode = e.target.value}"></mwc-textfield>
                <mwc-textfield outlined label="Comment" .value="${this.editedCard.cardData.comment}" @change=${(e) => this.editedCard.cardData.comment = e.target.value}"></mwc-textfield>
                <mwc-button raised label="Save or Update" icon="save" @click="${this.saveCard}"></mwc-button>
            </div>
        <h4>READ/DELETE</h4>
        <div class="cards">
            ${this.cards.map(card => html`<bbzz-card @bbzz-card-edit="${this.catchEditEvent}" @bbzz-card-remove="${this.catchRemoveEvent}" .card="${card}"></bbzz-card>`) }
        </div>
      </div>
    `;
    }

    static get styles() {
        return css``;
    }
}

customElements.define('bbzz-cards', BBZZCards);