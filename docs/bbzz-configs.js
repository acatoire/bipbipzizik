import { LitElement, html, css } from 'https://unpkg.com/lit-element@2.4.0/lit-element.js?module';
import 'https://unpkg.com/@material/mwc-formfield@0.18.0/mwc-formfield.js?module';
import 'https://unpkg.com/@material/mwc-textfield@0.18.0/mwc-textfield.js?module';

import './bbzz-config.js'

class BBZZConfigs extends LitElement {
    static get properties() {
        return {
            configs: {type:Array},
            editedConfig : {type: Object}
        }
    }

    constructor() {
        super();
        this.configs = [];
        this.editedConfig = {
            configId : Date.now(),
            configData : {
                app_name: "",
                app_owner: "",
                app_id: "",
                sonos_server_ip: "",
                sonos_server_port: "",
                room_name: "",
                multi_read_mode: "",
                card_timeout: ""
            }
        };
    }

    catchEditConfigEvent(e){
        this.editedConfig = e.detail.config;
        this.requestUpdate();
    }

    catchRemoveConfigEvent(e){
        let event = new CustomEvent('bbzz-config-remove-admin', {
            detail: {
                config: e.detail.config
            }
        });
        this.dispatchEvent(event);
    }

    saveConfig(){
        let event = new CustomEvent('bbzz-config-save', {
            detail: {
                config: this.editedConfig
            }
        });
        this.dispatchEvent(event);
        this.editedConfig = {
            configId : Date.now(),
            configData : {
                app_name: "",
                app_owner: "",
                app_id: "",
                sonos_server_ip: "",
                sonos_server_port: "",
                room_name: "",
                multi_read_mode: "",
                card_timeout: ""
            }
        };
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
        <div class="edit-card">
            <mwc-textfield outlined label="App Name" .value="${this.editedConfig.configData.app_name}" @change=${(e) => this.editedConfig.configData.app_name = e.target.value}"></mwc-textfield>
            <mwc-textfield outlined label="App Owner" .value="${this.editedConfig.configData.app_owner}" @change=${(e) => this.editedConfig.configData.app_owner = e.target.value}"></mwc-textfield>
            <mwc-textfield outlined label="App Id" .value="${this.editedConfig.configData.app_id}" @change=${(e) => this.editedConfig.configData.app_id = e.target.value}"></mwc-textfield>
            <mwc-textfield outlined label="Server IP" .value="${this.editedConfig.configData.sonos_server_ip}" @change=${(e) => this.editedConfig.configData.sonos_server_ip = e.target.value}"></mwc-textfield>
            <mwc-textfield outlined label="Server port" .value="${this.editedConfig.configData.sonos_server_port}" @change=${(e) => this.editedConfig.configData.sonos_server_port = e.target.value}"></mwc-textfield>
            <mwc-textfield outlined label="Room name" .value="${this.editedConfig.configData.room_name}" @change=${(e) => this.editedConfig.configData.room_name = e.target.value}"></mwc-textfield>
            <mwc-textfield outlined label="Mode" .value="${this.editedConfig.configData.multi_read_mode}" @change=${(e) => this.editedConfig.configData.multi_read_mode = e.target.value}"></mwc-textfield>
            <mwc-textfield outlined label="Timeout" .value="${this.editedConfig.configData.card_timeout}" @change=${(e) => this.editedConfig.configData.card_timeout = e.target.value}"></mwc-textfield>
            <mwc-button raised label="Save or Update" icon="save" @click="${this.saveConfig}"></mwc-button>
        </div>
        <h4>READ/DELETE</h4>
        <div class="configs">
            ${this.configs.map(config => html`<bbzz-config @bbzz-config-edit="${this.catchEditConfigEvent}" @bbzz-config-remove="${this.catchRemoveConfigEvent}" .config="${config}"></bbzz-config>`) }
        </div>
      </div>  
    `;
    }

    static get styles() {
        return css``;
    }
}

customElements.define('bbzz-configs', BBZZConfigs);