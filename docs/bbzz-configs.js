import { LitElement, html, css } from 'https://unpkg.com/lit-element@2.4.0/lit-element.js?module';
import 'https://unpkg.com/@material/mwc-formfield@0.18.0/mwc-formfield.js?module';
import 'https://unpkg.com/@material/mwc-textfield@0.18.0/mwc-textfield.js?module';

import './bbzz-config.js'

class BBZZConfigs extends LitElement {
    static get properties() {
        return {
            configs: {type:Array},
        }
    }

    constructor() {
        super();
        this.configs = [];
    }

    render() {
        return html`
      <div class='container'>
        <div class='header'>
          <img src="img/config.png" height="150" alt="">
          <h1>BipBipZiZik Configs editor</h1>
          <h4>
            This page allows to edit all configs.<br>
            Find your raspberry ID and choose your config.
          </h4>
        </div>
        <h2>Configs</h2>
        <h4>CREATE/UPDATE</h4>
        <div class="configs">
            ${this.configs.map(config => html`<bbzz-config .config="${config}"></bbzz-config>`) }
        </div>
      </div>  
    `;
    }

    static get styles() {
        return css``;
    }
}

customElements.define('bbzz-configs', BBZZConfigs);