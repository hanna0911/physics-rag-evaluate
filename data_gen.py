####################################
## 产生待测试数据的文件，数据格式如下
####################################

# test_data = [{"description": "大学物理", "selection1": "1", "selection2": "2"}, 
#              {"description": "大学物理", "selection1": "123", "selection2": "fas"},
#              {"description": "大学物理", "selection1": "423", "selection2": "534"},]


import json

with open("physics_gen_q.json", "r") as f:
    unragged = json.load(f)

with open("physics_gen_q_ragged.json", "r") as f:
    ragged = json.load(f)


total_cnt = len(unragged)

test_data = []

for i in range(total_cnt):
    description = f"请选出下列题目中，更符合用户需求的题目。\n\n用户需求：{unragged[i]['user']}"
    test_data.append({"description": description, "selection1": unragged[i]['gen'].replace("\(", "$").replace("\)", "$").replace("\[", "$").replace("\]", "$"), "selection2": ragged[i]['gen'].replace("\(", "$").replace("\)", "$").replace("\[", "$").replace("\]", "$")})
