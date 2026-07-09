# Write a program to find out whether a given post is talking about “Harry” or not.

post_text=input('Enter a post: ').lower()
if 'harry' in post_text:
    print('Post is talking about Harry')
else:
    print('Post is not talking about Harry')