def get_formatted_name(first_name,last_name):
    full_name=f"{first_name} {last_name}"
    return full_name.title()
#This is an infinite loop
while True:
    print('\nPlease enter your name:')
    print("(enter 'quit'to end program)")
    f_name=input('first name: ')
    if f_name=='quit':
        break
    l_name=input('last name: ')
    if l_name=='quit':
        break
    formatted_name=get_formatted_name(f_name,l_name)
    print(f"\nHello, {formatted_name}!")
def make_album(artist_name,album_title):
    album={'artist':artist_name,'album':album_title}
    return album
while True:
    print("\nPlease enter your song details")
    print("Enter 'quit'to end program")
    alist=input('artist: ')
    if alist=='quit':
        break
    blist=input('album: ')
    if blist=='quit':
        break
    album=make_album(alist,blist)
    print(album)
