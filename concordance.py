#!/usr/bin/env python3
import sys

#Function to populate lists from files
def populate_arr(file_wanted):
    the_file = open(sys.argv[file_wanted], 'r')
    to_populate = []
    if the_file == None:
        sys.exit(1)
    to_populate = list(the_file)
    return to_populate

#Function to find "-e" argument
def find_e():
    for i in range(0, len(sys.argv)):
        if(sys.argv[i] == "-e"):
            return i;
    return -1



#Function to find if word is an exclusion word or not
def is_exclusion(word, exclusion):
    for i in range(0, len(exclusion)):
        if(word.lower() == exclusion[i].lower()):
            return True
    return False

#Function to find if word is a repeated word in keywords list or not
def is_repeat(word, keywords):
    for i in range(0, len(keywords)):
        if(word.lower() == keywords[i].lower()):
            return True
    return False
    
#Function to populate lists from files
def populate_arr(file_wanted):
    the_file = open(sys.argv[file_wanted], 'r')
    to_populate = []
    if the_file == None:
        sys.exit(1)
    to_populate = list(the_file)
    return to_populate


#Function to find words that should be keywords
def find_keywords(lines, exclusion):
    keywords = []

    #Go through lines
    for i in range(0, len(lines)):
        line_list = (lines[i]).split()

        #Go through words in each line
        for j in range(0, len(line_list)):
            if(is_exclusion(line_list[j], exclusion)):
                continue
            elif(is_repeat(line_list[j], keywords)):
                continue
            else:
                keywords.append(line_list[j])
    return keywords

#Function that compares two strings, if string one should come after string two, return 1, if not return 0
def compare(str_one, str_two):
    length = len(str_one)
    if(len(str_two) < len(str_one)):
        length = len(str_two)
    for i in range(0, length):
        if(ord(str_one[i].lower()) > ord(str_two[i].lower())):
            return 1
        elif(ord(str_one[i].lower()) < ord(str_two[i].lower())):
            return 0
        elif(i == length-1):
            if(len(str_one) > len(str_two)):
                return 1
            else:
                return 0

#Function that selection sorts keywords
def sort_keywords(keywords):
    for i in range(0, len(keywords)):
        smallest_index = i
        for j in range(i+1, len(keywords)):
            if(compare(keywords[smallest_index], keywords[j]) == 1):
                smallest_index = j
        keywords[i], keywords[smallest_index] = keywords[smallest_index], keywords[i]
    return keywords

#Function that returns the number of times a word is in a line
def find(keyword, line):
    times_in_line = 0
    list_line = line.split()
    for i in range(0, len(list_line)):
        if(keyword.lower() == list_line[i].lower()):
            times_in_line = times_in_line + 1
    return times_in_line

#Function that returns the amount of spaces that should be printed
def create_spaces(max_len, word):
    to_return = ''
    for i in range(0, (max_len+2-len(word))):
        to_return = to_return + ' '
    return to_return


#Function that prints out lines
def printing(words, lines):
    max_len = 0
    for i in range(0, len(words)):
        if(len(words[i]) > max_len):
            max_len = len(words[i])

    #Check for keyword in each line
    for i in range(0, len(words)):

        #Go through each lines
        for j in range(0, len(lines)):
            if(find(words[i], lines[j]) > 0):
                base = words[i].upper() + create_spaces(max_len, words[i]) +str(lines[j]) + " (" + str(j+1)
                if(find(words[i], lines[j]) == 1):
                    print (base + ")")
                elif(find(words[i], lines[j]) > 1):
                    print (base + "*)")


#main function
def main():
    e_location = find_e()
    exclusion = []
    lines = []
    keywords = []

    #If exception file exists
    if(e_location != -1):
        exclusion = populate_arr(e_location+1)
       # exclusion = take_off_newline(exclusion)
        #Take off newline
        for i in range(0, len(exclusion)):
            if(exclusion[i][len(exclusion[i])-1] == '\n'):
                into_list = list(exclusion[i])
                revised_list = into_list[0:(len(into_list)-1)]
                new_word = ''.join(revised_list)
                exclusion[i] = new_word

    #where input file is, depending on -e placement/existence
    where_is_input = 0
    if(e_location == -1):
        where_is_input = 1
    elif(e_location == 1):
        where_is_input = 3
    else:
        where_is_input = 1
    lines = populate_arr(where_is_input)

    #Take off newline
    for i in range(0, len(lines)):
        if(lines[i][len(lines[i])-1] == '\n'):
            into_list = list(lines[i])
            revised_list = list(into_list[0:(len(into_list)-1)])
            new_line = ''.join(revised_list)
            lines[i] = new_line
    keywords = find_keywords(lines, exclusion)
    sort = sort_keywords(keywords)
    printing(sort, lines)

if __name__ == "__main__":
    main()
