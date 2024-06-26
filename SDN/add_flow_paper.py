## Add flow for topo_ring_3h.py

import requests




s1_flow1 = {
    "dpid": 1,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 100,
    "match":{
        "dl_dst":"00:00:00:00:00:01"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 5
        }
    ]
}

s1_flow2 = {
    "dpid": 1,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 90,
    "match":{
        "dl_dst":"00:00:00:00:00:02"
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
    "priority": 90,
    "match":{
        "dl_dst":"00:00:00:00:00:03"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port":2
        }
    ]
}
s1_flow3_2 = {
    "dpid": 1,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 90,
    "match":{
        "dl_dst":"00:00:00:00:00:04"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port":2
        }
    ]
}
s1_flow3_3 = {
    "dpid": 1,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 90,
    "match":{
        "dl_dst":"00:00:00:00:00:05"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port":2
        }
    ]
}
s1_flow3_4 = {
    "dpid": 1,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 90,
    "match":{
        "dl_dst":"00:00:00:00:00:06"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port":2
        }
    ]
}
s1_flow_s7 = {
    "dpid": 1,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 90,
    "match":{
        "dl_dst":"00:00:00:00:00:07"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port":3
        }
    ]
}
s1_flow_s7_2 = {
    "dpid": 1,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 0,
    "match":{
        "in_port":3
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port":6
        }
    ]
}
s1_flow_s8 = {
    "dpid": 1,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 90,
    "match":{
        "dl_dst":"00:00:00:00:00:08"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port":4
        }
    ]
}
s1_flow_s8_2 = {
    "dpid": 1,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 0,
    "match":{
        "in_port":4
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port":6
        }
    ]
}
s1_flow_i = {
    "dpid": 1,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 0,
    "match":{
        "in_port":1
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port":6
        }
    ]
}

s1_flow_i2 = {
    "dpid": 1,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 0,
    "match":{
        "in_port":2
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port":6
        }
    ]
}
s1_flow_i3 = {
    "dpid": 1,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 0,
    "match":{
        "in_port":5
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port":6
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
        "dl_dst":"00:00:00:00:00:02"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 5
        }
    ]
}


  
s2_flow2 = {
    "dpid": 2,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 90,
    "match":{
        "dl_dst":"00:00:00:00:00:01"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 1
        }
    ]
}
s2_flow2_2 = {
    "dpid": 2,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 90,
    "match":{
        "dl_dst":"00:00:00:00:00:03"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 2
        }
    ]
}
s2_flow2_3 = {
    "dpid": 2,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 90,
    "match":{
        "dl_dst":"00:00:00:00:00:04"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 2
        }
    ]
}
s2_flow2_4 = {
    "dpid": 2,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 90,
    "match":{
        "dl_dst":"00:00:00:00:00:05"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 2
        }
    ]
}
s2_flow2_5 = {
    "dpid": 2,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 90,
    "match":{
        "dl_dst":"00:00:00:00:00:06"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 2
        }
    ]
}

s2_flow_i = {
    "dpid": 2,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 0,
    "match":{
        "dl_src":"00:00:00:00:00:02"
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
        "dl_dst":"00:00:00:00:00:03"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 5
        }
    ]
}


s3_flow2 = {
    "dpid": 3,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 90,
    "match":{
        "dl_dst":"00:00:00:00:00:01"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 1
        }
    ]
}
s3_flow2_2 = {
    "dpid": 3,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 90,
    "match":{
        "dl_dst":"00:00:00:00:00:04"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 3
        }
    ]
}
s3_flow2_3 = {
    "dpid": 3,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 90,
    "match":{
        "dl_dst":"00:00:00:00:00:05"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 4
        }
    ]
}
s3_flow2_4 = {
    "dpid": 3,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 90,
    "match":{
        "dl_dst":"00:00:00:00:00:6"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 4
        }
    ]
}
s3_flow3 = {
    "dpid": 3,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 90,
    "match":{
        "dl_dst":"00:00:00:00:00:02"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 2
        }
    ]
}
s3_flow_i = {
    "dpid": 3,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 0,
    "match":{
        "dl_src":"00:00:00:00:00:03"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 1
        }
    ]
}
s3_flow_i2 = {
    "dpid": 3,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 0,
    "match":{
        "dl_src":"00:00:00:00:00:04"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 1
        }
    ]
}
s3_flow_i3 = {
    "dpid": 3,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 0,
    "match":{
        "dl_src":"00:00:00:00:00:05"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 1
        }
    ]
}
s3_flow_i4 = {
    "dpid": 3,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 0,
    "match":{
        "dl_src":"00:00:00:00:00:06"
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
        "dl_dst":"00:00:00:00:00:04"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 5
        }
    ]
}

s4_flow2 = {
    "dpid": 4,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 90,
    "match":{
        "dl_dst":"00:00:00:00:00:05"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 2
        }
    ]
}
s4_flow2_2 = {
    "dpid": 4,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 90,
    "match":{
        "dl_dst":"00:00:00:00:00:06"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 3
        }
    ]
}


