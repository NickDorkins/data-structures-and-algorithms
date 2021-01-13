
# input <-- LL1, LL2
# output <-- zipList
# Current1 = LL1.head
# Current2 = LL2.head
# if current1 = NONE
# current1 = current2
# current1.head = current2.head
# return LL1
# while current1 != NONE
# if current2.next = NONE
# placeholder = current1.next
# current1.next = current2
# current1.next.next = placeholder
# current1 = current1.next
# current2 = current2.next
# while current2 != NONE
# current1.next = current2
# current1 = current1.next
# current2 = current2.next
# return LL1


def zipLists(list1, list2):
    current1 = list1.head
    current2 = list2.head

    if current1 = NONE:
        current1 = current2
        current1.head = current2.head
        return list1

    while current1 != NONE:
        if current2.next = NONE:
            placeholder = current1.next
            current1.next = current2
            current1.next.next = placeholder
            current1 = current1.next
            current2 = current2.next
        while current2 != NONE:
            current1.next = current2
            current1 = current1.next
            current2 = current2.next
            return list1