from urllib.request import *

def get_attributes(n):
    """ returns dictionary containing attributes supplied from pokeapi.co
        inputs: Pokedex number of Pokemon
    """
    
    assert(1 <= n <= 721)
    
    url = "http://pokeapi.co/api/v2/pokemon/" + str(n) + "/"
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7'
    with urlopen(Request(url, headers={'User-Agent': user_agent})) as f:
            s = f.read()
            
    s = str(s)[2:-1]

    # replace words Python doesn't use
    s = s.replace('true', 'True')
    s = s.replace('false', 'False')
    s = s.replace('null', 'None')
    
    return eval(s)


