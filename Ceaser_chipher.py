
# coding: utf-8

# In[91]:


import string 
class Caesar(object):
    
    key=0
    out_str=''
    
    def __init__(self):
        pass
    
    #To Calculate and return Ascii values of the words
    def num_values(self,words):
        self.words=words
        return list(map(ord,self.words))
    
    # TO return a encrypted/decrypted message of the given in_str(input string) in out_str, mode=0 to encrypt 
    # mode=1 to decrypt
    def en_dec(self,in_str,key=0,mode=0):
        self.mode=mode
        self.in_str=in_str
        
        # check invalid mode
        if self.mode not in [0,1]:
            return
        elif self.mode==0:
            self.key=key
        elif self.mode==1:
            self.key=(26-key)
        
        #to get ascii values as a list in self.val
        self.val=self.num_values(in_str)
        for letter_val in self.val:
            if letter_val in list(map(ord,string.ascii_letters)):
                #to return wrap up value of the letter
                                   
                self.out_str+=chr(self.wrap_letter(letter_val,self.key))
            else: 
                #to return non-alphabates intact
                self.out_str+= chr(letter_val)
        return self.out_str
         
    def wrap_letter(self,val,key):
        self.val=val
        self.key=key
        # (val-base_value) to shift to relative to 0 then add key them mod by 26 to wrap it
        # around then projecting back to its ascii range 
        if val in range(97,123):
                        
            return ((((self.val-97)+self.key)%26)+97)
        if val in range(65,91):
            
            return ((((self.val-65)+self.key)%26)+65)                          
                                                            
                                  
        


# In[90]:


if __name__=='__main__':
    contd=True
    while contd:
        print("Welcome to Caesar Cipher. I'm Caesar I'll help you to encode/decode your message.\n")
        c=Caesar()
        while True:
            try:
            
                message=str(input("Please type the message you want to convert!\t"))
                break
            except :
                print ('Please Enter correct input\n')
                continue
            
        while True:
            try:
                key=int(input("please enter your secret key[0-26]\t"))
                if key<0:
                    key*=-1
                break
            except :
                print ('Please Enter correct input\n')
                continue
            
        while True:
            try:
                mode=str(input("Do You want to encrypt or decrypt your message? e/d\t"))
            
                if mode=='e':
                    outcome=c.en_dec(message,key,0)
                    print ('\nYour ENCRYPTED Message is "{x}"'.format(x=outcome))
                    break
                elif mode=='d':
                    outcome=c.en_dec(message,key,1)
                    print ('\nYour DECRYPTED Message is "{x}"'.format(x=outcome))
                    break
                else:
                    print ('Please Enter correct input e/d\n')
                    continue
            except :
                print ('Please Enter correct input\n')
                continue
        while True:
            try:
                input_start=input("Do you want to go for another round? y/n")
                if input_start=='y':
                    break
                elif input_start=='n':
                    contd=False
                    break
            except:
                print("Enter correct input")
                continue

