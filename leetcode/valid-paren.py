def validParentheses(s):
    stack = []      
    open = ['(','[','{']
    close = [')',']','}']

    for p in s:
        if p in close and stack == []:
            return False
        elif p in open:
            stack.append(p)
        elif p in close and stack[-1] == open[close.index(p)]:
            stack.pop()
        else:
            return False

    if stack == []:
        return True
    else:
        return False

# an attempt to get it faster
def valid2(s):
    stack = []      
    open = ['(','[','{']
    close = [')',']','}']
    edge = []

    map(lambda x: edge.append(False) if x in close and stack == [] else stack.append(x) if x in open else stack.pop() if x in close and stack[-1] == open[close.index(x)] else edge.append(False), list(s))

    return True if stack == [] and edge == [] else False

def tests():
    print ('1:  Pass | ' + s) if validParentheses(s :='()') else print('1:  Fail | ' + s)
    print ('2:  Pass | ' + s) if validParentheses(s :='(()()()()()()()())') else print('2:  Fail | ' + s)
    print ('3:  Pass | ' + s) if validParentheses(s :='[(()((((()))))())]') else print('3:  Fail | ' + s)
    print ('4:  Pass | ' + s) if validParentheses(s :='([][][][[[[]]]])') else print('4:  Fail | ' + s)
    print ('5:  Pass | ' + s) if validParentheses(s :='({{}})') else print('5:  Fail | ' + s)
    print ('6:  Pass | ' + s) if not validParentheses(s :='(') else print('6: Fail | ' + s)
    print ('7:  Pass | ' + s) if not validParentheses(s :='((((((())') else print('7: Fail | ' + s)
    print ('8:  Pass | ' + s) if not validParentheses(s :='([[[[[)') else print('8: Fail | ' + s)
    print ('9:  Pass | ' + s) if not validParentheses(s :='(}}}}}}}}})') else print('9: Fail | ' + s)
    print ('10: Pass | ' + s) if not validParentheses(s :='([{))') else print('10: Fail | ' + s)
    print ('11: Pass | ' + s) if not validParentheses(s :=')))))))))))))))') else print('11: Fail | ' + s)

    print ('12: Pass | ' + s) if valid2(s :='()') else print('12: Fail | ' + s)
    print ('13: Pass | ' + s) if valid2(s :='(()()()()()()()())') else print('13: Fail | ' + s)
    print ('14: Pass | ' + s) if valid2(s :='[(()((((()))))())]') else print('14: Fail | ' + s)
    print ('15: Pass | ' + s) if valid2(s :='([][][][[[[]]]])') else print('15: Fail | ' + s)
    print ('16: Pass | ' + s) if valid2(s :='({{}})') else print('16: Fail | ' + s)
    print ('17: Pass | ' + s) if not valid2(s :='(') else print('17: Fail | ' + s)
    print ('18: Pass | ' + s) if not valid2(s :='((((((())') else print('18: Fail | ' + s)
    print ('19: Pass | ' + s) if not valid2(s :='([[[[[)') else print('19: Fail | ' + s)
    print ('20: Pass | ' + s) if not valid2(s :='(}}}}}}}}})') else print('20: Fail | ' + s)
    print ('21: Pass | ' + s) if not valid2(s :='([{))') else print('21: Fail | ' + s)
    print ('22: Pass | ' + s) if not valid2(s :=')))))))))))))))') else print('22: Fail | ' + s)
    



def main():
    tests()


if __name__ == '__main__':
    main()