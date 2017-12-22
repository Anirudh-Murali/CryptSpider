import pandas as pd
import numpy as np
import os as os

def get_months(data):
    num_of_months = data.shape[1] -2
    months = []
    for d in data.columns[1:num_of_months+1]:
        d = float(d)
#           print(d)
        months.append(d)
    starting_month = min(months)
    ending_month = float(starting_month) + float(num_of_months) - 1

    return months
def rename_months(data,months,key=0):
    if key ==1:
        named_months = ['week_name']
    else:
        named_months = []
    for i in months:
        if i == 1:
          named_months.append("January")
        elif i == 2:
          named_months.append("Febuary")
        elif i == 3:
          named_months.append("March")
        elif i == 4:
          named_months.append("April")
        elif i == 5:
          named_months.append("May")
        elif i == 6:
          named_months.append("June")
        elif i == 7:
          named_months.append("July")
        elif i == 8:
          named_months.append("August")
        elif i == 9:
          named_months.append("September")
        elif i == 10:
          named_months.append("October")
        elif i == 11:
          named_months.append("November")
        elif i == 12:
          named_months.append("December")
    if key == 1:
        named_months.append("index")
    #     print(named_months)
        data.columns = named_months
    #     print(data)
        return data
    else:
        return named_months

def check_returns(data,months):
    first = data[months[0]][0]
    k = -1

    returns_list = []
    for m in months:
        na_count = 0
        first = 0
        returns_value = []
        return_dict = {}
        for i in data[m].index:
                if k == -1:
                    k = 0
    #                 first = data[m][i]
                    continue


                else:
                    returns = data[m][i] - first
                    first = data[m][i]
    #                 k = -1
    #                 print(returns)
                    if returns > 0:
                        returns = 1
                    else:
                        returns = 0
                    returns_value.append(returns)
        returns_value = np.array(returns_value)
    #     print(returns_value.sum())
        deciding_factor = returns_value.sum()
        if deciding_factor > 2:
                return_dict[m] = True
        else:
                return_dict[m] = False

        return_dict["Number_of_Profitable_weeks"] = returns_value.sum()
        returns_list.append(return_dict)
    return(returns_list)


def selecting_criteria(data,returns_score,months):
    num_of_months = len(returns_score)
    to_clear = int(num_of_months * 0.50)                       #you can change the criteria here
    # print(to_clear)
    count = 0
    i = 0
    # selected = []
    for m in months:
        if returns_score[i][m] == True:
            count += 1
        i += 1
        if count > to_clear:
#             print("Coin Selected"+str(data['index'][0]))
            return True
    return False

def flash(data):
# data= pd.read_excel("Output/1BL/omisego.xls")
    months = get_months(data)
#     print(str(months))
    data = rename_months(data,months,1)
#     print(data)
    months.sort()
    months =rename_months(data,months)
#     print("-------------------------------------------")
    returns_score = check_returns(data,months)
#     print(returns_score)


    select = selecting_criteria(data,returns_score,months)
    print(data['index'][0]+"  :  "+str(select))
    return select

# print(selected_coins)

def run_it(folder,folder_name):
    count = 0
    names = pd.DataFrame()
    selected_coins = []

    for file in folder:
        filepath = folderpath + "\\" + file
    #     print(filepath)
        data = pd.read_excel("Output/"+folder_name+"/"+file)
        select = flash(data)
    #     print(data)
    #     break
        if select == True:
            selected_coins.append(data['index'][0])


        names = names.append(data, ignore_index=True)
        count = count + 1
    # print(names)
    print ("Files Imported" + str(count))
    print ("-----------------------------------------Selected coin:----------------------------------------------")
    print (selected_coins)
    selected_coins = pd.DataFrame(selected_coins)
    selected_coins.to_csv("Results/"+folder_name+".csv")
    print(len(selected_coins))


#set folder to import files from
folder_name = '1MIL-10MIL'
folderpath = r'/media/batman/Stuff/Projects/TE/Stirring Minds/API/Data_Scrapper/Output/'+str(folder_name)
folder = os.listdir(folderpath)
run_it(folder,folder_name)
#print list of files
