    
from random import randrange, choice    

#Welcome message function    
def start_sequence():
    start_message = input("Welcome to 20 Questions Pokemon Edition! \nPlease think of a Pokemon. \nWhen you are ready to play press the Enter key, and I will try to guess your pokemon in 20 questions or less! \n(Please respond only respond to questions by pressing \"y\" or \"n\")")
    if start_message != "":
        def catch_sequence():
            catch_message = input("Please press the Enter (or Return) key to start the game.")
            if catch_message != "":
                catch_sequence()
        catch_sequence()
    question_picker()

#SQL code to build and ultimately return
query_start = "USE Pokedex SELECT * FROM PokeTable "
query = ""       

#current question the game is asking
current = None

#List of available attributes to ask from
attribute_list = ["normal", "fight", "flying", "poison", "ground", "rock", "bug", "ghost", "steel", "fire", "water", "grass", "electric", "psychic", "ice", "dragon", "dark", "fairy"]

#List denoting which attributes the pokemon is strong or weak against. Example element: ("strong", "water")
affect_list = []
            
'''general template for asking question and adding response to query
input_list - 2 elements, all elements of the same index must behave the same (> or <) 
begin_text - first half of question
end_text - second half of question
column_name - name of column in database that the question corresponds to
greater - typically >
lesser - typically <
median_val - middle value of sorted column
flag - 0 indicates first question, 1 indicates last question, False indicates neither
attribute - optional, used specifically for "against_questions"
punctuation - optional, to round out "against_questions" '''
#Combinations: Index0 and "y", Index0 and "n", Index1 and "y", Index1 and "n"
def question_func(input_list, begin_text, end_text, column_name, greater, lesser, median_val, flag=False, attribute="", punctuation=""):
    global query
    choice = input_list[randrange(0,2)]
    question = input(begin_text + choice + end_text + attribute + punctuation)
    
    #flag handling
    if flag == 0:
        conjunction = ""
    if flag == 1:
        conjunction = "WHERE "
    if not flag:
        conjunction = " AND "

    #query builder
    if question == "y" and choice == input_list[0]:
        query = conjunction + column_name + greater + str(median_val) + query
    elif question == "n" and choice == input_list[0]:
        query = conjunction + column_name + lesser + str(median_val) + query
    elif question == "y" and choice == input_list[1]:
        query = conjunction + column_name + lesser + str(median_val) + query
    elif question == "n" and choice == input_list[1]:
        query = conjunction + column_name + greater + str(median_val) + query
    else:
        print("Please press only \"y\" or \"n\"")
        current(flag=flag, attribute=attribute)
    question_picker()



# '''Questions below'''

def size_question(flag=False, attribute=""):
    input_list = ["taller", "shorter"]
    begin_text = "Is your pokemon "
    end_text = " than a golf club?"
    column_name = "height_m"
    greater = " > "
    lesser = " < "
    median_val = 1
    question_func(input_list, begin_text, end_text, column_name, greater, lesser, median_val, flag, attribute)

def weight_question(flag=False, attribute=""):
    input_list = ["heavier", "lighter"]
    begin_text = "Is your pokemon "
    end_text = " than a husky?"
    column_name = "weight_kg"
    greater = " > "
    lesser = " < "
    median_val = 27.3
    flag = flag
    question_func(input_list, begin_text, end_text, column_name, greater, lesser, median_val, flag, attribute)


def generation_question(flag=False, attribute=""):
    input_list = ["last 4", "original 3"]
    begin_text = "Is your pokemon part of the "
    end_text = " generations?"
    column_name = "generation"
    greater = " > "
    lesser = " < "
    median_val = 3.1
    flag = flag
    question_func(input_list, begin_text, end_text, column_name, greater, lesser, median_val, flag, attribute)


def catch_rate_question(flag=False, attribute=""):
    input_list = ["regular pokeball", "ultra ball"]
    begin_text = "Would it make sense to use a(n) "
    end_text = " to catch your pokemon?"
    column_name = "capture_rate"
    greater = " > "
    lesser = " < "
    median_val = 100
    flag = flag
    question_func(input_list, begin_text, end_text, column_name, greater, lesser, median_val, flag, attribute)
    
def speed_question(flag=False, attribute=""):
    input_list = ["fast", "slow"]
    begin_text = "Is your pokemon "
    end_text = "?"
    column_name = "speed"
    greater = " > "
    lesser = " < "
    median_val = 65
    flag = flag
    question_func(input_list, begin_text, end_text, column_name, greater, lesser, median_val, flag, attribute)

def legendary_question(flag=False, attribute=""):
    input_list = ["legendary", "not legendary"]
    begin_text = "Is your pokemon "
    end_text = "?"
    column_name = "is_legendary"
    greater = " > "
    lesser = " < "
    median_val = 0.5
    flag = flag
    question_func(input_list, begin_text, end_text, column_name, greater, lesser, median_val, flag, attribute)

def gender_question(flag=False, attribute=""):
    input_list = ["male", "female"]
    begin_text = "Is your pokemon usually "
    end_text = "?"
    column_name = "percentage_male"
    greater = " > "
    lesser = " < "
    median_val = 51
    flag = flag
    question_func(input_list, begin_text, end_text, column_name, greater, lesser, median_val, flag, attribute)


def two_types_question(flag=False, attribute=""):
    input_list = ["one", "two"]
    begin_text = "Does your pokemon have "
    end_text = " type(s)?"
    column_name = "type2"
    greater = " IS NULL "
    lesser = " IS NOT NULL "
    median_val = ""
    flag = flag
    question_func(input_list, begin_text, end_text, column_name, greater, lesser, median_val, flag, attribute)

def against_questions(flag=False, attribute=""):
    if not attribute:
        attribute = attribute_list.pop(randrange(0, len(attribute_list) - 1))
    input_list = ["weak", "strong"]
    begin_text = "Is your pokemon "
    end_text = " against "
    column_name = "against_" + attribute
    greater = " >= "
    lesser = " <= "
    median_val = 1
    flag = flag
    punctuation = "?"
    question_func(input_list, begin_text, end_text, column_name, greater, lesser, median_val, flag, attribute, punctuation)

#Binding of each function to name
size = size_question
weight = weight_question
generation = generation_question
catch_rate = catch_rate_question
speed = speed_question
legendary = legendary_question
against = against_questions
gender = gender_question
two_types = two_types_question

#List of each question function
question_list = [size, weight, generation, catch_rate, speed, legendary, gender, two_types] + [against] * 5

#Chooses a question to pick
def question_picker():
    global current
    global query
    global query_start
    if len(question_list) == 0:
        print("I have found your pokemon. Search for it using this query:\n" + query_start + query + ";")
    elif len(question_list) == 1:
        current = question_list.pop(randrange(0, len(question_list)))
        current(flag=1)
    elif len(question_list) == 13:
        current = question_list.pop(randrange(1, len(question_list)))
        current(flag=0)
    else:
        current = question_list.pop(randrange(0, len(question_list)))
        current(flag=False)

start_sequence() 