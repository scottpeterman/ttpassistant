examples = {
    "mac_address_table_ios": """usa1-core-01#show mac address-table 
          Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
   1    0c4f.6392.0001    DYNAMIC     Gi0/1
   1    0c4f.6392.8001    DYNAMIC     Gi0/1
   1    0c59.b769.0000    DYNAMIC     Gi0/1
   1    0cab.0018.0003    DYNAMIC     Gi0/1
   1    ca01.8e69.0038    DYNAMIC     Gi0/0
Total Mac Addresses for this criterion: 5
usa1-core-01#""",
    "cdp_detail_ios": """usa1-core-01#show cdp neigh detail
-------------------------
Device ID: usa1-core-02.home.com
Entry address(es): 
  IP address: 172.16.101.2
Platform: Cisco ,  Capabilities: Router Switch IGMP 
Interface: GigabitEthernet0/1,  Port ID (outgoing port): GigabitEthernet0/1
Holdtime : 163 sec

Version :
Cisco IOS Software, vios_l2 Software (vios_l2-ADVENTERPRISEK9-M), Version 15.2(4.0.55)E, TEST ENGINEERING ESTG_WEEKLY BUILD, synced to  END_OF_FLO_ISP
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2015 by Cisco Systems, Inc.
Compiled Tue 28-Jul-15 18:52 by sasyamal

advertisement version: 2
VTP Management Domain: ''
Native VLAN: 1
Duplex: half
Management address(es): 
  IP address: 172.16.101.2

-------------------------
Device ID: usa1-access-02.home.com
Entry address(es): 
  IP address: 172.16.101.4
Platform: Cisco ,  Capabilities: Router Switch IGMP 
Interface: GigabitEthernet0/3,  Port ID (outgoing port): GigabitEthernet0/2
Holdtime : 153 sec

Version :
Cisco IOS Software, vios_l2 Software (vios_l2-ADVENTERPRISEK9-M), Version 15.2(4.0.55)E, TEST ENGINEERING ESTG_WEEKLY BUILD, synced to  END_OF_FLO_ISP
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2015 by Cisco Systems, Inc.
Compiled Tue 28-Jul-15 18:52 by sasyamal

advertisement version: 2
VTP Management Domain: ''
Native VLAN: 1
Duplex: half
Management address(es): 
  IP address: 172.16.101.4

-------------------------
Device ID: usa1-rtr-1.home.com
Entry address(es): 
  IP address: 172.16.101.100
Platform: Cisco 7206VXR,  Capabilities: Router 
Interface: GigabitEthernet0/0,  Port ID (outgoing port): Ethernet2/0
Holdtime : 130 sec

Version :
Cisco IOS Software, 7200 Software (C7200-ADVENTERPRISEK9-M), Version 15.2(4)M11, RELEASE SOFTWARE (fc2)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2016 by Cisco Systems, Inc.
Compiled Sun 16-Oct-16 07:53 by prod_rel_team

advertisement version: 2
Duplex: half


Total cdp entries displayed : 3
usa1-core-01# """,
    "show_interface_ios": """usa1-core-01#show int g 0/1
GigabitEthernet0/1 is up, line protocol is up (connected) 
  Hardware is iGbE, address is 0cab.0018.0001 (bia 0cab.0018.0001)
  Description: to switch2 e1(g0/1)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Unknown, Unknown, link type is auto, media type is unknown media type
  output flow-control is unsupported, input flow-control is unsupported
  Auto-duplex, Auto-speed, link type is auto, media type is unknown
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:01, output 00:00:02, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/0 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     1111314 packets input, 78239931 bytes, 0 no buffer
     Received 1100689 broadcasts (1100689 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 1100689 multicast, 0 pause input
     516778 packets output, 50339457 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
usa1-core-01# """

}