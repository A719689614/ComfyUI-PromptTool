from .AC_CATEGORY import ac_category
import os
# =================================================================
script_dir = os.path.dirname(os.path.abspath(__file__))
absolute_path_1 = ('positive')
absolute_path_2 = ('negative')
# positve
file_path_1 = os.path.join(script_dir,absolute_path_1)
txt_files_1 = []
for file in os.listdir(file_path_1):
    if file.endswith(".txt"):
        txt_files_1.append(file)
# negative
file_path_2 = os.path.join(script_dir,absolute_path_2)
txt_files_2 = []
for file in os.listdir(file_path_2):
    if file.endswith(".txt"):
        txt_files_2.append(file)

# =================================================================
Switch_list = ["One", "Two"]

class Switch_1:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
            "Switch": (Switch_list,),
            "Prompt_1":("STRING",{"forceInput":True}),
            "Prompt_2":("STRING",{"forceInput":True}),
            }
            }
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Prompt",)
    FUNCTION = "switch"
    CATEGORY = ac_category()

    def switch(self, Switch,Prompt_1, Prompt_2):
        if Switch == "One":
            return (Prompt_1,)
        if Switch == "Two":
            return (Prompt_2,)
# =================================================================
class AC_Join_1:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
            "Prompt_1":("STRING",{"forceInput":True}),
            "Prompt_2":("STRING",{"forceInput":True}),
            }
            }
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Prompt",)
    FUNCTION = "switch_2"
    CATEGORY = ac_category()

    def switch_2(self,Prompt_1, Prompt_2):
        result = Prompt_1 + Prompt_2
        return (result,)
# =================================================================
class Positive_model:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required":{
            "List":(txt_files_1,)
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Prompt",)
    FUNCTION = "positive"
    CATEGORY = ac_category()

    def positive(self,List):
        new_path = os.path.join(file_path_1,List)
        f = open(new_path,'r',encoding='utf-8')
        result = f.read()
        f.close()
        return (result,)
# =================================================================
class Negative_model:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required":{
            "List":(txt_files_2,)
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Prompt",)
    FUNCTION = "negative"
    CATEGORY = ac_category()

    def negative(self,List):
        new_path = os.path.join(file_path_2,List)
        f = open(new_path,'r',encoding='utf-8')
        result = f.read()
        f.close()
        return (result,)
# =================================================================
