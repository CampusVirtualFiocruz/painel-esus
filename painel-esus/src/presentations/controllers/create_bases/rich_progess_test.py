def add_log(log, text, update=True):
    if update and len(log) > 0:
        log.pop()
    log.append(text)
    
    return log

def test_add_log():
    log = []
    text = [
        [('1'),('2'),('3')]
    ]
    t = add_log(log, text)
    text = [[("1"), ("-2"), ("3")]]
    t = add_log(log, text)
    print(t)
    text = [[("2"), ("2"), ("3")]]
    t = add_log(log, text, False)
    print(t)
