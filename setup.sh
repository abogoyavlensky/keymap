#!/bin/bash
sudo mkdir -p /opt/xmodmap
sudo cp xkblayout-state /opt/xmodmap/xkblayout-state
sudo cp xmodmap.py /opt/xmodmap/xmodmap.py
sudo chmod a+x /opt/xmodmap/xmodmap.py
sudo chmod a+x /opt/xmodmap/xkblayout-state
sudo cp .Xmodmap /opt/xmodmap/.Xmodmap
sudo cp .Xmodmap_ru /opt/xmodmap/.Xmodmap_ru
sudo cp xmodmap.service /etc/systemd/system/xmodmap.service
