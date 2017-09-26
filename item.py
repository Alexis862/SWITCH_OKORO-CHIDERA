the_list=["James", 75 ,["joseph", "dudeth"],["first", "baby"],("football","orange"),{"position":"first"}]
print()
def extract_list(item_list):
    for item in item_list:
        if type(item)==list or type(item)== tuple:
            extract_list(item)
        print(item)

            
extract_list(the_list)
