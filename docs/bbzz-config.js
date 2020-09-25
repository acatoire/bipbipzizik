import { LitElement, html, css } from 'https://unpkg.com/lit-element@2.4.0/lit-element.js?module';

class BBZZConfig extends LitElement {
    static get properties() {
        return {
            config: {type:Object}
        }
    }

    edit(){
        let event = new CustomEvent('bbzz-config-edit', {
            detail: {
                config: this.config
            }
        });
        this.dispatchEvent(event);
    }

    delete(){
        console.log(`remove ${this.config.configId}`);
        let event = new CustomEvent('bbzz-config-remove', {
            detail: {
                config: this.config
            }
        });
        this.dispatchEvent(event);
    }

    constructor() {
        super();
        this.config = {};
    }

    render() {
        return html`
            <div>Firebase Id:</div>
            <div> ${this.config.configId}</div>
            <div>App name:</div>
            <div>${this.config.configData.app_name}</div>
            <div>App owner:</div>
            <div>${this.config.configData.app_owner}</div>
            <div>App Id:</div>
            <div>${this.config.configData.app_id}</div>
            <div>Server IP:</div>
            <div>${this.config.configData.sonos_server_ip}</div>
            <div>Server Port:</div>
            <div>${this.config.configData.sonos_server_port}</div>
            <div>Room name:</div>
            <div>${this.config.configData.room_name}</div>
            <div>Mode:</div>
            <div>${this.config.configData.multi_read_mode}</div>
            <div>Timeout:</div>
            <div>${this.config.configData.card_timeout}</div>
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

customElements.define('bbzz-config', BBZZConfig);