s4_flow3 = {
    "dpid": 4,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 90,
    "match":{
        "dl_dst":"00:00:00:00:00:01"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port":1
        }
    ]
}
s4_flow3_2 = {
    "dpid": 4,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 90,
    "match":{
        "dl_dst":"00:00:00:00:00:02"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port":1
        }
    ]
}
s4_flow3_3 = {
    "dpid": 4,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 90,
    "match":{
        "dl_dst":"00:00:00:00:00:03"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port":1
        }
    ]
}
s4_flow_i = {
    "dpid": 4,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 0,
    "match":{
        "dl_src":"00:00:00:00:00:04"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port":1
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
        "dl_dst":"00:00:00:00:00:05"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 5
        }
    ]
}
s5_flow2 = {
    "dpid": 5,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 90,
    "match":{
        "dl_dst":"00:00:00:00:00:06"
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
    "priority": 90,
    "match":{
        "dl_dst":"00:00:00:00:00:01"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 1
        }
    ]
}
s5_flow3_2 = {
    "dpid": 5,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 90,
    "match":{
        "dl_dst":"00:00:00:00:00:02"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 1
        }
    ]
}
s5_flow3_3 = {
    "dpid": 5,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 90,
    "match":{
        "dl_dst":"00:00:00:00:00:03"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 1
        }
    ]
}
s5_flow4 = {
    "dpid": 5,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 90,
    "match":{
        "dl_dst":"00:00:00:00:00:04"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 2
        }
    ]
}
s5_flow5 = {
    "dpid": 5,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 90,
    "match":{
        "dl_dst":"00:00:00:00:00:06"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 3
        }
    ]
}
s5_flow_i = {
    "dpid": 5,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 0,
    "match":{
        "dl_src":"00:00:00:00:00:05"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port":1
        }
    ]
}
s5_flow_i2 = {
    "dpid": 5,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 0,
    "match":{
        "dl_src":"00:00:00:00:00:06"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port":1
        }
    ]
}
s6_flow1 = {
    "dpid": 6,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 100,
    "match":{
        "dl_dst":"00:00:00:00:00:06"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 5
        }
    ]
}


s6_flow2 = {
    "dpid": 6,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 90,
    "match":{
        "dl_dst":"00:00:00:00:00:01"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 2
        }
    ]
}
s6_flow2_2 = {
    "dpid": 6,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 90,
    "match":{
        "dl_dst":"00:00:00:00:00:02"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 2
        }
    ]
}
s6_flow2_3 = {
    "dpid": 6,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 90,
    "match":{
        "dl_dst":"00:00:00:00:00:03"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 2
        }
    ]
}
s6_flow2_4 = {
    "dpid": 6,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 90,
    "match":{
        "dl_dst":"00:00:00:00:00:04"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 1
        }
    ]
}
s6_flow2_5 = {
    "dpid": 6,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 90,
    "match":{
        "dl_dst":"00:00:00:00:00:05"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 2
        }
    ]
}
s6_flow_i = {
    "dpid": 6,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 0,
    "match":{
        "dl_src":"00:00:00:00:00:06"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port":2
        }
    ]
}

s7_flow1 = {
    "dpid": 7,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 100,
    "match":{
        "dl_dst":"00:00:00:00:00:07"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 5
        }
    ]
}
s7_flow2 = {
    "dpid": 7,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 100,
    "match":{
        "dl_src":"00:00:00:00:00:07"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 2
        }
    ]
}
s7_flow_i = {
    "dpid": 7,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 0,
    "match":{
        "dl_src":"00:00:00:00:00:07"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port":3
        }
    ]
}
s8_flow1 = {
    "dpid": 8,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 100,
    "match":{
        "dl_dst":"00:00:00:00:00:08"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 5
        }
    ]
}
s8_flow2 = {
    "dpid": 8,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 100,
    "match":{
        "dl_src":"00:00:00:00:00:08"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 2
        }
    ]
}
s8_flow_i = {
    "dpid": 8,
    "table_id": 0,
    "idle_timeout": 0,
    "hard_timeout": 0,
    "priority": 0,
    "match":{
        "dl_src":"00:00:00:00:00:08"
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port":4
        }
    ]
}



url = "http://localhost:8080/stats/flowentry/add"  # Replace with the appropriate URL

## list of all flows
list_flow = [s1_flow1, s1_flow2, s1_flow3, s1_flow3_2, s1_flow3_3, 
             s1_flow3_4, s2_flow1, s2_flow2, s2_flow2_2, s2_flow2_3, 
             s2_flow2_4, s2_flow2_5, s3_flow1, s3_flow2, s3_flow2_2, 
             s3_flow2_3, s3_flow2_4, s3_flow3, s4_flow1, s4_flow2, 
             s4_flow2_2, s4_flow3, s4_flow3_2, s4_flow3_3, s5_flow1, 
             s5_flow2, s5_flow3, s5_flow3_2, s5_flow3_3, s5_flow4, 
             s5_flow5, s6_flow1, s6_flow2, s6_flow2_2, s6_flow2_3, s6_flow2_4, s6_flow2_5,
                s1_flow_i, s1_flow_i2, s1_flow_i3, s2_flow_i, s3_flow_i, s3_flow_i2, s3_flow_i3, s3_flow_i4,
                s4_flow_i, s5_flow_i, s5_flow_i2, s6_flow_i, s7_flow1, s7_flow2, s7_flow_i, s8_flow1, s8_flow2, s8_flow_i, s1_flow_s7, s1_flow_s7_2, s1_flow_s8, s1_flow_s8_2]
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
