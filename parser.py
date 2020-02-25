def step_into(json_dict, key, backtrack):
    """
    (dict, str, list) -> None
    Goes through the object in nested structure
    """
    if key in json_dict:
        backtrack.append(json_dict)
        if isinstance(json_dict[key], dict): 
            show_key_options(json_dict[key], backtrack)
        elif isinstance(json_dict[key], list):
            el_count = len(json_dict[key])
            new_d = {}
            for el_num in range(el_count):
                new_d[str(el_num + 1)] = json_dict[key][el_num]
            show_key_options(new_d, backtrack)
        else:
            print(json_dict[key])
            print("You have reached your endpoint ^^")


def show_key_options(json_dict, backtrack):
    """
    (dict, list) -> None
    Prints key available for current nest
    """
    print("Keys available:")
    for key in json_dict:
        print(key, end=" "*5)
    key = input("\nEnter next key: ")
    step_into(json_dict, key, backtrack)
