from random import randrange  

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
query_start = "SELECT * FROM \"FullTable\" "
query = ""       

#current question the game is asking
current = None

#List of available attributes to ask from
attribute_list = ["normal", "fight", "flying", "poison", "ground", "rock", "bug", "ghost", "steel", "fire", "water", "grass", "electric", "psychic", "ice", "dragon", "dark", "fairy"]

#Counter of extreme questions added to question_list
extreme_counter = 0

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
attribute - optional, used specifically for "againsts"
punctuation - optional, to round out "againsts"
null_check - for pokemon with no gender '''
#Combinations: Index0 and "y", Index0 and "n", Index1 and "y", Index1 and "n"

class Question_Func():
    global query
    input_list = ""
    begin_text = ""
    end_text = ""
    column_name = ""
    greater = " > "
    lesser = " < "
    median_val = 0
    flag = False
    attribute = ""
    punctuation = ""
    equal_sign = ""
    null_check = ""

    #Chooses positive or negative option
    def choose(self):
        self.choice = self.input_list[randrange(0,2)]
        self.ask()
    #Asks question
    def ask(self):
        self.input = input(self.begin_text + self.choice + self.end_text + self.attribute + self.punctuation)
        self.flag_handling()
        
    #Changes conjunction based on if question is asked first, last, or neither
    def flag_handling(self):
        if self.flag == 0:
            self.conjunction = ""
        if self.flag == 1:
            self.conjunction = "WHERE "
        if not self.flag:
            self.conjunction = " AND "
        self.query_builder()
    
    #Assembles the unique SQL statement
    def query_builder(self):
        global query
        if self.input == "y" and self.choice == self.input_list[0]:
            query = self.conjunction + self.column_name + self.greater + str(self.median_val) + self.null_check + query
            big_choice()
        elif self.input == "n" and self.choice == self.input_list[0]:
            query = self.conjunction + self.column_name + self.lesser + self.equal_sign + str(self.median_val) + self.null_check + query
            small_choice()
        elif self.input == "y" and self.choice == self.input_list[1]:
            query = self.conjunction + self.column_name + self.lesser + str(self.median_val) + self.null_check + query
            small_choice()
        elif self.input == "n" and self.choice == self.input_list[1]:
            query = self.conjunction + self.column_name + self.greater + self.equal_sign + str(self.median_val) + self.null_check + query
            big_choice()
        else:
            print("Please press only \"y\" or \"n\"")
            current.ask()
        question_picker()






# '''Questions below'''

class Size(Question_Func):
    input_list = ["taller", "shorter"]
    begin_text = "Is your pokemon "
    end_text = " than a golf club?"
    column_name = "height_m"
    greater = " >= "
    lesser = " <= "
    median_val = 1

class Minor_Size(Question_Func):
    end_text = " than a desk lamp?"
    median_val = 0.61
    input_list = ["taller", "shorter"]
    begin_text = "Is your pokemon "
    column_name = "height_m"
    greater = " >= "
    lesser = " <= "
    
class Major_Size(Question_Func):
    end_text = " than Danny Devito?"
    median_val = 1.5
    input_list = ["taller", "shorter"]
    begin_text = "Is your pokemon "
    column_name = "height_m"
    greater = " >= "
    lesser = " <= "

class Weight(Question_Func):
    input_list = ["heavier", "lighter"]
    begin_text = "Is your pokemon "
    end_text = " than a husky?"
    column_name = "weight_kg"
    greater = " >= "
    lesser = " <= "
    median_val = 27.3

class Minor_Weight(Question_Func):
    end_text = " than a weighted blanket?"
    median_val = 9
    input_list = ["heavier", "lighter"]
    begin_text = "Is your pokemon "
    column_name = "weight_kg"
    greater = " >= "
    lesser = " <= "

class Major_Weight(Question_Func):
    end_text = " than 140 pounds?"
    median_val = 64.35
    input_list = ["heavier", "lighter"]
    begin_text = "Is your pokemon "
    column_name = "weight_kg"
    greater = " >= "
    lesser = " <= "
    
class Generation(Question_Func):
    input_list = ["last 4", "original 3"]
    begin_text = "Was your pokemon first introduced in the "
    end_text = " generations?"
    column_name = "generation"
    median_val = 3.1


class Catch_Rate(Question_Func):
    input_list = ["regular pokeball", "ultra ball"]
    begin_text = "Would it make sense to use a(n) "
    end_text = " to catch your pokemon?"
    column_name = "capture_rate"
    median_val = 100
    
class Speed(Question_Func):
    input_list = ["fast", "slow"]
    begin_text = "Is your pokemon "
    end_text = "?"
    column_name = "speed"
    median_val = 65
   

class Legendary(Question_Func):
    input_list = ["legendary", "not legendary"]
    begin_text = "Is your pokemon "
    end_text = "?"
    column_name = "is_legendary"
    greater = " = "
    median_val = 1

class Gender(Question_Func):
    input_list = ["male", "female"]
    begin_text = "Is your pokemon usually "
    end_text = "?"
    column_name = "percentage_male"
    median_val = 50
    greater = " >= "
    lesser = " <= "
    null_check = f" OR {column_name} IS NULL "


class Two_Types(Question_Func):
    input_list = ["one", "two"]
    begin_text = "Does your pokemon have "
    end_text = " type(s)?"
    column_name = "type2"
    greater = " IS NULL"
    lesser = " IS NOT NULL"
    median_val = ""
   
class Againsts(Question_Func):
    input_list = ["weak", "strong"]
    begin_text = "Is your pokemon "
    end_text = " against "
    greater = " >"
    lesser = " <"
    median_val = 1
    punctuation = "?"
    equal_sign = "= "

    def __init__(self):
        self.attribute = attribute_list.pop(randrange(0, len(attribute_list) - 1))
        self.column_name = "against_" + self.attribute



#List of each question class 
question_list = [Size, Weight, Catch_Rate, Generation, Speed, Legendary, Gender, Two_Types] + [Againsts] * 5

#adds extreme question to question_list
def fine_tune(extreme_question):
    global extreme_counter
    if extreme_question not in question_list:
        question_list.append(extreme_question)
        extreme_counter += 1

#chooses correct extreme question to be added
def big_choice():
    if isinstance(current, Weight):
        fine_tune(Major_Weight)
    if isinstance(current, Size):
        fine_tune(Major_Size)

def small_choice():
    if isinstance(current, Weight):
        fine_tune(Minor_Weight)
    if isinstance(current, Size):
        fine_tune(Minor_Size)


#Chooses a question to pick
def question_picker():
    global current
    global query
    global query_start
    global extreme_counter
    if len(question_list) == 0:
        print("I have found your pokemon. Search for it using this query:\n" + query_start + query + ";")
    elif len(question_list) == 1 and extreme_counter == 2:
        current = question_list.pop(randrange(0, len(question_list)))()
        current.flag = 1
        current.choose()
    elif len(question_list) == 13:
        current = question_list.pop(randrange(1, len(question_list)))()
        current.flag = 0
        current.choose()
    else:
        current = question_list.pop(randrange(0, len(question_list)))()
        current.flag = False
        current.choose()

start_sequence() 