
To start with, update API_KEY in palm_api.py
You can update the kea-dhcp4.csv, if required.


**Sample Output:
**

C:\Scripts\python.exe  nlp2sql.py 

(NLP -> SQL -> NLP) How can i help you ? what is the table name?


The table name is Kea_DHCP_Server_assigned_IP


→ SQL Query for reference: SELECT name FROM sqlite_master WHERE type='table';

(NLP -> SQL -> NLP).. any more query ?  how many records are there?


There are 20 records.


→ SQL Query for reference: SELECT count(*) FROM Kea_DHCP_Server_assigned_IP

(NLP -> SQL -> NLP).. any more query ?  display only first two records


**IP Address** | **Hardware Address** | **Client ID** | **Valid Lifetime** | **Expire Timestamp** | **SubnetId** | **Hostname**
----------|----------------|--------------|----------------|-------------|-------------|-------------
192.168.1.100 | 00:1a:2b:3c:4d:5e | 01:02:03:04:05:06 | 86400 | 1679875199 | 1 | laptop-1
192.168.1.101 | 00:0a:1b:2c:3d:4e | 11:22:33:44:55:66 | 43200 | 1679896799 | 1 | printer-1


→ SQL Query for reference: SELECT * FROM Kea_DHCP_Server_assigned_IP LIMIT 2;

(NLP -> SQL -> NLP).. any more query ?  is there duplicate entries in IP address ?


**There are no duplicate entries in the IP address column.**


→ SQL Query for reference: SELECT count(*),ipaddress FROM Kea_DHCP_Server_assigned_IP GROUP BY ipaddress HAVING count(*) > 1

(NLP -> SQL -> NLP).. any more query ?  is there duplicate entries in Hardware address ?


Yes, there are duplicate entries in Hardware address.

    The following table shows the duplicate entries:

    | Hardware Address | Count |
    |---|---|
    | 00:0a:1b:2c:3d:4e | 5 |
    | 00:11:22:33:44:55 | 3 |
    | 00:1a:2b:3c:4d:5e | 5 |
    | 00:aa:bb:cc:dd:ee | 7 |


→ SQL Query for reference: SELECT HardwareAddress, count(*)
    FROM Kea_DHCP_Server_assigned_IP
    GROUP BY HardwareAddress
    HAVING count(*) > 1

(NLP -> SQL -> NLP).. any more query ?  what is the hostname and hardware address for the IP address 192.168.1.100


The hostname for the IP address 192.168.1.100 is laptop-1 and the hardware address is 00:1a:2b:3c:4d:5e.


→ SQL Query for reference: SELECT Hostname, HardwareAddress FROM Kea_DHCP_Server_assigned_IP WHERE IPAddress = '192.168.1.100'

(NLP -> SQL -> NLP).. any more query ?  thanks

Thanks You !

Process finished with exit code 0
