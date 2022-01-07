import json

def getCode(file):
    with open('data.txt') as json_file:
        data = json.load(json_file)
        if data['codes']:
            code = data['codes'][0]
            data['codes'].pop(0)
            print(data['codes'])
        else:
            print("error, no codes in file")
            codesRaw = input("Give me some codes: \n")
            codes = codesRaw.split()[2:-1]
            code = codes[0]
            codes.pop(0)
            data["codes"] = codes
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)
        return code

