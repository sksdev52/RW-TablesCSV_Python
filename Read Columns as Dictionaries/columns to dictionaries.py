#Python 3.14.2
import csv
#import json
#import os
def table_transpose(a=[]):
    c=[]
    for r in range (len(a)): #iterate through each row in the matrix starting with the first row
        for e in range (len (a[r])): #The number of elements in the first column
            row =[]
            for p in range (len(a)):
                element= a[p][e] # Take the eth element of each row
                row.append(element) # Append in a new row, then let the r loop go to the next row and so on resulting in interchanging rows with colomns
            c.append(row)
        return c
def column_to_dictionary_no_title(datafile=str):
    
    with open(datafile, mode ='r', encoding="utf8") as infile: 
        reader = csv.reader(infile, delimiter=',')
        table = []
        for row in reader:
            if not any(cell.strip() for cell in row): # If empty row is encountered
                break
            else:
                in_col = row
                table.append(in_col)
        table = table_transpose(table)
        dict_lst = []
        for z in range (0, len(table)):
                empty_lst = []
                new_dict = {str(table[z][0]): empty_lst}
                dict_lst.append(new_dict)
                for y in range (1, len(table[z])): # since [0] is the column title
                    element = float(table[z][y])
                    empty_lst.append(element)
        return dict_lst    

def column_to_dictionary_one_title(datafile=str,title =str):
    '''
    Example "Test" is the title that is passed to the function. if the very first entry of the very first line
    of the csv file is the same as the title then in the example below hdr0[0] will match the title string. Otherwise
    the code will enter the else loop and enter the for row in reader loop and look to match the title string
    with row[0] entry.
    '''
    found_title = False
    with open(datafile, mode ='r', encoding="utf8") as infile: 
        reader = csv.reader(infile, delimiter=',')
        for row in reader:
            if len(row) >0:
                if row[0] == title:
                    found_title = True
                    table = []
                    for row in reader:
                       if not any(cell.strip() for cell in row): # If empty row is encountered
                           break
                       else:
                           in_col = row
                           table.append(in_col)
                            
                    table = table_transpose(table)
                    dict_lst = []
                    for z in range (0, len(table)):
                         empty_lst = []
                         new_dict = {str(table[z][0]): empty_lst}
                         dict_lst.append(new_dict)
                         for y in range (1, len(table[z])): # since [0] is the column title
                             element = float(table[z][y])
                             empty_lst.append(element)
                    return dict_lst
                
