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

### Headscale Configuration

### Zabbix Configuration

To enable this template you must add the following custom keys in the Zabbix
Service Configuration file directory.

```
```

