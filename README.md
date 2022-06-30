# ZHA disconnected device check
Based on the AppDaemon from this post https://community.home-assistant.io/t/zha-show-last-seen-lqi-and-rssi-as-entity-attributes/275760/16
This compares the last seen attribute of all ZHA(Zigbee) devices and if it hasnt been seen for 120 mins its considered offline and added to the attributes of the sensor.zha_last_seen entity

![image](https://user-images.githubusercontent.com/2896329/176730644-e24fe5be-1d91-40ea-a4ff-c3e2f28abd64.png)

---
Add this to your apps.yaml
```
 zhacheck:
  module: zhacheck
  class: zha_check
  token: *****
  ip: ***.***.***.***
  max: 7200
  print: 1
  ```
  the token is a long lived token from HA (https://www.atomicha.com/home-assistant-how-to-generate-long-lived-access-token-part-1/)
  
  the ip is the ip address of your HA instance (192.168.1.101)
  
  max is the max time before considered offline in seconds
  
  print will add or remove the Friendly name and Icon from the attributes section of the sensor.zha_last_seen entity (1 to add them 0 to remove)
  ![image](https://user-images.githubusercontent.com/2896329/176738618-61477913-fdba-433d-888e-3490336deb7b.png)

  
  ---

The app checks every 5 minutes but you can manually call it via an automation ex.

![image](https://user-images.githubusercontent.com/2896329/176730948-9354dd81-9d51-496c-9d79-2adeae72baf6.png)
