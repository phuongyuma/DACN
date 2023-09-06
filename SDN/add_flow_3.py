## Add flow for topo_ring_3h.py

import requests

## add table
s1_group50 = {
    "dpid": 1,
    "type": "SELECT",
    "group_id": 50,
    "buckets": [
        {
            "weight": 50,
            "actions": [
                {
                    "type": "OUTPUT",
                    "port": 1
                }
            ]
        },
        {
            "weight": 50,
             "actions": [
                {
                    "type": "OUTPUT",
                    "port": 2
                }
            ]
        }
    ]
}

s3_group53 = {
    "dpid": 2,
    "type": "SELECT",
    "group_id": 51,
    "buckets": [
        {
            "weight": 50,
            "actions": [
                {
                    "type": "OUTPUT",
                    "port": 1
                }
            ]
        },
        {
            "weight": 50,
             "actions": [
                {
                    "type": "OUTPUT",
                    "port": 2
                }
            ]
        }
    ]
}


list_group = [s1_group50, s5_group51]
for group in list_group:
    group_data = group
    response = requests.post("http://localhost:8080/stats/groupentry/add", json=group_data)
    if response.status_code == 200:
        print("Group added successfully!")
    else:
        print("Failed to add group", group_data, ". Status code:", response.status_code)


s1_flow1 = {
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
            "port": 3
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
        "in_port":3
    },
    "actions":[
        {
            "type":"GROUP",
            "group_id": 50
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
        "in_port":1
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 2
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
        "in_port":2
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 1
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
        "in_port":1
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 2
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



s4_flow1 = {
    "dpid": 4,
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

s4_flow2 = {
    "dpid": 4,
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


s5_flow1 = {
    "dpid": 5,
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
            "port": 3
        }
    ]
}

s5_flow2 = {
    "dpid": 5,
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
            "port": 3
        }
    ]
}

s5_flow3 = {
    "dpid": 5,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 100,
    "match":{
        "in_port":3
    },
    "actions":[
        {
            "type":"GROUP",
            "group_id": 51
        }
    ]
}



url = "http://localhost:8080/stats/flowentry/add"  # Replace with the appropriate URL

## list of all flows
list_flow = [s1_flow1, s1_flow2, s1_flow3, s2_flow1, s2_flow2, s3_flow1, s3_flow2, s4_flow1, s4_flow2, s5_flow1, s5_flow2, s5_flow3]
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

