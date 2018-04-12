#This program illustrates the combination of the encoder and the decoder program.
#The user can decide whether they want to encode or decode.
#Name: Ramansh Sharma ; Date: 1/18/17


def main():                                                     #main function: This function contains all other functions. A raw input is taken and one of the other functions is called.
    t=raw_input("\nPress 'a' for encode or 'b' to decode: ")
    if t=='a' or t=='A':
        encoder()                                               #Calls the encoder function.
    elif t=='b' or t=='B':
        decoder()                                               #Calls the decoder function.

def decoder():                                                  #Encoder function.
    import string                                               #The string module is imported.
    x=raw_input("\nEnter your numbers to see their string: ") #The sequence of numbers is taken as a raw input.
    key=input("\nEnter your key: ")                               #The key is taken as a input since it is supposed to be subtracted later and hence it needs to be a number, rather than a string.
            
    
    if 1>key or 94<key:
        print '\ninvalid'
        decoder()
        #The key cannot be smaller than 1 or greater than 94. If the input is invalid according to this inequality, the user has to start back from the decoder function.
        
    message=""                              #Accumulative variable that takes all the computations and prints it in the end.
    for char in string.split(x):            #Splits all the separate numbers in the raw input into separate elements in a list.
        r=eval(char)                        #Evaluates all the elements in the list into a number rather than a string so that the numbers can be worked upon mathematical calculations later on.
        message=message+chr(r-key)          #Subtracts the key from the number and placed into the accumulative variable 'message'.
    print '\nThe decoded message is:\n\n', message

    sure=raw_input("\nWould you like to encode, if so press a. If you want to decode, press b. If you would like to exit, press anything else: ")

    if sure=='A' or sure=='a':
        encoder()
    elif sure=='B' or sure=='b':
        decoder()
    else:
        print "Goodbye user!"
    #The 'sure' raw input including all these if else statements asks the user whether they want to exit the program, chose to encode or decode.
            



def encoder():
    x=raw_input("\nInput your string to encode it: ")    #The string message that needs to be encoded.
    y=0
    f=input("\nEnter your shift key: ")                       #Shift key that will be added to the ASCII numbers of the string (and later subtracted from the numbers in the decoder function).
    if 1>f or 94<f:                         
        print'\ninvalid'
        encoder()
    #Ensures that the key is not less than 1 or more than 94. If it is invalid, the user has to start back from the encoder program.
                
    print "\nThe encoded message is:\n"
    for i in range(len(x)):                 #Loop that happens as many times as there are characters in the string.
        print int(ord(x[y]))+f,             #Takes the number of the corresponding letter, and adds the key.
        y=y+1

    sure=raw_input("\n\nWould you like to encode, if so press a. If you want to decode, press b. If you would like to exit, press anything else: ")

    if sure=='A' or sure=='a':
        encoder()
    elif sure=='B' or sure=='b':
        decoder()
    else:
        print "\nGoodbye user!"
#Asks the user whether they want to exit the program, go to encode or decode.




main()
    












    
    
