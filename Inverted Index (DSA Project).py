#!/usr/bin/env python
# coding: utf-8

# In[3]:

###-------------------------------------------- GROUP-19 -------------------------------------------------------###

##### This is Document Level Inverted Index (Record-Level Algorithm) #####

#import string module, to be use to remove the punctuations from documents
import string

#initialized empty dictionary where words and position/s will be saved
word_dic = {}

#create a function that accepts a filename, where word_dic is updated
def update_word_dic(filename):
    #open input file
    f_input = open(filename+".txt", 'r')

    #loop through each line on the txt file
    index_counter = 0
    for line in f_input.readlines():
        #remove all punctuations from the line
        line = line.translate(str.maketrans('', '', string.punctuation))
        #remove the next line or "\n" from the line
        line = line.replace("\n", "")
        #if the line is not empty split the line by words
        if line != "":
            word_array = line.split()
            #loop through the each words in the line and get its lowercase
            for word in word_array:
                word_lowered = word.lower()
                #if the word_lowered is already saved in the word_dic,
                if word_lowered in word_dic.keys():
                    #get the dictionary of filename and listof indexes on the word_dic using the word_lowered
                    #and check if the filename is found in there
                    doc_index_dic = word_dic[word_lowered]
                    if filename in doc_index_dic.keys():
                        #add index_counter to the value of the filename in the dictionary and assign the
                        #updated dictionary to the key word_lowered on word_dic
                        doc_index_dic[filename].append(index_counter)
                        word_dic[word_lowered] = doc_index_dic
                    else:
                        #otherwise, add the filename with value equal to the list where the index_counter is saved, to the dictionary
                        #of filename and index and assign the updated dictionary to the key word_lowered on word_dic
                        doc_index_dic[filename] = [index_counter]
                        word_dic[word_lowered] = doc_index_dic
                #if the word_lowered is not yet included in the word_dic add the filename with value equal to the list where the index_counter is saved
                else:
                    word_dic[word_lowered] = {filename:[index_counter]}

                #increment the index_counter
                index_counter+=1
    #close the input file
    f_input.close()



#----------------- Driver Code -------------------#

    #to get the inverted index from doc1 and doc2, call the function update_word_dic for each doc

#filename1 = "doc1"
#filename2 = "doc2"
#filename3 = "doc3"
#update_word_dic(filename1)
#update_word_dic(filename2)
#update_word_dic(filename3)

    #print each word from word_dic and its document position and the number of occurrence

#for word in word_dic:
#    print(word, end=" ")
#    doc_count_dic = word_dic[word]
#    output_str = ""
#    for doc in doc_count_dic:
#        output_str += "("+doc+", "+str(len(doc_count_dic[doc]))+", "+str(doc_count_dic[doc])+"); "

    #    output_str[:-2] will not include to last 2 character of the string which is semicolon and a space

#    print(output_str[:-2])



