import json
json_str = '''

{
    "response_code":200,
    "param_entity":[
        {
            "target_lable":"螺母",
            "target_pose":"(x,y,z)",
            "target_angle":"θ"
        },
        {
            "target_lable":"螺栓",
            "target_pose":"(x,y,z)",
            "target_angle":"θ"
        }
    ]
}

'''
# 打印字符串 str
print(type(json_str))

# 打印转换好的dict ; str-->dict
data = json.loads(json_str)
print("json.loads(json_str) type is " +  str(type(data)))
print("data:"+ str(data))

# param_entity is list
print(data.get('response_code'))
param_entity = data.get('param_entity')
print(type(param_entity))

# param_entity[0] is dict
print("param_entity集合的长度：" + str(len(param_entity)))
print(param_entity[0])
print(type(param_entity[0]))
print(param_entity[0].get("target_lable"))

# 遍历集合
for entity_list in param_entity:
    print(entity_list.get("target_lable"))

# 封装执行序列
