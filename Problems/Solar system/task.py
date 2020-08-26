with open('planets.txt', 'w', encoding='utf-8') as file:
    for word in ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'):
        file.write(word + '\n')
