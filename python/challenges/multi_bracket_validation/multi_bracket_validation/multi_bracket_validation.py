
def multi_bracket_validation(input: str) -> bool:
    char_list = input
    if len(char_list) == 0:
        return False
    
    mutable_list = []
    brackets = "()[]{}"

    for character in char_list:
        if character in brackets:
            mutable_list.append(character)
        else:
            # char_list.remove(character)
            continue
        
        if len(mutable_list) == 0:
            return False

        iterator = mutable_list
        print(f"ITERATOR {iterator}")

        for bracket in iterator:
            print(f"Iterator in first for loop {iterator}")
            if bracket == '(':
                for comp in mutable_list:
                    if comp == ')':
                        mutable_list.remove(bracket, comp)
                    else:
                        return False
            if bracket == '[':
                for comp in mutable_list:
                    if comp == ']':
                        mutable_list.remove(bracket, comp)
                    else:
                        return False
            if bracket == '{':
                for comp in mutable_list:
                    if comp == '}':
                        mutable_list.remove(bracket, comp)
                    else:
                        return False

    if mutable_list == '':
        return True