examples = {
    "IOS Show CDP Neighbor detail":
        {
            "description": "cdp neigh details from IOS",
            "result": [
                [
                    {
                        "capabilities": "Router Switch IGMP",
                        "device_id": "usa1-core-02.home.com",
                        "device_ip": "172.16.101.2",
                        "local_interface": "GigabitEthernet0/1",
                        "platform": "Cisco",
                        "remote_interface": "GigabitEthernet0/1"
                    },
                    {
                        "capabilities": "Router Switch IGMP",
                        "device_id": "usa1-access-02.home.com",
                        "device_ip": "172.16.101.4",
                        "local_interface": "GigabitEthernet0/3",
                        "platform": "Cisco",
                        "remote_interface": "GigabitEthernet0/2"
                    },
                    {
                        "device_id": "usa1-rtr-1.home.com",
                        "device_ip": "172.16.101.100",
                        "local_interface": "GigabitEthernet0/0",
                        "remote_interface": "Ethernet2/0"
                    }
                ]
            ],
            "source_text": "\nusa1-core-01#show cdp neigh detail\n-------------------------\nDevice ID: usa1-core-02.home.com\nEntry address(es): \n  IP address: 172.16.101.2\nPlatform: Cisco ,  Capabilities: Router Switch IGMP \nInterface: GigabitEthernet0/1,  Port ID (outgoing port): GigabitEthernet0/1\nHoldtime : 166 sec\n\nVersion :\nCisco IOS Software, vios_l2 Software (vios_l2-ADVENTERPRISEK9-M), Version 15.2(4.0.55)E, TEST ENGINEERING ESTG_WEEKLY BUILD, synced to  END_OF_FLO_ISP\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2015 by Cisco Systems, Inc.\nCompiled Tue 28-Jul-15 18:52 by sasyamal\n\nadvertisement version: 2\nVTP Management Domain: ''\nNative VLAN: 1\nDuplex: half\nManagement address(es): \n  IP address: 172.16.101.2\n\n-------------------------\nDevice ID: usa1-access-02.home.com\nEntry address(es): \n  IP address: 172.16.101.4\nPlatform: Cisco ,  Capabilities: Router Switch IGMP \nInterface: GigabitEthernet0/3,  Port ID (outgoing port): GigabitEthernet0/2\nHoldtime : 161 sec\n\nVersion :\nCisco IOS Software, vios_l2 Software (vios_l2-ADVENTERPRISEK9-M), Version 15.2(4.0.55)E, TEST ENGINEERING ESTG_WEEKLY BUILD, synced to  END_OF_FLO_ISP\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2015 by Cisco Systems, Inc.\nCompiled Tue 28-Jul-15 18:52 by sasyamal\n\nadvertisement version: 2\nVTP Management Domain: ''\nNative VLAN: 1\nDuplex: half\nManagement address(es): \n  IP address: 172.16.101.4\n\n-------------------------\nDevice ID: usa1-rtr-1.home.com\nEntry address(es): \n  IP address: 172.16.101.100\nPlatform: Cisco 7206VXR,  Capabilities: Router \nInterface: GigabitEthernet0/0,  Port ID (outgoing port): Ethernet2/0\nHoldtime : 148 sec\n\nVersion :\nCisco IOS Software, 7200 Software (C7200-ADVENTERPRISEK9-M), Version 15.2(4)M11, RELEASE SOFTWARE (fc2)\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2016 by Cisco Systems, Inc.\nCompiled Sun 16-Oct-16 07:53 by prod_rel_team\n\nadvertisement version: 2\nDuplex: half\n\n\nTotal cdp entries displayed : 3\nusa1-core-01# ",
            "template": "Device ID: {{ device_id }}\n  IP address: {{ device_ip | default('no ip found') }}\nPlatform: {{ platform | ORPHRASE }} ,  Capabilities: {{ capabilities | ORPHRASE }} \nInterface: {{ local_interface }},  Port ID (outgoing port): {{ remote_interface }}\n",
            "variables": [
                {
                    "end": 94,
                    "filters": [],
                    "functions": [],
                    "start": 73,
                    "var_name": "device_id"
                },
                {
                    "end": 141,
                    "filters": [],
                    "functions": [
                        "default('no ip found')"
                    ],
                    "start": 129,
                    "var_name": "device_ip"
                },
                {
                    "end": 157,
                    "filters": [
                        "ORPHRASE"
                    ],
                    "functions": [],
                    "start": 152,
                    "var_name": "platform"
                },
                {
                    "end": 193,
                    "filters": [
                        "ORPHRASE"
                    ],
                    "functions": [],
                    "start": 175,
                    "var_name": "capabilities"
                },
                {
                    "end": 224,
                    "filters": [],
                    "functions": [],
                    "start": 206,
                    "var_name": "local_interface"
                },
                {
                    "end": 270,
                    "filters": [],
                    "functions": [],
                    "start": 252,
                    "var_name": "remote_interface"
                }
            ]
        },
    "vIOS Show Interface":
{
    "description": "IOS Show Interface vios_l2 virtual switch",
    "result": [
        {
            "bandwidth": "1000000",
            "bia_mac": "0cab.0018.0001",
            "collisions": "0",
            "crc": "0",
            "current_mac": "0c:ab:00:18:00:01",
            "delay": "10",
            "description": "No Description Configured",
            "framing_errors": "0",
            "hardware": "iGbE",
            "ignored": "0",
            "input_pkts_sec": "0 packets/sec",
            "input_rate": "0 bits/sec",
            "input_sampling_rate": "5 minute",
            "inpute_errors": "0",
            "interface_name": "GigabitEthernet0/1",
            "interface_resets": "2",
            "lp_state": "up",
            "mtu": "1500",
            "output_errors": "0",
            "output_pkts_sec": "0 packets/sec",
            "output_rate": "0 bits/sec",
            "output_sampling_rate": "5 minute",
            "overruns": "0",
            "phy_state": "up"
        }
    ],
    "source_text": "usa1-core-01#show int g 0/1\nGigabitEthernet0/1 is up, line protocol is up (connected) \n  Hardware is iGbE, address is 0cab.0018.0001 (bia 0cab.0018.0001)\n  Description: to switch2 e1(g0/1)\n  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, \n     reliability 255/255, txload 1/255, rxload 1/255\n  Encapsulation ARPA, loopback not set\n  Keepalive set (10 sec)\n  Unknown, Unknown, link type is auto, media type is unknown media type\n  output flow-control is unsupported, input flow-control is unsupported\n  Auto-duplex, Auto-speed, link type is auto, media type is unknown\n  input flow-control is off, output flow-control is unsupported \n  ARP type: ARPA, ARP Timeout 04:00:00\n  Last input 00:00:01, output 00:00:02, output hang never\n  Last clearing of \"show interface\" counters never\n  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0\n  Queueing strategy: fifo\n  Output queue: 0/0 (size/max)\n  5 minute input rate 0 bits/sec, 0 packets/sec\n  5 minute output rate 0 bits/sec, 0 packets/sec\n     1111314 packets input, 78239931 bytes, 0 no buffer\n     Received 1100689 broadcasts (1100689 multicasts)\n     0 runts, 0 giants, 0 throttles \n     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored\n     0 watchdog, 1100689 multicast, 0 pause input\n     516778 packets output, 50339457 bytes, 0 underruns\n     0 output errors, 0 collisions, 2 interface resets\n     0 unknown protocol drops\n     0 babbles, 0 late collision, 0 deferred\n     0 lost carrier, 0 no carrier, 0 pause output\n     0 output buffer failures, 0 output buffers swapped out\nusa1-core-01# ",
    "template": "{{ interface_name }} is {{ phy_state | contains_re('(?i)\\b(?:up|down)\\b') }}, line protocol is {{ lp_state | contains_re('(?i)\\b(?:up|down)\\b') }} (connected) \n  Hardware is {{ hardware | ORPHRASE }}, address is {{ current_mac | MAC | mac_eui() }} (bia {{ bia_mac | MAC }})\n  Description: {{ description | default('No Description Configured') }}\n  MTU {{ mtu }} bytes, BW {{ bandwidth }} Kbit/sec, DLY {{ delay }} usec, \n  {{ input_sampling_rate | ORPHRASE }} input rate {{ input_rate | ORPHRASE }}, {{ input_pkts_sec | ORPHRASE }}\n  {{ output_sampling_rate | ORPHRASE }} output rate {{ output_rate | ORPHRASE }}, {{ output_pkts_sec | ORPHRASE }}\n     {{ inpute_errors }} input errors, {{ crc }} CRC, {{ framing_errors }} frame, {{ overruns }} overrun, {{ ignored }} ignored\n     {{ output_errors }} output errors, {{ collisions }} collisions, {{ interface_resets }} interface resets\n",
    "variables": [
        {
            "end": 46,
            "filters": [],
            "functions": [],
            "start": 28,
            "var_name": "interface_name"
        },
        {
            "end": 52,
            "filters": [],
            "functions": [
                "contains_re('(?i)\\b(?:up|down)\\b')"
            ],
            "start": 50,
            "var_name": "phy_state"
        },
        {
            "end": 73,
            "filters": [],
            "functions": [
                "contains_re('(?i)\\b(?:up|down)\\b')"
            ],
            "start": 71,
            "var_name": "lp_state"
        },
        {
            "end": 105,
            "filters": [
                "ORPHRASE"
            ],
            "functions": [],
            "start": 101,
            "var_name": "hardware"
        },
        {
            "end": 132,
            "filters": [
                "MAC"
            ],
            "functions": [
                "mac_eui()"
            ],
            "start": 118,
            "var_name": "current_mac"
        },
        {
            "end": 152,
            "filters": [
                "MAC"
            ],
            "functions": [],
            "start": 138,
            "var_name": "bia_mac"
        },
        {
            "end": 188,
            "filters": [],
            "functions": [
                "default('No Description Configured')"
            ],
            "start": 169,
            "var_name": "description"
        },
        {
            "end": 199,
            "filters": [],
            "functions": [],
            "start": 195,
            "var_name": "mtu"
        },
        {
            "end": 217,
            "filters": [],
            "functions": [],
            "start": 210,
            "var_name": "bandwidth"
        },
        {
            "end": 234,
            "filters": [],
            "functions": [],
            "start": 232,
            "var_name": "delay"
        },
        {
            "end": 923,
            "filters": [
                "ORPHRASE"
            ],
            "functions": [],
            "start": 915,
            "var_name": "input_sampling_rate"
        },
        {
            "end": 971,
            "filters": [
                "ORPHRASE"
            ],
            "functions": [],
            "start": 963,
            "var_name": "output_sampling_rate"
        },
        {
            "end": 1163,
            "filters": [],
            "functions": [],
            "start": 1162,
            "var_name": "inpute_errors"
        },
        {
            "end": 1179,
            "filters": [],
            "functions": [],
            "start": 1178,
            "var_name": "crc"
        },
        {
            "end": 945,
            "filters": [
                "ORPHRASE"
            ],
            "functions": [],
            "start": 935,
            "var_name": "input_rate"
        },
        {
            "end": 960,
            "filters": [
                "ORPHRASE"
            ],
            "functions": [],
            "start": 947,
            "var_name": "input_pkts_sec"
        },
        {
            "end": 994,
            "filters": [
                "ORPHRASE"
            ],
            "functions": [],
            "start": 984,
            "var_name": "output_rate"
        },
        {
            "end": 1009,
            "filters": [
                "ORPHRASE"
            ],
            "functions": [],
            "start": 996,
            "var_name": "output_pkts_sec"
        },
        {
            "end": 1186,
            "filters": [],
            "functions": [],
            "start": 1185,
            "var_name": "framing_errors"
        },
        {
            "end": 1195,
            "filters": [],
            "functions": [],
            "start": 1194,
            "var_name": "overruns"
        },
        {
            "end": 1206,
            "filters": [],
            "functions": [],
            "start": 1205,
            "var_name": "ignored"
        },
        {
            "end": 1327,
            "filters": [],
            "functions": [],
            "start": 1326,
            "var_name": "output_errors"
        },
        {
            "end": 1344,
            "filters": [],
            "functions": [],
            "start": 1343,
            "var_name": "collisions"
        },
        {
            "end": 1358,
            "filters": [],
            "functions": [],
            "start": 1357,
            "var_name": "interface_resets"
        }
    ]
    },
    "IOS Show Mac Address-Table":
{
    "description": "mac address table from IOS",
    "result": [
        [
            {
                "capabilities": "Router Switch IGMP",
                "device_id": "usa1-core-02.home.com",
                "device_ip": "172.16.101.2",
                "holdtime": 166,
                "local_interface": "GigabitEthernet0/1",
                "platform": "Cisco",
                "remote_interface": "GigabitEthernet0/1"
            },
            {
                "capabilities": "Router Switch IGMP",
                "device_id": "usa1-access-02.home.com",
                "device_ip": "172.16.101.4",
                "holdtime": 161,
                "local_interface": "GigabitEthernet0/3",
                "platform": "Cisco",
                "remote_interface": "GigabitEthernet0/2"
            },
            {
                "device_id": "usa1-rtr-1.home.com",
                "device_ip": "172.16.101.100",
                "holdtime": 148,
                "local_interface": "GigabitEthernet0/0",
                "remote_interface": "Ethernet2/0"
            }
        ]
    ],
    "source_text": "\nusa1-core-01#show cdp neigh detail\n-------------------------\nDevice ID: usa1-core-02.home.com\nEntry address(es): \n  IP address: 172.16.101.2\nPlatform: Cisco ,  Capabilities: Router Switch IGMP \nInterface: GigabitEthernet0/1,  Port ID (outgoing port): GigabitEthernet0/1\nHoldtime : 166 sec\n\nVersion :\nCisco IOS Software, vios_l2 Software (vios_l2-ADVENTERPRISEK9-M), Version 15.2(4.0.55)E, TEST ENGINEERING ESTG_WEEKLY BUILD, synced to  END_OF_FLO_ISP\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2015 by Cisco Systems, Inc.\nCompiled Tue 28-Jul-15 18:52 by sasyamal\n\nadvertisement version: 2\nVTP Management Domain: ''\nNative VLAN: 1\nDuplex: half\nManagement address(es): \n  IP address: 172.16.101.2\n\n-------------------------\nDevice ID: usa1-access-02.home.com\nEntry address(es): \n  IP address: 172.16.101.4\nPlatform: Cisco ,  Capabilities: Router Switch IGMP \nInterface: GigabitEthernet0/3,  Port ID (outgoing port): GigabitEthernet0/2\nHoldtime : 161 sec\n\nVersion :\nCisco IOS Software, vios_l2 Software (vios_l2-ADVENTERPRISEK9-M), Version 15.2(4.0.55)E, TEST ENGINEERING ESTG_WEEKLY BUILD, synced to  END_OF_FLO_ISP\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2015 by Cisco Systems, Inc.\nCompiled Tue 28-Jul-15 18:52 by sasyamal\n\nadvertisement version: 2\nVTP Management Domain: ''\nNative VLAN: 1\nDuplex: half\nManagement address(es): \n  IP address: 172.16.101.4\n\n-------------------------\nDevice ID: usa1-rtr-1.home.com\nEntry address(es): \n  IP address: 172.16.101.100\nPlatform: Cisco 7206VXR,  Capabilities: Router \nInterface: GigabitEthernet0/0,  Port ID (outgoing port): Ethernet2/0\nHoldtime : 148 sec\n\nVersion :\nCisco IOS Software, 7200 Software (C7200-ADVENTERPRISEK9-M), Version 15.2(4)M11, RELEASE SOFTWARE (fc2)\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2016 by Cisco Systems, Inc.\nCompiled Sun 16-Oct-16 07:53 by prod_rel_team\n\nadvertisement version: 2\nDuplex: half\n\n\nTotal cdp entries displayed : 3\nusa1-core-01# ",
    "template": "Device ID: {{ device_id }}\n  IP address: {{ device_ip | default('no ip found') }}\nPlatform: {{ platform | ORPHRASE }} ,  Capabilities: {{ capabilities | ORPHRASE }} \nInterface: {{ local_interface }},  Port ID (outgoing port): {{ remote_interface }}\nHoldtime : {{ holdtime | WORD | to_int() | to_float() }} sec\n",
    "variables": [
        {
            "end": 94,
            "filters": [],
            "functions": [],
            "start": 73,
            "var_name": "device_id"
        },
        {
            "end": 141,
            "filters": [],
            "functions": [
                "default('no ip found')"
            ],
            "start": 129,
            "var_name": "device_ip"
        },
        {
            "end": 157,
            "filters": [
                "ORPHRASE"
            ],
            "functions": [],
            "start": 152,
            "var_name": "platform"
        },
        {
            "end": 193,
            "filters": [
                "ORPHRASE"
            ],
            "functions": [],
            "start": 175,
            "var_name": "capabilities"
        },
        {
            "end": 224,
            "filters": [],
            "functions": [],
            "start": 206,
            "var_name": "local_interface"
        },
        {
            "end": 270,
            "filters": [],
            "functions": [],
            "start": 252,
            "var_name": "remote_interface"
        },
        {
            "end": 285,
            "filters": [
                "WORD"
            ],
            "functions": [
                "to_int() | to_float()"
            ],
            "start": 282,
            "var_name": "holdtime"
        }
    ]
 },
    "Netstat Linux":
{
    "description": "netstat -ln from ubuntu",
    "result": [
        [
            {
                "listening_port": "631",
                "listing_ip": "127.0.0.1",
                "recv_q": "0",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            },
            {
                "listening_port": "33125",
                "listing_ip": "127.0.0.1",
                "recv_q": "0",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            },
            {
                "listening_port": "33027",
                "listing_ip": "127.0.0.1",
                "recv_q": "0",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            },
            {
                "listening_port": "34269",
                "listing_ip": "127.0.0.1",
                "recv_q": "0",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            },
            {
                "listening_port": "35589",
                "listing_ip": "127.0.0.1",
                "recv_q": "0",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            },
            {
                "listening_port": "35639",
                "listing_ip": "127.0.0.1",
                "recv_q": "0",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            },
            {
                "listening_port": "35213",
                "listing_ip": "127.0.0.1",
                "recv_q": "0",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            },
            {
                "listening_port": "53",
                "listing_ip": "192.168.122.1",
                "recv_q": "0",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            },
            {
                "listening_port": "36761",
                "listing_ip": "127.0.0.1",
                "recv_q": "0",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            },
            {
                "listening_port": "3080",
                "listing_ip": "127.0.0.1",
                "recv_q": "0",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            },
            {
                "listening_port": "5023",
                "listing_ip": "127.0.0.1",
                "recv_q": "0",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            },
            {
                "listening_port": "5021",
                "listing_ip": "127.0.0.1",
                "recv_q": "0",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            },
            {
                "listening_port": "5011",
                "listing_ip": "127.0.0.1",
                "recv_q": "0",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            },
            {
                "listening_port": "5010",
                "listing_ip": "127.0.0.1",
                "recv_q": "1",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            },
            {
                "listening_port": "5009",
                "listing_ip": "127.0.0.1",
                "recv_q": "0",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            },
            {
                "listening_port": "5008",
                "listing_ip": "127.0.0.1",
                "recv_q": "0",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            },
            {
                "listening_port": "5007",
                "listing_ip": "127.0.0.1",
                "recv_q": "0",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            },
            {
                "listening_port": "5006",
                "listing_ip": "127.0.0.1",
                "recv_q": "0",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            },
            {
                "listening_port": "5005",
                "listing_ip": "127.0.0.1",
                "recv_q": "0",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            },
            {
                "listening_port": "5004",
                "listing_ip": "127.0.0.1",
                "recv_q": "0",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            },
            {
                "listening_port": "5003",
                "listing_ip": "127.0.0.1",
                "recv_q": "0",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            },
            {
                "listening_port": "5002",
                "listing_ip": "127.0.0.1",
                "recv_q": "0",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            },
            {
                "listening_port": "5001",
                "listing_ip": "127.0.0.1",
                "recv_q": "1",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            },
            {
                "listening_port": "5030",
                "listing_ip": "127.0.0.1",
                "recv_q": "0",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            },
            {
                "listening_port": "5026",
                "listing_ip": "127.0.0.1",
                "recv_q": "0",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            },
            {
                "listening_port": "5024",
                "listing_ip": "127.0.0.1",
                "recv_q": "0",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            },
            {
                "listening_port": "37063",
                "listing_ip": "127.0.0.1",
                "recv_q": "0",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            },
            {
                "listening_port": "37041",
                "listing_ip": "127.0.0.1",
                "recv_q": "0",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            },
            {
                "listening_port": "38587",
                "listing_ip": "127.0.0.1",
                "recv_q": "0",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            },
            {
                "listening_port": "54629",
                "listing_ip": "127.0.0.1",
                "recv_q": "0",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            },
            {
                "listening_port": "5432",
                "listing_ip": "127.0.0.1",
                "recv_q": "0",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            },
            {
                "listening_port": "6379",
                "listing_ip": "127.0.0.1",
                "recv_q": "0",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            },
            {
                "listening_port": "39013",
                "listing_ip": "127.0.0.1",
                "recv_q": "0",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            },
            {
                "listening_port": "40823",
                "listing_ip": "127.0.0.1",
                "recv_q": "0",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            },
            {
                "listening_port": "53",
                "listing_ip": "127.0.0.53",
                "recv_q": "0",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            },
            {
                "listening_port": "42145",
                "listing_ip": "127.0.0.1",
                "recv_q": "0",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            },
            {
                "listening_port": "43895",
                "listing_ip": "127.0.0.1",
                "recv_q": "0",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            },
            {
                "listening_port": "44795",
                "listing_ip": "127.0.0.1",
                "recv_q": "0",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            },
            {
                "listening_port": "44793",
                "listing_ip": "127.0.0.1",
                "recv_q": "0",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            },
            {
                "listening_port": "902",
                "listing_ip": "0.0.0.0",
                "recv_q": "0",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            },
            {
                "listening_port": "44045",
                "listing_ip": "127.0.0.1",
                "recv_q": "0",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            },
            {
                "listening_port": "22",
                "listing_ip": "0.0.0.0",
                "recv_q": "0",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            },
            {
                "listening_port": "60451",
                "listing_ip": "127.0.0.1",
                "recv_q": "0",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            },
            {
                "listening_port": "389",
                "listing_ip": "0.0.0.0",
                "recv_q": "0",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            },
            {
                "listening_port": "8000",
                "listing_ip": "0.0.0.0",
                "recv_q": "0",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            },
            {
                "listening_port": "46845",
                "listing_ip": "127.0.0.1",
                "recv_q": "0",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            },
            {
                "listening_port": "5433",
                "listing_ip": "0.0.0.0",
                "recv_q": "0",
                "remote_ip": "0.0.0.0",
                "remote_port": "*",
                "send_q": "0",
                "state": "LISTEN"
            }
        ]
    ],
    "source_text": "speterman@ThinkStation:~$ netstat -ln\nActive Internet connections (only servers)\nProto Recv-Q Send-Q Local Address           Foreign Address         State\ntcp        0      0 127.0.0.1:631           0.0.0.0:*               LISTEN\ntcp        0      0 127.0.0.1:33125         0.0.0.0:*               LISTEN\ntcp        0      0 127.0.0.1:33027         0.0.0.0:*               LISTEN\ntcp        0      0 127.0.0.1:34269         0.0.0.0:*               LISTEN\ntcp        0      0 127.0.0.1:35589         0.0.0.0:*               LISTEN\ntcp        0      0 127.0.0.1:35639         0.0.0.0:*               LISTEN\ntcp        0      0 127.0.0.1:35213         0.0.0.0:*               LISTEN\ntcp        0      0 192.168.122.1:53        0.0.0.0:*               LISTEN\ntcp        0      0 127.0.0.1:36761         0.0.0.0:*               LISTEN\ntcp        0      0 127.0.0.1:3080          0.0.0.0:*               LISTEN\ntcp        0      0 127.0.0.1:5023          0.0.0.0:*               LISTEN\ntcp        0      0 127.0.0.1:5021          0.0.0.0:*               LISTEN\ntcp        0      0 127.0.0.1:5011          0.0.0.0:*               LISTEN\ntcp        1      0 127.0.0.1:5010          0.0.0.0:*               LISTEN\ntcp        0      0 127.0.0.1:5009          0.0.0.0:*               LISTEN\ntcp        0      0 127.0.0.1:5008          0.0.0.0:*               LISTEN\ntcp        0      0 127.0.0.1:5007          0.0.0.0:*               LISTEN\ntcp        0      0 127.0.0.1:5006          0.0.0.0:*               LISTEN\ntcp        0      0 127.0.0.1:5005          0.0.0.0:*               LISTEN\ntcp        0      0 127.0.0.1:5004          0.0.0.0:*               LISTEN\ntcp        0      0 127.0.0.1:5003          0.0.0.0:*               LISTEN\ntcp        0      0 127.0.0.1:5002          0.0.0.0:*               LISTEN\ntcp        1      0 127.0.0.1:5001          0.0.0.0:*               LISTEN\ntcp        0      0 127.0.0.1:5030          0.0.0.0:*               LISTEN\ntcp        0      0 127.0.0.1:5026          0.0.0.0:*               LISTEN\ntcp        0      0 127.0.0.1:5024          0.0.0.0:*               LISTEN\ntcp        0      0 127.0.0.1:37063         0.0.0.0:*               LISTEN\ntcp        0      0 127.0.0.1:37041         0.0.0.0:*               LISTEN\ntcp        0      0 127.0.0.1:38587         0.0.0.0:*               LISTEN\ntcp        0      0 127.0.0.1:54629         0.0.0.0:*               LISTEN\ntcp        0      0 127.0.0.1:5432          0.0.0.0:*               LISTEN\ntcp        0      0 127.0.0.1:6379          0.0.0.0:*               LISTEN\ntcp        0      0 127.0.0.1:39013         0.0.0.0:*               LISTEN\ntcp        0      0 127.0.0.1:40823         0.0.0.0:*               LISTEN\ntcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN\ntcp        0      0 127.0.0.1:42145         0.0.0.0:*               LISTEN\ntcp        0      0 127.0.0.1:43895         0.0.0.0:*               LISTEN\ntcp        0      0 127.0.0.1:44795         0.0.0.0:*               LISTEN\ntcp        0      0 127.0.0.1:44793         0.0.0.0:*               LISTEN\ntcp        0      0 0.0.0.0:902             0.0.0.0:*               LISTEN\ntcp        0      0 127.0.0.1:44045         0.0.0.0:*               LISTEN\ntcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN\ntcp        0      0 127.0.0.1:60451         0.0.0.0:*               LISTEN\ntcp        0      0 0.0.0.0:389             0.0.0.0:*               LISTEN\ntcp        0      0 0.0.0.0:8000            0.0.0.0:*               LISTEN\ntcp        0      0 127.0.0.1:46845         0.0.0.0:*               LISTEN\ntcp        0      0 0.0.0.0:5433            0.0.0.0:*               LISTEN",
    "template": "tcp        {{ recv_q }}      {{ send_q }} {{ listing_ip }}:{{ listening_port }}           {{ remote_ip }}:{{ remote_port }}               {{ state }}\n",
    "variables": [
        {
            "end": 167,
            "filters": [],
            "functions": [],
            "start": 166,
            "var_name": "recv_q"
        },
        {
            "end": 174,
            "filters": [],
            "functions": [],
            "start": 173,
            "var_name": "send_q"
        },
        {
            "end": 184,
            "filters": [],
            "functions": [],
            "start": 175,
            "var_name": "listing_ip"
        },
        {
            "end": 188,
            "filters": [],
            "functions": [],
            "start": 185,
            "var_name": "listening_port"
        },
        {
            "end": 206,
            "filters": [],
            "functions": [],
            "start": 199,
            "var_name": "remote_ip"
        },
        {
            "end": 208,
            "filters": [],
            "functions": [],
            "start": 207,
            "var_name": "remote_port"
        },
        {
            "end": 229,
            "filters": [],
            "functions": [],
            "start": 223,
            "var_name": "state"
        }
    ]
}
}
