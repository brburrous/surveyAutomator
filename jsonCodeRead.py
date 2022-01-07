import json

def getCode(file, index):
    with open('data.txt') as json_file:
        data = json.load(json_file)
        if data['codes']:
            codes = data['codes']
        else:
            codesRaw = input("Give me some codes: \n").split()
            codes = codesRaw[2:len(codesRaw)]
            data["codes"] = codes
    code = list(filter(lambda x: x.startswith(index), codes))[0]
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)
        return code

