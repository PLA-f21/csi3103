#!/usr/bin/env python
# coding: utf-8

# In[5]:


import csv
import json
import openpyxl as xl

wb = xl.load_workbook("data/user_profile.xlsx")
col = wb["user_profile"]["A"][1:]
file = []

for i in range(len(col)):
    file.append(str(col[i].value))


# In[6]:


##file = ['513','534','720','530'] # (IMPOLTANT!!!! HARD CODING!!! we should add in this array for file number.. sad)
# file '530' is empty

k = 0  # for file index
total_people_num = len(file)

# initial calculation
outing_density = {}

# under these are density
place_toilet = {}
place_kitchen = {}
place_living = {}  # ex) watching tv
activition_score = {}

# sooni's talk
recent_sooni_talk = {}

# eating pill days are not overlapped
# plus, if want to display the time, we should ""recent 3 days""!!
pill_time = (
    {}
)  # display the unbalance time. if this is empty, not eating pill or eating well


# In[7]:


while k < len(file):

    local_height = 0  # for finding height of file
    local_outing = 0

    local_totalplace = 0  # I plus this for density
    local_place_toilet = 0
    local_place_kitchen = 0
    local_place_living = 0

    local_activition_score = 0.0
    local_totalactivition = 0

    i = 2  # pill time index
    local_pill = []
    local_pill_unbalance = ""
    local_pill_flag = False
    if int(file[k]) < 30064:
        f = open("data/hs_g73_m08/hs_" + file[k] + "_m08_0903_1355.csv", "r")
    else:
        f = open("data/hs_g73_m08/hs_" + file[k] + "_m08_0903_1356.csv", "r")

    rdr = csv.reader(f)

    # reading for each csv file
    for line in rdr:
        ##print(line[2])

        if line[2] == "외출":  # calculation outing density
            local_outing += 1

        # calculation activition score
        if line[2] == "매우 활동":
            local_activition_score += 2.0
            local_totalactivition += 1
        elif line[2] == "활동":
            local_activition_score += 1.0
            local_totalactivition += 1
        elif line[2] == "미동":
            local_activition_score += 0.3
            local_totalactivition += 1
        elif line[2] == "부동":
            local_totalactivition += 1
        elif line[2] == "프로그램":
            local_activition_score += 1.0
            local_totalactivition += 1
        elif line[2] == "외출":
            local_activition_score += 1.0
            local_totalactivition += 1

        # calculation place density(int number)
        if line[2] == "변기":
            local_place_toilet += 1
            local_totalplace += 1
        elif (line[2] == "프로그램") or (line[2] == "리모콘"):
            local_place_living += 1
            local_totalplace += 1
        elif (
            (line[2] == "전자렌지")
            or (line[2] == "식사 판단")
            or (line[2] == "냉장고")
            or (line[2] == "식사")
        ):
            local_place_kitchen += 1
            local_totalplace += 1

        if line[7] == "Message_1":
            recent_sooni_talk[file[k]] = ""

        if (line[7] != "") and (line[7] != "프로그램 메시지") and (line[7] != "Message_1"):
            recent_sooni_talk[file[k]] = line[7]

        # medicine (pill) time check
        if line[2] == "약":
            local_pill.append(line[1])

        # if 3 days continuous time delay above 2 hours, pill flag is true (bad behavior)
        while i < len(local_pill):
            if (int(local_pill[i - 2][12:14]) - int(local_pill[i - 1][12:14])) < -1 or (
                int(local_pill[i - 2][12:14]) - int(local_pill[i - 1][12:14])
            ) > 1:
                if (int(local_pill[i - 1][12:14]) - int(local_pill[i][12:14])) < -1 or (
                    int(local_pill[i - 1][12:14]) - int(local_pill[i][12:14])
                ) > 1:
                    local_pill_flag = True

            if local_pill_flag == True:
                # if want to show recent 3 days, local_pill_unbalance = local_pill[i-2] + local_pill[i-1] + local_pill[i]
                local_pill_unbalance = (
                    local_pill_unbalance
                    + local_pill[i - 2]
                    + local_pill[i - 1]
                    + local_pill[i]
                    + " && "
                )
                local_pill_flag = False

            i += 1

        ##print(local_pill)
        local_height += 1  # index(height) plus

    # file loop finish
    f.close()

    # store in dictionary
    try:
        outing_density[file[k]] = format(
            (local_outing / 31), ".3f"
        )  # store outing density
    except ZeroDivisionError:
        outing_density[file[k]] = 0.000

    try:
        activition_score[file[k]] = format(
            (local_activition_score / local_totalactivition), ".5f"
        )
    except ZeroDivisionError:
        activition_score[file[k]] = 0.00000

    try:
        place_toilet[file[k]] = format((local_place_toilet / local_totalplace), ".3f")
    except ZeroDivisionError:
        place_toilet[file[k]] = 0.000

    try:
        place_kitchen[file[k]] = format((local_place_kitchen / local_totalplace), ".3f")
    except ZeroDivisionError:
        place_kitchen[file[k]] = 0.000

    try:
        place_living[file[k]] = format((local_place_living / local_totalplace), ".3f")
    except ZeroDivisionError:
        place_living[file[k]] = 0.000

    if local_pill_unbalance != "":
        pill_time[file[k]] = local_pill_unbalance
    else:
        pill_time[file[k]] = ""

    # plus file index
    k += 1


# In[8]:


# outing_density


# In[9]:


# activition_score


# In[10]:


# place_toilet


# In[11]:


# place_kitchen


# In[12]:


# place_living


# In[13]:


# total_people_num


# In[14]:


# recent_sooni_talk


# In[15]:


# pill_time


# In[ ]:


user_data = {
    "outing_density": outing_density,
    "activation_score": activition_score,
    "place_toilet": place_toilet,
    "place_kitchen": place_kitchen,
    "place_living": place_living,
    "total_people_num": total_people_num,
    "recent_sooni_talk": recent_sooni_talk,
    "pill_time": pill_time,
}

with open("data/user_data.json", "w") as f:
    json.dump(user_data, f)
