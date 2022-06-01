def make_albulm(artist_name,albulm_title,number_songs=None):
    """Return diction of artist and albulm"""
    make_albulm = {'Artist Name': artist_name,'Albulm Title': albulm_title}
    if number_songs:
        make_albulm['songs'] = number_songs
    return make_albulm

while True:
    print("\nPlease provide your favorite artist and albulm title")
    print("(Type 'q' in the prompt to quit)")

    name =  input("\n Please provide an artist's name: ")
    if name == 'q':
        break

    title = input("\nPlease provide a title for your favorite albulm: ")
    if title == 'q':
        break

    albulm = make_albulm(artist_name=name,albulm_title=title)
    print (albulm)