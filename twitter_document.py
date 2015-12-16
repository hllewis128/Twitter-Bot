import tweepy

# We're going to treat this as a wrapper for the document class
# Because of the setup we're going to have to make sure to enclose the work
# done with this object with a try/catch
class TwitterDocument():


    # creates blank variable for self.doc and tells the instance of twitter_document 
    #(e.g. twit_test in twitter_bot_basic) to use the value passed in from the parameter path
    def __init__(self, path):
        self.doc = None
        self.doc_path = path

    # creates function that stores stream (connection between file and bot, for example) 
    # for open file in self.doc; speficies that it's a stream for reading the file only
    def open_File(self):
        self.doc = open(self.doc_path, 'r')

    # closes the file if there is an open path to one
    def close_File(self):
        if not (self.doc is None):
            self.doc.close

    # Makes it possible to iterate this class (twitter_document) in for loop in twitter_bot_basic
    def __iter__(self):
        return self

    # This function returns the next line in the form of premade array of tweets
    # Makes previously defined function possible
    # This needs to be changed to account for blank lines
    def next(self):
        next_line = self.get_Next_Line_In_Tweets()
        if not next_line:
            raise StopIteration()
        else:
            return next_line 


    # When calling this function surround with a try catch that
    # will close the file if it fails
    def get_Next_Line(self):
        return self.doc.readline()

    # Flesh this out and figure what this should return
    # When calling this function surround with a try catch that
    # will close the file if it fails
    def search_Text(self, search_text):
        return search_text

    # Returns an array with the current line broken into 140 character elements
    # in an array
    #
    # When calling this function surround with a try catch that will close the file if it fails
    def get_Next_Line_In_Tweets(self):
        line = self.get_Next_Line().rstrip('\r\n')
        last_space = 0
        line_array = []

        if len(line) > 140:
            while (last_space < len(line)):
                if (last_space + 140) < len(line):
                    first_char_in_slice = last_space
                    last_space = line.rfind(" ", first_char_in_slice, first_char_in_slice + 140)
                    #Had to adjust since slice takes end-1 for end of string
                    last_space += 1 
                    line_array.append(line[first_char_in_slice:last_space])
                else:
                    line_array.append(line[last_space:len(line)])
                    #using last space to break out of loop
                    last_space = len(line)
        elif line.strip():
            line_array.append(line)
        return line_array

