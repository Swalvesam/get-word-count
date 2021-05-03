
#import file add to variable
file_with_words = open("twain.txt")
#def funtion word_count:
def word_count(file):
   #make dictionary and seperate by words
    words = []
    for line in file:
        line = line.rstrip()
        line_words = line.split()
        words.extend(line_words)
    #print(words)

    #create counter dictionary
    word_count = {}

    #iterate over the text
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
        
    #return word_counts
    print(word_count)
    return word_count

#call function to print word counts

word_count(file_with_words)


