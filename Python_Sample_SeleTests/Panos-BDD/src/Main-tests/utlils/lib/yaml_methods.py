from utils.lib import read_yaml

def yaml_dictionary(input_data_file_name, table):
    test_input_data = read_yaml(input_data_file_name)
    yaml_to_dict = test_input_data[table]
    return yaml_to_dict

def compare_wordings(context, actual_text, expected_text, include_flag=False, include_multi=False,
                     include_in_multi=False, include_all=False):
    #...
