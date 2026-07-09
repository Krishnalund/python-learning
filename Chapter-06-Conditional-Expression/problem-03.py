# A spam comment is defined as a text containing following keywords: “Make a lot of
# money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.
text='''
    Make a lot of money by discovering new opportunities 
    and improving your skills. Buy now to take advantage 
    of this limited-time offer. Subscribe this newsletter 
    to receive exclusive updates and special deals. Click 
    this link to learn more and get started today.
'''
text=text.lower()
if('make a lot of money' in text or 'buy now' in text or 'subscribe this' in text
    or 'click this' in text ):
    print('Spam')
else:
    print('Not spam')