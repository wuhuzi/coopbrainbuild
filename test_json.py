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
# 接收实体位姿封装值
def get_entity_param():

    # 打印转换好的dict ; str-->dict
    data = json.loads(json_str)
    # param_entity is list
    param_entity = data.get('param_entity')
    return param_entity



# 封装执行序列
def encapsulate_sequences():
    # 获取带有封装参数的实体
    param_entity = get_entity_param()
    print(param_entity)
    # 开始封装执行序列
    sequences_data_encapsulate = {}
    # 封装 response code
    sequences_data_encapsulate["response_code"] = "200"

    '''
    封装sequences
        1. 动作基元获取
        2. 动作基元参数封装
        3. 封装sequences
    '''
    # 1. 动作基元获取 assume primitives is lists name:primitives_list
    primitives_list = ["趋", "抓", "提", "移", "放", "回"]
    sequences = []
    for primitive in primitives_list:
        primitive_dict = {}
        primitive_dict["skills"] = "抓取"
        primitive_dict["primitives"] = primitive
        if (primitive == '趋'):
            primitive_dict["target_lable"] = '螺母'
            primitive_dict["target_pose"] = '(x,y,z)'
        elif (primitive == '移'):
            primitive_dict["target_lable"] = '螺栓'
            primitive_dict["target_pose"] = '(x,y,z)'
        else:
            primitive_dict["target_lable"] = 'None'
            primitive_dict["target_pose"] = 'None'

        if (primitive == '抓'):
            primitive_dict["target_angle"] = '100'
        elif (primitive == '放'):
            primitive_dict["target_angle"] = '0'
        else:
            primitive_dict["target_angle"] = 'None'
        sequences.append(primitive_dict)

    # 统计sequences 的长度 并封装入json
    sequences_data_encapsulate["count"] = len(sequences)
    # 封装sequences
    sequences_data_encapsulate["data"] = {"sequences": sequences}
    # 封装结果转为json
    sequences_data_encapsulate_json = json.dumps(sequences_data_encapsulate, ensure_ascii=False)
    print(sequences_data_encapsulate_json)
    return sequences_data_encapsulate_json



encapsulate_sequences()