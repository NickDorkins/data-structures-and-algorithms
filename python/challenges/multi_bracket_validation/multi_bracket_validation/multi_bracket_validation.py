
def multi_bracket_validation(input):
    char_list = list(input)
    if len(char_list) == 0:
        return False
    
    mutable_list = []
    brackets = "()[]{}"
    iterator = []

    for character in char_list:
        # print(character)
        if character in list(brackets):
            mutable_list.append(character)
            iterator.append(character)
            print(mutable_list)

        else:
    #         char_list.remove(character)
            continue
        
        if len(mutable_list) == 0:
            return False

       

        print(f"ITERATOR {iterator}")

        for bracket in iterator:
            print(f"Iterator in first for loop {iterator}")
            if bracket == '(':
                for comp in mutable_list:
                    if comp == ')':
                        mutable_list.remove(comp)
                        mutable_list.remove(bracket)
                        print(mutable_list)
                    # else:
                        # return False
            elif bracket == '[':
                for comp in mutable_list:
                    if comp == ']':
                        mutable_list.remove(comp)
                        mutable_list.remove(bracket)
                    # else:
                        # return False
            elif bracket == '{':
                for comp in mutable_list:
                    if comp == '}':
                        mutable_list.remove(comp)
                        mutable_list.remove(bracket)
                    # else:
                        # return False

    if mutable_list == []:
        return True
    else:
        return False

multi_bracket_validation("hello()")