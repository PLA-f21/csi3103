# csi3103

### user_data.json 사용하는법

```python
import json

# load json file
with open("data/user_data.json") as f:
    user_data = json.load(f)
  
# use example
print(user_data["eat_time"]["490"]["25"]["breakfast"]) # 7:24
# id 490 ate breakfast at 7:24 on the 25th

print(user_data["eat_time"]["228"]["5"]) # {'breakfast': '-', 'lunch': '-', 'dinner': '-'}
# id 228 didn't eat anyting(?) on the 5th 

print(user_data["sleep_time"]["490"]["25"]) # {'start': '23:20', 'end': '6:03'}
# id 490 slept on the 24th 23:20 and woke up on the 25th 6:03 
```

주의할 점은 dict 키값은 전부 str 타입임


### 생활점수 상위 몇% 인지 구하는 스크립트

```python
# user_data["activition_score"]["average"] 이게 평균

rank = 0
my_score = user_data["activition_score"][id] # id example) id = "228"
for uid in user_data["activition_score"].keys():
    if (float(my_score) >= float(user_data["activition_score"][uid])) and uid != "average":
        rank += 1

rate = rank * 100 // (len(user_data["activition_score"]) - 1) # because we have to exclude "average"
```
