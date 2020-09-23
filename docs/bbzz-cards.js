import { LitElement, html, css } from 'https://unpkg.com/lit-element@2.4.0/lit-element.js?module';

class BBZZCards extends LitElement {
    static get properties() {
        return {
        }
    }

    constructor() {
        super();
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
          <div id="firebase-login">
            <button id="firebase-login-button" onclick="logIn()">Log in using Google</button>
          </div>
        </div>
        <h2>Cards</h2>
        <h4>CREATE/UPDATE</h4>
        <h4>READ/DELETE</h4>
      </div>
    `;
    }

    static get styles() {
        return css``;
    }
}

customElements.define('bbzz-cards', BBZZCards);