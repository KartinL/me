"""All about IO."""

# python3 ../course/week4/tests.py

import json
import os
import requests
import inspect
import sys
import time

# Handy constants
LOCAL = os.path.dirname(os.path.realpath(__file__))  # the context of this file
CWD = os.getcwd()  # The curent working directory
if LOCAL != CWD:
    print("Be care`ful that your relative paths are")
    print("relative to where you think they are")
    print("LOCAL", LOCAL)
    print("CWD", CWD)


def get_some_details():
    """Parse some JSON.

    In lazyduck.json is a description of a person from https://randomuser.me/
    Read it in and use the json library to convert it to a dictionary.
    Return a new dictionary that just has the last name, password, and the
    number you get when you add the postcode to the id-value.
    TIP: Make sure that you add the numbers, not concatinate the strings.
         E.g. 2000 + 3000 = 5000 not 20003000
    TIP: Keep a close eye on the format you get back. JSON is nested, so you
         might need to go deep. E.g to get the name title you would need to:
         data["results"][0]["name"]["title"]
         Look out for the type of brackets. [] means list and {} means
         dictionary, you'll need integer indeces for lists, and named keys for
         dictionaries.
    """

    # script_dir = os.path.dirname(__file__)
    # file_path = os.path.join(script_dir, "/lazyduck.json"
    # print(file_path)
    # fptr = open(file_path, 'r')

    # script_dir = os.path.dirname(__file__) 
    # rel_path = "/lazyduck.json"
    # abs_file_path = os.path.join(script_dir, rel_path)
    
    # open and read json file 
    json_data = open(LOCAL + "/lazyduck.json").read()  

    # convert from json string to a dictionary 
    data = json.loads(json_data) 

    # print last name 

    last = data["results"][0]["name"]["last"]
    pw = data["results"][0]["login"]["password"]
    num = data["results"][0]["location"]["postcode"] + int(data["results"][0]["id"]["value"])
    
    #  convert it to integers 

    # for lastName, password in dict.items():
    #     print(lastName, password)
    # mode = "r"
    # print results.get("lastName")
    # print (keys_needed)  

        # with open('https://randomuser.me/', 'r') as fp:
        #     obj = json.load(fp)

    # data = json.dumps(json_data)
    # data = json.loads(json_data)
    # print (json_data)

    # thisdict= {/lazyduck.json}

    # lastName = thisdict["lastName"]
    # password = thisdict["password"]
    # postcodePlusID = thisdict["postcode + ID"]

    return {"lastName": last, "password": pw, "postcodePlusID": num}


def wordy_pyramid():
    """Make a pyramid out of real words.

    There is a random word generator here:
    http://api.wordnik.com/v4/words.json/randomWords?api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5&minLength=10&maxLength=10&limit=1
    The arguments that the generator takes is the minLength and maxLength of the word
    as well as the limit, which is the the number of words. 
    Visit the above link as an example.
    Use this and the requests library to make a word pyramid. The shortest
    words they have are 3 letters long and the longest are 20. The pyramid
    should step up by 2 letters at a time.
    Return the pyramid as a list of strings.
    I.e. ["cep", "dwine", "tenoner", ...]
    [
    "cep",
    "dwine",
    "tenoner",
    "ectomeric",
    "archmonarch",
    "phlebenterism",
    "autonephrotoxin",
    "redifferentiation",
    "phytosociologically",
    "theologicohistorical",
    "supersesquitertial",
    "phosphomolybdate",
    "spermatophoral",
    "storiologist",
    "concretion",
    "geoblast",
    "Nereis",
    "Leto",
    ]
    TIP: to add an argument to a URL, use: ?argName=argVal e.g. &minLength=
    """

    key = "91xyilewfpmpj4yxy8czdk62875bkkljjdqchl0zkklspme95"
    template = "http://api.wordnik.com/v4/words.json/randomWords?api_key={key}&minLength={minLength}&maxLength={maxLength}&limit={limit}"
    # http://api.wordnik.com/v4/words.json/randomWords?api_key=91xyilewfpmpj4yxy8czdk62875bkkljjdqchl0zkklspme95&minLength=3&maxLength=20&limit=18
    minLength = 3
    maxLength = 20
    limit = 1
    step = 2
    pyramid_list = []
    
    for length in range(minLength, maxLength, step):
        time.sleep(1)
        url = template.format(base=template, minLength=length, maxLength=length, limit=limit, key=key)
        r = requests.get(url)
        if r.status_code is 200:
            the_json = json.loads(r.text)
            # print(the_json)
            # print(list(a.values()))
            a = the_json[0]["word"]
            # print(a)
            pyramid_list.append(a)
    
    for item in pyramid_list:
        print(item)

    for length in range(maxLength, minLength, -step):
        time.sleep(1)
        url = template.format(base=template, minLength=length, maxLength=length, limit=limit, key=key)
        r = requests.get(url)
        if r.status_code is 200:
            the_json = json.loads(r.text)
            # print(the_json)
            # print(list(a.values()))
            a = the_json[0]["word"]
            # print(a)
            pyramid_list.append(a)

    for item in pyramid_list:
        print(item)

            # b = the_joson[]["word"]
            # print(a.values())

            # print(b)
            # print()
            # if len(a) == 3:
            # a = the_json["word"]
            # print(a)
            # print(len(a))
            # print(min((word for word in i if word), key=len))
            # print(str(min(a, key=len)))

            # if len(a) == 3:
            #     pyramid_list.append()
            #     # print(pyramid_list.append)
            #     a = len(a) + 2
            #     if len(a) == 20:
            #         a = len(a) - 2
            #         if len(a) == 4:
                        # break


