import enquiries

options = ['thing 1', 'thing 2', 'thing 3']
choice = enquiries.choose('Choose one of these options: ', options)

if enquiries.confirm('Do you want to write something?'):
    text = enquiries.freetext('Write something interesting: ')
    print(text)
