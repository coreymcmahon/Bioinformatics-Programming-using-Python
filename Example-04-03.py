def echo1():
    """Prompt the user for a string, "echo" it and return it"""
    line = input('Say something:')
    print('You said ',line)
    return line

def recording_echo():
    """Echo the user's inut until it equals 'bye', then return a list of all the inputs received"""
    lst = []
    entry = echo1()
    while entry != 'bye':
        lst.append(entry)
        entry = echo1()
    return lst
