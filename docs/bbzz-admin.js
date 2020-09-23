import { LitElement, html, css } from 'https://unpkg.com/browse/lit-element@2.4.0/lit-element.js?module';

class BBZZAdmin extends LitElement {
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
                <h1>BipBipZiZik admin interface</h1>
                <h4>Lets config everything</h4>
              </div>
              <h2>Cards</h2>
              <div class=cardLink>
                <a href="cards.html">Card edit</a>
              </div>
              <div class=configLink>
                <a href="configs.html">Config edit</a>
              </div>
            </div>
    `;
    }

    static get styles() {
        return css`
      :host {
      }
    `;
    }
}

customElements.define('bbzz-admin', BBZZAdmin);