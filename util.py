import json
import pickle
import numpy as np
__locations=None
__data_columns=None
__model=None
def get_estimated_price_bang(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index=-1
    x= np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)


def get_location_names_bang():
    return __locations

def load_saved_artifacts1():           #banglore
    print("loading saved artifacts......start ")
    global __data_columns
    global __locations

    with open("columns_Banglore.json",'r') as f:
       __data_columns= json.load(f)['data_columns']
       __locations=__data_columns[3:]

    global  __model
    with open("banglore_house_price_model.pickle",'rb') as f:
        __model=pickle.load(f)
        print("loading saved artifacts is done")


def load_saved_artifacts2():  #Ahmedabad
    print("loading saved artifacts......start ")
    global __data_columns
    global __locations

    with open("columns_ahmedabad.json",'r') as f:
       __data_columns= json.load(f)['data_columns']
       __locations=__data_columns[3:]

    global  __model
    with open("Ahmedabad_home_prices_model.pickle",'rb') as f:
        __model=pickle.load(f)
        print("loading saved artifacts is done")


def load_saved_artifacts3():  #Delhi
    print("loading saved artifacts......start ")
    global __data_columns
    global __locations

    with open("columns_delhi.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    global __model
    with open("Delhi_house_price_model.pickle", 'rb') as f:
        __model = pickle.load(f)
        print("loading saved artifacts is done")

def load_saved_artifacts4():     #Mumbai
    print("loading saved artifacts......start ")
    global __data_columns
    global __locations

    with open("columns_mumbai.json",'r') as f:
       __data_columns= json.load(f)['data_columns']
       __locations=__data_columns[3:]

    global  __model
    with open("mumbai_house_price_model.pickle",'rb') as f:
        __model=pickle.load(f)
        print("loading saved artifacts is done")

def load_saved_artifacts5():     #Kolkata
    print("loading saved artifacts......start ")
    global __data_columns
    global __locations

    with open("columns_kolkata.json",'r') as f:
       __data_columns= json.load(f)['data_columns']
       __locations=__data_columns[3:]

    global  __model
    with open("Kolkata_home_prices_model.pickle",'rb') as f:
        __model=pickle.load(f)
        print("loading saved artifacts is done")


def load_saved_artifacts6():     #Indore
    print("loading saved artifacts......start ")
    global __data_columns
    global __locations

    with open("columns_indore.json",'r') as f:
       __data_columns= json.load(f)['data_columns']
       __locations=__data_columns[3:]

    global  __model
    with open("Indore_prices_model.pickle",'rb') as f:
        __model=pickle.load(f)
        print("loading saved artifacts is done")


def load_saved_artifacts7():     #Gurgaon
    print("loading saved artifacts......start ")
    global __data_columns
    global __locations

    with open("columns_gurgaon.json",'r') as f:
       __data_columns= json.load(f)['data_columns']
       __locations=__data_columns[3:]

    global  __model
    with open("Gurgaon_home_prices_model.pickle",'rb') as f:
        __model=pickle.load(f)
        print("loading saved artifacts is done")


def load_saved_artifacts8():     #Hydrabad
    print("loading saved artifacts......start ")
    global __data_columns
    global __locations

    with open("columns_hydrabad.json",'r') as f:
       __data_columns= json.load(f)['data_columns']
       __locations=__data_columns[3:]

    global  __model
    with open("Hydrabad_house_price_model.pickle",'rb') as f:
        __model=pickle.load(f)
        print("loading saved artifacts is done")


def load_saved_artifacts9():     #Chennai
    print("loading saved artifacts......start ")
    global __data_columns
    global __locations

    with open("columns_chennai.json",'r') as f:
       __data_columns= json.load(f)['data_columns']
       __locations=__data_columns[3:]

    global  __model
    with open("chennai_house_price_model.pickle",'rb') as f:
        __model=pickle.load(f)
        print("loading saved artifacts is done")

def load_saved_artifacts10():     #Pune
    print("loading saved artifacts......start ")
    global __data_columns
    global __locations

    with open("columns_pune2.json",'r') as f:
       __data_columns= json.load(f)['data_columns']
       __locations=__data_columns[3:]

    global  __model
    with open("pune2.pickle",'rb') as f:
        __model=pickle.load(f)
        print("loading saved artifacts is done")



if __name__=="__main__":
    load_saved_artifacts10()
    print (get_location_names_bang())
    print(get_estimated_price_bang('Hinjewadi', 1000, 2, 2))
