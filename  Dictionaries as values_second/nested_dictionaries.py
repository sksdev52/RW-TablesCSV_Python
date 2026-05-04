#   #Write output to json and access with text

import csv
import json
import os

                
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


                                           
def table_rows_mean_std_median(table=[]):
    # CAUTION: THE TABLE NEEDS TO BE TRANSPOSED BEFORE USING THE FUNCTIONS BELOW.
# Otherwise the calculations will be performed for horizontal rows instead of vertical columns.
# transpose() is called in the first line of the function below. Comment out if not required
    t = table_transpose(table) # Transpose table right at the begining
    to_send = []
    row_for_means=[]
    to_send.append(row_for_means)
    row_for_std=[]
    to_send .append(row_for_std)
    row_for_num_entries =[]
    to_send.append(row_for_num_entries)
    row_for_minimums=[]
    to_send.append(row_for_minimums) 
    row_for_maxs=[]
    to_send.append(row_for_maxs) 
    row_for_medians = []
    to_send.append(row_for_medians) 
    
    for l in range (len(t)):
        add= sum(t[l])
        mean= add/len(t[l])
        row_for_means.append(mean)
        variance= sum((x- mean)**2 for x in t[l]) /(len(t[l])-1)
        std= variance**0.5
        row_for_std.append(std)        
    
        t[l].sort() # Sor the row/column in ascending order
        p= len(t[l]) # Get the length of the list
        row_for_num_entries.append(p)
        min = t[l][0]
        row_for_minimums.append(min)
        max= t[l][-1]
        row_for_maxs.append(max)

        if p % 2 == 0.0: # If the number of entries is even
            c= p/2
            ind1= int(c-1.5) # index one
            ind2= int(c+1.5) # index two
            md = (t[l][ind1] + t[l][ind2])/2 # Average the two vvalues
            row_for_medians.append(md)
        
        elif p % 2 != 0.0:  # number of entries is odd
            c=p/2
            ind = int(c-0.5) # -0.5 instead of +0.5 because the indexing starts from 0
            md = t[l][ind] # Get the middle value 
            row_for_medians.append(md)              
       
    return to_send 

def convert_table_to_string(tbin=[]):
    for c in range (len(tbin)):
        for r in range (len (tbin[c])):
            tbin[c][r]= str(tbin[c][r])
    return tbin