#IMPORTANT: THIS FUNCTION REQUIRES A BLANK LINE BETWEEN THE TITLE AND SUBTITLE IN CERTAIN SITUATIONS
def column_to_dictionary_with_title_subtitle(datafile=str, title= str, subtitle= str): # Data file name, title name, subtitle name 
        ''' 
        IMPORTANT: THIS FUNCTION REQUIRES A BLANK LINE BETWEEN THE TITLE AND SUBTITLE IN CERTAIN SITUATIONS
        DO NOT insert another title, subtitile and column title within one title. For reference in the example
        below please do not insert title for year 2025, month and day within year 2026. The values for 2025 should 
        either be above the year 2026 or below it. Code is not designed to pick up such errors.
        Sometimes matching row[0] to string works, other times matching row to string works.
         If there is only one entry in the entire row match row to string.
         Exception in this case is title row where row[0] matches and using just row returns an empty list.
        Trying to match hdr2[0] gives list index out of range error
        #Trying to match hdr3 to coltl results in not entering the loop while hdr3[0] works.
        '''
        lsts_of_dicts_to_send=[]
        table = []
        with open(datafile, mode ='r', encoding="utf8") as infile: # Open csv file dictread in read mode
            
            reader = csv.reader(infile, delimiter=',')
            found_title = False
            
            for row in reader:
                    if len(row) >0: # To skip blank row
                            if row[0] == title: 
                                found_title = True
                                if found_title == True:
                                    found_subtitle = False
                                    hdr2 = next(reader) # Find subtitle
                                    if hdr2 == subtitle:   # If subtitle is also found              
                                        found_subtitle = True
                                        if found_subtitle == True:
                                            for row in reader:
                                                    if not any(cell.strip() for cell in row):
                                                        break
                                                    else:
                                                        in_col = row
                                                        table.append(in_col)
                                        
                                    
                                    elif not found_subtitle: # If subtitle was not found                                                   
                                        for row in reader: # Look for subtitle again
                                            if len(row) >0: 
                                                if row[0] == subtitle: # If subtitle is found
                                                    found_subtitle = True
                                                    if found_subtitle == True:
                                                        for row in reader:
                                                            if not any(cell.strip() for cell in row):
                                                                    break
                                                            else:
                                                                in_col = row
                                                                table.append(in_col)
                                                                                                   
                                                                    
                            
                                else:
                                    found_title == False
                                    hdr1a = next(reader) # Find subtitle
                                    if hdr1a == title:   # If subtitle is also found
                                        found_title = True
                                        if found_title == True:
                                            found_subtitle = False
                                            hdr2 = next(reader) # Find subtitle
                                            if hdr2 == subtitle:   # If subtitle is also found              
                                                found_subtitle = True
                                                if found_subtitle == True:
                                                    for row in reader:
                                                        if not any(cell.strip() for cell in row):
                                                            break
                                                        else:
                                                            in_col = row
                                                            table.append(in_col)                 
                                                        
                                            
                                            elif not found_subtitle: # If subtitle was not found
                                                for row in reader: # Look for subtitle again
                                                    if len(row) >0: 
                                                        if row[0] == subtitle: # If subtitle is found
                                                            found_subtitle = True
                                                            if found_subtitle == True:
                                                                for row in reader:
                                                                    if not any(cell.strip() for cell in row):
                                                                        break
                                                                    else:
                                                                        in_col = row
                                                                        table.append(in_col)
        table = table_transpose(table)                                                                                    
        for z in range (0, len(table)):
                         empty_lst = []
                         new_dict = {str(table[z][0]): empty_lst}
                         lsts_of_dicts_to_send.append(new_dict)
                         for y in range (1, len(table[z])): # since [0] is the column title
                             element = float(table[z][y])
                             empty_lst.append(element)                                                            
                                                                                                
                                                                                                
        return lsts_of_dicts_to_send                                      


def calculations_on_dictionary_values (lst_of_dcts = [{},{}]): # A list of dictionaries
    for i in range(0, len(lst_of_dcts)):
        for vlst in lst_of_dcts[i].values():
            stat_lst = []
            calc = (vlst)
            add= sum(calc)
            mean= add/len(calc)
            average = {"mean": str(mean)}
            stat_lst.append(average)
            variance= sum((x- mean)**2 for x in calc) /(len(calc)-1)
            stdv= variance**0.5
            deviation = {"stdv": str(stdv)}
            stat_lst.append(deviation)
            p = len(calc)
            count = {"count" : p}
            stat_lst.append(str(count))
            calc.sort()
            mini = calc[0]
            minimum = {"min": str(mini)}
            stat_lst.append(minimum)
            maximum= calc[-1]
            max = {"max": str(maximum)}
            stat_lst.append(max)
            if p % 2 == 0.0: # If the number of entries is even
                c= p/2
                ind1= int(c-1.5) # index one
                ind2= int(c+1.5) # index two
                md = (calc[ind1] + calc[ind2])/2 # Average the two vvalues
                median = {"median": str(md)}
                stat_lst.append(median)
            
            elif p % 2 != 0.0:  # number of entries is odd
                c=p/2
                ind = int(c-0.5) # -0.5 instead of +0.5 because the indexing starts from 0
                md = calc[ind] # Get the middle value 
                median = {"median": str(md)}
                stat_lst.append(median)
            stats = {"stats": stat_lst}
            for r in range (0, len(vlst)): # Conver the values in dictionary list back to string
                vlst[r] = str(vlst[r])
                
        lst_of_dcts[i].update(stats)
    return 0 # This function does not return anything    

#example1 = column_to_dictionary_no_title("noheader.csv")
#print(example1) # Working as expected

# example2 = column_to_dictionary_one_title("testfile0.csv","Test")
# print(example2)   # Working as expected

# example2 = column_to_dictionary_one_title("testfile1.csv","March")
# print(example2)   # Working as well

example3 = column_to_dictionary_with_title_subtitle("testfile2.csv", "2026", "March")
print(example3)
print()
calculations_on_dictionary_values (example3)
print("Dictionary updated with calculations")
print(example3)
