import pyfiglet, requests, termcolor, random

print(termcolor.colored(pyfiglet.Figlet().renderText('Dad Jokinator'),'red'))
print(termcolor.colored('==================================================================\n','green'))
search_term = input('what would you like to hear a joke about? ')
response = requests.get('https://icanhazdadjoke.com/search',
    headers = {'Accept': 'application/json'},
    params = {'term' : search_term}
    )
jokes_returned = response.json()

if jokes_returned["total_jokes"] :
    print(f'You got back {jokes_returned["total_jokes"]} jokes, here is one of them: ')
    print(random.choice(jokes_returned['results'])['joke'])
    # print(random.choice(tuple((jk['joke'] for jk in jokes_returned['results']))))
else :
    print(f'No jokes were found about {search_term}, but here is one we thought you might like: ')
    response = requests.get('https://icanhazdadjoke.com/',
        headers = {'Accept': 'text/plain'}
        )
    print(response.text)
