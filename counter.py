import re

checklist = []
lastdata = {}
contacts = []

def calc_spammer(lastdata):
    values = list(lastdata.values())
    keys = list(lastdata.keys())
    maxkey = max(values)
    index = values.index(maxkey)
    print(keys[index]," is the champion in this group with ",values[index],"messages.")

def create_dataset(contacts,checklist):
    for elem in contacts:
        if elem in checklist and elem not in lastdata.keys():
            lastdata[elem]=1
        else:
            lastdata[elem] = lastdata[elem] + 1
    data_list = list(lastdata.items())
    sorted_list = sorted(data_list, key=lambda x: x[1])
    count = 0
    for item in sorted_list:
        print(str(item[0]) +": score: "+str(item[1]) +"  Rating:" + str(len(sortedList)-count))
        count+=1
    # print(sorted(lastdata,key=lambda x: lastdata[keyList.index(x.key())]))
    calc_spammer(lastdata)

def create_checklist(contacts):
    for i in range(10):
        for elem in contacts:
            if elem not in checklist:
                checklist.append(elem)
            else:
                pass
    create_dataset(contacts,checklist)

def filter_list(contacts):
    for i in range(3):
        for elem in contacts:
            if ':' in elem:
                contacts.remove(elem)
    create_checklist(contacts)

def flatten_list(contacts):
    contacts = [item for sublist in contacts for item in sublist]
    filter_list(contacts)

def extract_data(string):
    print("Date range is " +str(string[0]).strip().split(" ")[0].split(",")[0].strip() + " "+ str(string[len(string)-1]).split(" ")[0].split(",")[0].strip())
    for i in range(len(string)):
        match = re.findall('-(.*):',string[i])
        contacts.append(match)
    flatten_list(contacts)

def open_file():
    file = open("data.txt",'r', errors='ignore')
    string = file.read()
    string = string.splitlines()
    extract_data(string)

if __name__ == "__main__":
    open_file()



