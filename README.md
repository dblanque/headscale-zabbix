## Introduction
Zabbix Monitoring script-set for Headscale.

This is provided as is and has no warranty whatsoever.

Feel free to contribute by reporting bugs or submitting PRs!

*Tested on Zabbix 7.0 LTS*

### IMPORTANT NOTICE

It is very important that you DO NOT remove the python cleanup script,
as it deletes the Headscale keys from the JSON data locally before transferring
the data over the network.

These keys should not ever be stored remotely in the Zabbix Server.

### Would you like to support me?
<a href='https://ko-fi.com/E1E2YQ4TG' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://storage.ko-fi.com/cdn/kofi2.png?v=3' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>

## Functionalities

## Installation

If you use `zabbix_agentd` it should also be compatible, but I use
`zabbix_agent2`. You may need to change the paths to accomodate using the V1
agent.

### Headscale Configuration

To configure this template you must execute the following commands (or add
the sudoers/zabbix files manually).

#### Sudoers Files
```
curl --create-dirs -o /etc/sudoers.d/ https://raw.githubusercontent.com/dblanque/headscale-zabbix/main/sudoers.d/zabbix_headscale && \
chmod 0440 /etc/sudoers.d/zabbix_headscale && visudo -c
```

#### Zabbix Config Files
```
curl --create-dirs -o /etc/zabbix/zabbix_agent2.d/ https://raw.githubusercontent.com/dblanque/headscale-zabbix/main/zabbix_agent2.d
```

After this you may need to **Restart your Zabbix Agent**.

### Zabbix Configuration

Import the YAML Template and link it to your Headscale Host(s).