def get_table_with_title_subtitle_header(datafile=str, title= str, subtitle= str, coltl =str): # Data file name, title name, subtitle name and column title
        ''' DO NOT insert another title, subtitile and column title within one title. For reference in the example
        below please do not insert title for year 2025, month and day within year 2026. The values for 2025 should 
        either be above the year 2026 or below it. Code is not designed to pick up such errors.
        Sometimes matching row[0] to string works, other times matching row to string works.
         If there is only one entry in the entire row match row to string.
         Exception in this case is title row where row[0] matches and using just row returns an empty list.
        Trying to match hdr2[0] gives list index out of range error
        #Trying to match hdr3 to coltl results in not entering the loop while hdr3[0] works.'''
        to_send=[]
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
                                                        hdr3 = next(reader) # Find the column title
                                                        if hdr3[0]  == coltl: # If the 1st element of header 3 is column title
                                                            for row in reader:
                                                                if not any(cell.strip() for cell in row):
                                                                    break
                                                                else:
                                                                    for e in range (len(row)):
                                                                        row[e]= float(row[e])
                                                                    to_send.append(row)
                                                    
                                                
                                                elif not found_subtitle: # If subtitle was not found                                                   
                                                    for row in reader: # Look for subtitle again
                                                        if len(row) >0: 
                                                            if row[0] == subtitle: # If subtitle is found
                                                                found_subtitle = True
                                                                if found_subtitle == True:
                                                                    hdr3 = next(reader) # Start looking for column title
                                                                    if hdr3[0] == coltl:
                                                                        for row in reader:
                                                                                if not any(cell.strip() for cell in row):
                                                                                    break
                                                                                else:
                                                                                    for e in range (len(row)):
                                                                                        row[e]= float(row[e])
                                                                                    to_send.append(row)
                                                                                                   
                                                                    else: 
                                                                        not found_coltitle
                                                                        for row in reader: # Look for subtitle again
                                                                            if len(row) >0: 
                                                                                if row[0] == coltl:   
                                                                                    if not any(cell.strip() for cell in row):
                                                                                        break
                                                                                    else:
                                                                                        for e in range (len(row)):
                                                                                            row[e]= float(row[e])
                                                                                        to_send.append(row)
                            
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
                                                        found_coltitle = False
                                                        hdr3 = next(reader) # Find the column title
                                                        if hdr3[0] == coltl:
                                                            found_coltitle = True                 
                                                            
                                                
                                                elif not found_subtitle: # If subtitle was not found
                                                     for row in reader: # Look for subtitle again
                                                        if len(row) >0: 
                                                            if row[0] == subtitle: # If subtitle is found
                                                                found_subtitle = True
                                                                if found_subtitle == True:
                                                                    found_coltitle = False
                                                                    hdr3 = next(reader) # Start looking for column title
                                                                    if hdr3[0] == coltl:
                                                                        found_coltitle = True
                                                                        if found_coltitle == True: # If found column title, extract data
                                                                            for row in reader:
                                                                                if not any(cell.strip() for cell in row):
                                                                                    break
                                                                                else:
                                                                                    for e in range (len(row)):
                                                                                        row[e]= float(row[e])
                                                                                    to_send.append(row)
                                                                                                
                                                                    else: 
                                                                        not found_coltitle
                                                                        for row in reader: # Look for subtitle again
                                                                            if len(row) >0: 
                                                                                if row[0] == coltl:   
                                                                                    found_coltitle = True
                                                                                    if found_coltitle == True:
                                                                                        for row in reader:
                                                                                            if not any(cell.strip() for cell in row):
                                                                                                break
                                                                                            else:
                                                                                                for e in range (len(row)):
                                                                                                    row[e]= float(row[e])
                                                                                                to_send.append(row)
                                                                                                
                                                                                                
                                    
        
        return to_send                                      
                                                                    
                                                            
                                                   



yr_title = ["2026"] # Pass as list if calculations for more than 1 title required
months = ["Feb", "March"] # Same for the subtitle

w_day =["W1","W2","W3","W4", "W5"]
col_to_add = ["mean", "stdv", "count", "min", "max", "median"]

    

fileout = "nested_dictionaries.json"
with open(fileout, "w",encoding="utf-8") as outfile:
    
    for a in range (0,len(yr_title)):
        yr_lst = []
        yr_dnry = {str(yr_title[0]): yr_lst}
        #yr_dnry = {str(yr_title[0]): None} # See below why this is not used
        
        for b in range(0,len(months)):
            month_key = str(months[b])
            mnth_dnry = {month_key : None} # null will appear as the first value in the dictionary. Needed for initialiseing the dictionary
            #yr_dnry.update(mnth_dnry) # If updated here then the month dictionary without being updated by day dictionary is accessed
            tbl_in= get_table_with_title_subtitle_header("testfile2.csv", yr_title[a], months[b], "W1") # "W1" is the column title
            calc = table_rows_mean_std_median(tbl_in)
            calc = convert_table_to_string(calc) 
                
            for c in range (0, len(calc[0])):
                
                stat_lst= []
                for d in range (0, len(col_to_add)):
                    stats ={(col_to_add[d]):  calc[d][c]}
                    stat_lst.append(stats)
                
                
                day_key = str(w_day[c])
                mnth_dnry[day_key] =stat_lst
                # Not deleting 'None' value.            
            yr_lst.append(mnth_dnry)
            #yr_dnry.update(mnth_dnry) # Only the first month is included and not the subsequent one
            
                
            
    json.dump(yr_dnry, outfile, indent=2)       
                
    
print("Data written nested_dictionaries.json")

with open ("nested_dictionaries.json", 'r') as infile:
    indata = json.load(infile)
print(indata["2026"][1]["W3"]) # Here [1] is month March following which inner dictionaries which can be accessed by text


                       
                    

