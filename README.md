# DB410c MQTT publish on Scalenics w/SORACOM

1.Install python-pip and paho-mqtt

    apt-get install python-pip
    pip install paho-mqtt

2.Clone this repository

    git clone https://github.com/tmurasawa/db410c_soracom_din.git

3.Run program

    python ./db410c_soracom_din.py

4.Publish D-in data to Scalenics

* Login Scalenics Management Console
* Go to 'Device' menu
* Check new Device detected(ex.Device-ID:imsi)
* Go to 'Channel' menu
* Create new channel(ex:CH0)
* Return to 'Device' menu
* Edit new device and check 'Enabled=True' and bind new channel
* Go to 'Stream' menu
* Select 'Source:CH0' and check stream(ex. ON=1/OFF=0)

5.Have fun!!
