#   The order of values in columns is getting re-organised when dumping to json

import csv
import json
import copy

                
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


                                           
def calculations_on_dictionary_values (lst_of_dcts = [{},{}]): # A list of dictionaries
    for i in range(0, len(lst_of_dcts)):
        for vlst in lst_of_dcts[i].values():
            stat_lst = []
            calc = copy.deepcopy(vlst)
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






#IMPORTANT: THIS FUNCTION REQUIRES A BLANK LINE BETWEEN THE TITLE AND SUBTITLE IN CERTAIN SITUATIONS
def get_dict_table_with_title_subtitle(datafile=str, title= str, subtitle= str): # Data file name, title name, subtitle name 
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
                                                                    
                                                            



yr_title = ["2026"] # Pass as list if calculations for more than 1 title required
months = ["Feb", "March"] # Same for the subtitle
fileout = "dicts from columns.json"
with open(fileout, "w",encoding="utf-8") as outfile:
    
    for a in range (0,len(yr_title)):
        yr_lst = []
        yr_dnry = {str(yr_title[0]): yr_lst}
        
        
        for b in range(0,len(months)):
            
            month_key = str(months[b])
            mnth_lst = []
            mnth_dnry = {month_key : mnth_lst} 
            days= get_dict_table_with_title_subtitle("testfile2.csv", yr_title[a], months[b]) 
            calculations_on_dictionary_values(days)
            mnth_lst.append(days) 
            yr_lst.append(mnth_dnry)
            
            
        json.dump(yr_dnry, outfile, indent=2)       
                
print("Data written to dicts from columns.json")

with open ("dicts from columns.json", 'r') as infile:
    indata = json.load(infile)


def indexify (lst=[]):
    to_send ={}
    for i in range (0, len(lst)):
        new = {str(lst[i]) : i}
        to_send.update(new)
    return to_send
       
mn = indexify (months)


# Included in case the number of days in each month are required
days_in_each_month = []
for d in range (0, len(months)):
    num_days = len(indata["2026"][mn.get(months[d])][months[d]][0])
    new_dict = {str(months[d]) : num_days}
    days_in_each_month.append(new_dict)


print()
print("data for Feb, day 3")
print(indata["2026"][mn.get("Feb")]['Feb'][0][2])
print()
print("stats for Feb, day 3") 
print(indata["2026"][mn.get("Feb")]['Feb'][0][2]["stats"]) # The main dictionary name, followed by the month, followed by the 0th index and then the day index and stats dictionaary.
                                                   # Caution will have to be exercised to reduce the day index by 1 to get to the correct day


                       
                    

