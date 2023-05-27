import random

def handle_response(message) -> str: 
    #this makes it so user message can be in lower case and it will read
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey there!'

    if p_message == 'roll':
        return f'You rolled a {str(random.randint(1,6))}!'

    if p_message == '!help':
        #the `` creates a code block on discord
        return '`This is a message you can modify`'

    #return "I don't know what you said" if you want it to respond this way when one of the above isn't chosen