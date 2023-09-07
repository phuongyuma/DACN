## Add flow for topo_ring_3h.py

import requests




s1_flow1 = {
    "dpid": 1,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 100,
    "match":{
        #"dl_dst":"00:00:00:00:00:01"
        "ipv4_dst":"192.168.1.1"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 3
        }
    ]
}


s1_flow2 = {
    "dpid": 1,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 100,
    "match":{
        "in_port":2
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 1
        }
    ]
}

s1_flow3 = {
    "dpid": 1,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 100,
    "match":{
        "in_port":1
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port":2
        }
    ]
}
s1_flow4 = {
    "dpid": 1,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 100,
    "match":{
        "in_port":3
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port":2
        }
    ]
}

s2_flow1 = {
    "dpid": 2,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 100,
    "match":{
        #"dl_dst":"00:00:00:00:00:02"
        "ipv4_dst":"192.168.1.2"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 3
        }
    ]
}

  
s2_flow2 = {
    "dpid": 2,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 100,
    "match":{
        "in_port":1
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 2
        }
    ]
}
s2_flow3 = {
    "dpid":2,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 100,
    "match":{
        "in_port":2
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 1
        }
    ]
}
s2_flow4 = {
    "dpid": 2,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 100,
    "match":{
        "in_port":3
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port":2
        }
    ]
}

s3_flow1 = {
    "dpid": 3,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 100,
    "match":{
        #"dl_dst":"00:00:00:00:00:03"
        "ipv4_dst":"192.168.1.3"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 3
        }
    ]
}


s3_flow2 = {
    "dpid": 3,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 100,
    "match":{
        "in_port":2
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 1
        }
    ]
}
s3_flow3 = {
    "dpid": 3,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 100,
    "match":{
        "in_port":1
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 2
        }
    ]
}
s3_flow4 = {
    "dpid": 3,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 100,
    "match":{
        "in_port":3
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port":2
        }
    ]
}



url = "http://localhost:8080/stats/flowentry/add"  # Replace with the appropriate URL

## list of all flows
list_flow = [s1_flow1, s1_flow2, s1_flow3, s2_flow1, s2_flow2, s2_flow3, s3_flow1, s3_flow2, s3_flow3, s1_flow4, s2_flow4, s3_flow4]
for flow in list_flow:
    flow_data = flow
    response = requests.post(url, json=flow_data)
    if response.status_code == 200:
        print("Flow added successfully!")
    else:
        print("Failed to add flow", flow_data, ". Status code:", response.status_code)

# response = requests.post(url, json=flow_data)
# if response.status_code == 200:
#     print("Flow added successfully!")
# else:
#     print("Failed to add flow. Status code:", response.status_code)