def get_poke_height(id):

    template = "https://pokeapi.co/api/v2/pokemon/{id}"
    url = template.format(id=i)
    r = requests.get(url)
    if r.status_code is 200:
        the_json = json.loads(r.text)
        # converts it into a dictionary 
        height = the_json['height']
        return height




def pokedex(low=1, high=5):
    """ Return the name, height and weight of the tallest pokemon in the range low to high.

    Low and high are the range of pokemon ids to search between.
    Using the Pokemon API: https://pokeapi.co get some JSON using the request library
    (a working example is filled in below).
    Parse the json and extract the values needed.
    
    TIP: reading json can someimes be a bit confusing. Use a tool like
         http://www.jsoneditoronline.org/ to help you see what's going on.
    TIP: these long json accessors base["thing"]["otherThing"] and so on, can
         get very long. If you are accessing a thing often, assign it to a
         variable and then future access will be easier.
    """
    # template = "https://pokeapi.co/api/v2/pokemon/{id}"

    # url = template.format(id=5)
    # r = requests.get(url)
    # if r.status_code is 200:
    #     the_json = json.loads(r.text)
    #     the_json = r.json() (does the same as the line above)
    #     print(the_json)
    


    template = "https://pokeapi.co/api/v2/pokemon/{id}"
    
    max_height = 0 
    for i in range(low, high):
        url = template.format(id=i)
        r = requests.get(url)
        if r.status_code is 200:
            the_json = json.loads(r.text)
            # converts it into a dictionary 
            x = the_json['height']
            if x > max_height: 
                max_height = x
                height = the_json['height']
                # this gets the info from the json dictionary 
                weight = the_json['weight']
                name = the_json['name']
        
    # print(the_json['weight'])

    # weight = the_json['weight']
    # height = the_json['height']
    # name = the_json['name']

    return {"name": name, "weight": weight, "height": height}


def diarist():
    """Read gcode and find facts about it.

    Read in Trispokedovetiles(laser).gcode and count the number of times the
    laser is turned on and off. That's the command "M10 P1".
    Write the answer (a number) to a file called 'lasers.pew' in the week4 directory.
    TIP: you need to write a string, so you'll need to cast your number
    TIP: Trispokedovetiles(laser).gcode uses windows style line endings. CRLF
         not just LF like unix does now. If your comparison is failing this
         might be why. Try in rather than == and that might help.
    TIP: remember to commit 'lasers.pew' and push it to your repo, otherwise
         the test will have nothing to look at.
    TIP: this might come in handy if you need to hack a 3d print file in the future.
    """

    f = open("lasers.pew","w+")
    data = open("Trispokedovetiles(laser).gcode").read()
    count = str(data.count('M10 P1'))
    print(count)
    f.write(count)
    f.close()



if __name__ == "__main__":
    functions = [
        obj
        for name, obj in inspect.getmembers(sys.modules[__name__])
        if (inspect.isfunction(obj))
    ]
    for function in functions:
        try:
            print(function())
        except Exception as e:
            print(e)
    if not os.path.isfile("lasers.pew"):
        print("diarist did not create lasers.pew")