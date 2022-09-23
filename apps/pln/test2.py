import ast
def list_txt_data_clean():
    print("-- list txt data clean ---")
    with open('apps/pln/services/save_tt.txt', 'r') as data:
        data_list = ast.literal_eval(data.read())
    return data_list

list_txt_data_clean()