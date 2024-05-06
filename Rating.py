Rating = {
    'Naruto': {
        'Genre': 'Funny',
        'Rating': 5,
    },
    'Boruto': {
        'Genre': 'Funny',
        'Rating': 4,
    },
    'Jujutsu Kaisen': {
        'Genre': 'Action',
        'Rating': 7,
    },
    'Death Note': {
        'Genre': 'Thriller',
        'Rating': 8,
    },
    'Your Name': {
        'Genre': 'Romantic',
        'Rating': 9,
    }
}

choice = str(input("Enter the Genre: "))
for key,value in Rating.items():
    if value['Genre'] == choice:
        print(key)
        
    # choice = str(input("Enter the Genre: "))    
    # if choice == 'Funny' :
        
         
            