import { LitElement, html, css } from 'https://unpkg.com/lit-element@2.4.0/lit-element.js?module';

class BBZZCard extends LitElement {
    static get properties() {
        return {
            card: {type:Object}
        }
    }

    edit(){
        // Sends the card to change to the cards element
        let event = new CustomEvent('bbzz-card-edit', {
            detail: {
                card: this.card
            }
        });
        this.dispatchEvent(event);
    }

    delete(){
        console.log(`remove ${this.card.cardId}`);
        // Sends the card to remove to the cards element
        let event = new CustomEvent('bbzz-card-remove', {
            detail: {
                card: this.card
            }
        });
        this.dispatchEvent(event);
    }

    constructor() {
        super();
        this.card = {};
    }

    render() {
        return html`
            <div class='Id'>Id:</div>
            <div> ${this.card.cardId}</div>
            <div class='NameLabel'>Name:</div>
            <div class='nameTile'>${this.card.cardData.name}</div>
            <div class='idsLabel'>Ids:</div>
            <div class='idsTile'>${this.card.cardData.ids}</div>
            <div class='userLabel'>User:</div>
            <div class='userTile'>${this.card.cardData.user}</div>
            <div class='actionLabel'>Action:</div>
            <div class='actionTile'>${this.card.cardData.action}</div>
            <div class='dataLabel'>Data:</div>
            <div class='dataTile'>${this.card.cardData.data}</div>
            <div class='modeLabel'>Mode:</div>
            <div class='modeTile'>${this.card.cardData.mode}</div>
            <div class='commentLabel'>Comment:</div>
            <div class='commentTile'>${this.card.cardData.comment}</div>
            <mwc-button raised label="Edit" icon="edit" @click="${this.edit}"></mwc-button>
            <mwc-button raised label="Delete" icon="delete" @click="${this.delete}"></mwc-button>
    `;
    }

    static get styles() {
        return css`
        :host{
          display: inline-block;
          width: 250px;
          padding: 10px;
          border: 1px solid #EEE;
          border-bottom: none;
          border-radius: 2px;
          background-color: #fff;
        }`;
    }
}

customElements.define('bbzz-card', BBZZCard);