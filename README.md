# zhacheck
Based on the AppDaemon from this post https://community.home-assistant.io/t/zha-show-last-seen-lqi-and-rssi-as-entity-attributes/275760/16

Add this to your apps.yaml
```
 zhacheck:
  module: zhacheck
  class: zha_check
  token: *****
  ip: ***.***.***.***
  ```
  the token is a long lived token from HA (https://www.atomicha.com/home-assistant-how-to-generate-long-lived-access-token-part-1/)
  the ip is the ip address of your HA instance (192.168.1.101)
