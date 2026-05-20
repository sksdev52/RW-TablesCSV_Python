dict_lst = []
        for z in range (0, len(table)):
                empty_lst = []
                new_dict = {str(table[z][0]): empty_lst}
                dict_lst.append(new_dict)
                for y in range (1, len(table[z])): # since [0] is the column title
                    element = float(table[z][y])
                    empty_lst.append(element)
    return dict_lst