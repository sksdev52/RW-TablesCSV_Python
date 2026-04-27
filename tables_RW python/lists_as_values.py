# Error Prone

import csv
from csv import DictReader
from typing import List, Dict
import json
import os

def get_matrix_nosubheader(datafile=str): # Reads a table with no title, sub-title or header
# While using the function below make sure there are no empty rows above the data table to extract
# Just a table starting from the 1st row and 1st column
    with open(datafile, mode ='r', encoding="utf8") as infile: # Open csv file dictread in read mode
        reader = csv.reader(infile, delimiter=',') # check delimiters in csv file to make sure they match the delimiter argument here
        to_send=[]
        
        for row in reader: # This will extract each data row one by one
                if not any(cell.strip() for cell in row):
                    break
                else:
                    for e in range (len(row)):
                        row[e]= float(row[e])
                    to_send.append(row)  
                         
    #print ("Total number of rows: %d" % (reader.line_num))#csvreader.line_num counts and returns the number of rows iterated.
    return to_send
                
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

def get_table_single_title(datafile=str,title =str):
    to_send=[]
    with open(datafile, mode ='r', encoding="utf8") as infile: 
        reader = csv.reader(infile, delimiter=',')
        found_title = False
        for row in reader:
            if len(row) >0:
                if row[0] == title:
                    found_title = True
                    for row in reader:
                        if not any(cell.strip() for cell in row):
                            break
                        else:
                            for e in range (len(row)):
                                row[e]= float(row[e])
                            to_send.append(row)            


                for row in reader:
                    if not found_title:
                        if len(row) >0: # To avoid an error in case of a blank row
                            if row[0] == title:
                                #print("Title: ",row)
                                #found_title = True
                                for row in reader:
                                    if not any(cell.strip() for cell in row):
                                        break
                                    else:
                                        for e in range (len(row)):
                                            row[e]= float(row[e])
                                        to_send.append(row)
                                            
                                                
                                                
                                return to_send
                                        
def get_table_with_subtitle_column_title(datafile=str, subtitle= str, coltl =str): # Data file name, subtitle name and column title
    to_send=[]
    with open(datafile, mode ='r', encoding="utf8") as infile: # Open csv file dictread in read mode
        reader = csv.reader(infile, delimiter=',')
        found_subtitle = False
        for row in reader:
            if len(row) >0: # To skip blank row
                if row[0] == subtitle:
                    print("Subtitle Found", row[0])
                    found_subtitle = True
                    if found_subtitle == True:
                        hdr3 = next(reader) # Find the column title
                        if hdr3[0]  == coltl: # If the 1st element of header 3 is column title
                            #print("Column Title", hdr3[0])
                            for row in reader:
                                if not any(cell.strip() for cell in row):
                                    break
                                else:
                                    for e in range (len(row)):
                                        row[e]= float(row[e])
                                    to_send.append(row)
                                                     
                else :                
                    found_subtitle == False
                    hdr1a = next(reader) # Find subtitle
                    if hdr1a == subtitle:   # If subtitle is also found
                        #print("Subtitle Found", hdr1a)
                        found_subtitle = True
                        if found_subtitle == True:
                            hdr3 = next(reader) # Find the column title
                            if hdr3[0]  == coltl: # If the 1st element of header 3 is column title
                                #print("Column Title", hdr3[0])
                                for row in reader:
                                    if not any(cell.strip() for cell in row):
                                        break
                                    else:
                                        for e in range (len(row)):
                                            row[e]= float(row[e])
                                        to_send.append(row)
                                        
        return to_send


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
                                                                    
                                                            
                                                   


# rcd2 = get_table_single_title ("testfile1.csv", "Data")
# print(rcd2)     
# received0 =  get_matrix_nosubheader("testfile0.csv")
# for l in range (len(received0)):
#     print(received0[l])
# print()

# getmsm = table_rows_mean_std_median(received0) # Calculate mean, std and median
# print("Mean: ", getmsm[0])
# print("Stdv: ", getmsm[1])
# print("Number of entries", getmsm[2])
# print("Lowest value", getmsm[3])
# print ("Highest value", getmsm[4])
# print("Median: ", getmsm[5])

#sbtcolt = get_table_with_subtitle_column_title("testfile1.csv", "March", "W1") # The location of title is in different rows in testfile1 nad testfile2
#print(sbtcolt)

# revd1= get_table_with_title_subtitle_header("testfile1.csv", "2026", "March", "W1")# Hence checking to make sure they both work          
# print("Received", revd1)

# singlet= get_table_single_title("testfile1.csv","Data")
# print(singlet)

yr_title = ["2026"] # Pass as list if calculations for more than 1 title required
months = ["Feb", "March"] # Same for the subtitle
workday =["Stats", "W1","W2","W3","W4", "W5"]
w_day =["W1","W2","W3","W4", "W5"]
col_to_add = ["mean", "stdv", "count", "min", "max", "median"]
fileout = "nested_values _indictionaries.json"

with open(fileout, "w",encoding="utf-8") as outfile:
    
    
    for a in range (0,len(yr_title)):
            yrlst= []
            hdr101 = str(yr_title[a])
            json_yr= {hdr101: yrlst}
            
            for b in range(0,len(months)):
                mnlst= []
                month = str(months[b])
                json_mnth = {month: mnlst}
                yrlst.append(json_mnth)
                
                tbl_in= get_table_with_title_subtitle_header("testfile2.csv", yr_title[a], months[b], "W1") # "W1" is the column title
                calc = table_rows_mean_std_median(tbl_in)
                calc = convert_table_to_string(calc) # To save memory if needed or comment out
                
                for c in range (0, len(calc[0])):
                    daylst= []
                    json_wday ={str(w_day[c]): daylst}
                    mnlst.append(json_wday)
                    
                    stlst= []
                    for d in range (0, len(w_day)):
                        
                        stats ={str(col_to_add[d]):  calc[d][c]}
                        stlst.append(stats)
                        daylst.append(stats)
    
                           
            json.dump(json_yr, outfile, indent =2) # This indentation is important
                    
                        
                    
              
with open ("nested_values _indictionaries.json", 'r') as infile:
    indata = json.load(infile)
print("Data file opened")

print(indata["2026"][1]["March"][1]) # 2026 is the dictionary name, [] is the month, "March" is the dictionary in list and the next [] is the day in dictionary
       # In year '2026' look at the [1st month which is March in this case]["In March look at day][1 which is day 2]
                



