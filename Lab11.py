import pandas as pd
import json

# Given Data:
data = [1121, "Jackie Grainger", 22.22,
1122, "Jignesh Thrakkar", 25.25,
1127, "Dion Green", 28.75, False,
24.32, 1132, "Jacob Gerber",
"Sarah Sanderson", 23.45, 1137, True,
"Brandon Heck", 1138, 25.84, True,
1152, "David Toma", 22.65,
23.75, 1157, "Charles King", False,
"Jackie Grainger", 1121, 22.22, False,
22.65, 1152, "David Toma"]

new_data = []
info = {}
for ele in data:
    if(type(ele)==int):
        info['emp_info'] = ele
    elif(type(ele)==str):
        info['emp_name'] = ele
    elif(type(ele)==float):
        info['emp_hrl_wage'] = ele
    else:
        pass
    if(len(info)==3):
        new_data.append(info)
        info = {}

df = pd.DataFrame(new_data)
df.drop_duplicates(subset ="emp_info",keep = False, inplace = True)
df['total_hrl_rate'] = df['emp_hrl_wage'] * 1.3
main_list = json.loads(df.to_json(orient ='records'))
main_list

# Getting list of emp with underpaid Salary.
underpaid_salaries = df[df['total_hrl_rate'] < 30.65]  [df['total_hrl_rate'] > 28.15]
underpaid_salaries = json.loads(underpaid_salaries.to_json(orient ='records'))
underpaid_salaries

def get_raise(wage):
    if(wage >= 22.0 and wage < 24.0):
        return wage * 0.05
    elif(wage >= 24.0 and wage < 26.0):
        return wage * 0.04
    elif(wage >= 26.0 and wage < 28.0):
        return wage * 0.03
    else:
        return wage * 0.02

#company_raises
df['raise'] = df['emp_hrl_wage'].map(get_raise)
company_raises = json.loads(df[['emp_name','raise']].to_json(orient ='records'))
company_raises