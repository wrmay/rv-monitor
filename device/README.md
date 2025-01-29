# Design

We want to be able to remotely update the software on our Pi.  We'll set it up to reach out and download 
software from github periodically.

The device will have an "IoT Bootstrap" that consists of 2 cron job.  One that runs every 1-5 minutes, which is 
meant to collect and send data, and another that runs every 1-3 hours to check for updates to the main script.

How will we deal with connection parameters for MQTT ?  What about device setup steps like loading drivers ?? 

# DS18B20 Thermometer 

https://www.waveshare.com/wiki/Raspberry_Pi_Tutorial_Series:_1-Wire_DS18B20_Sensor
https://pinout.xyz/pinout/1_wire
https://www.raspberrypi.com/documentation/computers/config_txt.html#what-is-config-txt
https://www.raspberrypi.com/documentation/computers/configuration.html#part3.1



Run the `dtoverlay` command to set up your pi 
```
randy@pi501:/sys/bus $ ls /sys/bus
amba       cec          clocksource  cpu           gadget  gpio  i2c              mdio_bus  mipi-dsi  mmc_rpmb  pci          platform  sdio    serial-base  soc  usb
auxiliary  clockevents  container    event_source  genpd   hid   iscsi_flashnode  media     mmc       nvmem     pci_express  scsi      serial  snd_seq      spi  workqueue
randy@pi501:/sys/bus $ sudo dtoverlay w1-gpio-pi5  gpiopin=4 pullup=0
randy@pi501:/sys/bus $ ls /sys/bus
amba       cec          clocksource  cpu           gadget  gpio  i2c              mdio_bus  mipi-dsi  mmc_rpmb  pci          platform  sdio    serial-base  soc  usb  workqueue
auxiliary  clockevents  container    event_source  genpd   hid   iscsi_flashnode  media     mmc       nvmem     pci_express  scsi      serial  snd_seq      spi  w1
randy@pi501:/sys/bus $
```

```
[all]
dtoverlay=w1-gpio-pi5
dtparam=gpiopin=4,pullup=0
```

# AWS MQTT

To find an endpoint: `aws iot describe-endpoint --endpoint-type iot:Data-ATS` 