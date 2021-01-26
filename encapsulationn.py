import json
'''

{
    "response_code":200,
    "data":{
        "sequences":[
            {
                "skills":"抓取",
                "primitives":"趋",
                "target_lable":"螺母",
                "target_pose":"(x,y,z)",
                "target_angle":"θ"
            },
            {
                "skills":"抓取",
                "primitives":"抓",
                "target_lable":"螺母",
                "target_pose":"(x,y,z)",
                "target_angle":"θ"
            },
            {
                "skills":"抓取",
                "primitives":"提",
                "target_lable":"螺母",
                "target_pose":"(x,y,z)",
                "target_angle":"θ"
            },
            {
                "skills":"对准",
                "primitives":"移",
                "target_lable":"螺栓",
                "target_pose":"(x,y,z)",
                "target_angle":"θ"
            },
            {
                "skills":"插入",
                "primitives":"放",
                "target_lable":"螺母",
                "target_pose":"(x,y,z)",
                "target_angle":"θ"
            },
            {
                "skills":"init",
                "primitives":"回",
                "target_lable":"",
                "target_pose":"(x,y,z)",
                "target_angle":"θ"
            }
        ]
    }
}

'''
sequences_data_encapsulate = {}
# response code
sequences_data_encapsulate["response_code"] = "200"
# 统计sequences 的长度
a = {"skills":"init","primitives":"回","target_lable":"","target_pose":"(x,y,z)","target_angle":"θ"}
b = {"skills":"init","primitives":"回","target_lable":"","target_pose":"(x,y,z)","target_angle":"θ"}

sequences = [a,b]
sequences_data_encapsulate["count"] = len(sequences)

# 封装sequences
sequences_data_encapsulate["data"] = {"sequences":sequences}





sequences_data_encapsulate_json = json.dumps(sequences_data_encapsulate,ensure_ascii=False)

print(sequences_data_encapsulate)
print(sequences_data_encapsulate_json)

