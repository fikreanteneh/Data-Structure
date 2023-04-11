class Contact:
    
    def __init__(self):
        self.__contact__ = []
    
    def contactList(self):     # this returns the  the contact list
        return self.__contact__

    def add(self, value):    # add contact but contact with the same name is not allowed even if they differ by capitalization
        index = self.insertIndex(value.lower())
        if index == 0:
            self.__contact__ = [value] + self.__contact__
        elif index == len(self.__contact__):
            self.__contact__ = self.__contact__ + [value]
        else:
            self.__contact__ = self.__contact__[0:index] + [value] + self.__contact__[index:]

    def addList(self, values):  # use it to add list of contacts
        for contacts in values:
            self.add(contacts)

    def remove(self, value):   # this function removes a contact from the list. capitalization doesnt matter
        index = self.searchIndex(value.lower())
        if index < 0:
            raise Exception("There is no such contact list")
        self.__contact__.pop(index)

    def insertIndex(self, value):  #find the index to insert a value
        left,right = 0, len(self.__contact__) - 1
        while left <= right:
            mid = (right + left) // 2
            if len(self.__contact__) == mid + 1:
                return mid 

            elif self.__contact__[mid].lower() <= value < self.__contact__[mid + 1].lower():
                return mid + 1
            elif value < self.__contact__[mid].lower():
                right = mid - 1
            else:
                left = mid + 1
        return 0
        
    def searchIndex(self, value): #to get the exact index of a given contact
        index = self.insertIndex(value)
        if self.__contact__[0] is None or (index == 0 and self.__contact__[index].lower() != value):
            return - 1
        elif self.__contact__[index - 1].lower() == value.lower():
            return index - 1
        return -1

    def search(self, value):  #returns related contacts
        index = self.insertIndex(value.lower()) - 1
        if index < 0: index = 0
        size = len(value)
        relatedlist = []
        while self.__contact__[index] is not None  and len(self.__contact__[index]) >= size and self.__contact__[index].lower()[:size] == value.lower():
            relatedlist.append(self.__contact__[index])
            index += 1
        return relatedlist

#use Contact to instanciate a contact list ie c = Contact()
#use c.add("string") to add to contact
# use c.addList([list])  to add list of contacts
# use c.search("strings") to find related characters
# use c.searchIndex("strings") to find index of the value
# use c.remove("string") to remove a contact with that value


# below is random contact lists
x = Contact()
x.add("BETSI")
x.add("yosi")
x.add("fikre")
x.add("sinte")
x.add("anteneh")
x.add("ayele")
x.add("abebe")
x.add("osd")
x.add("dean")
x.add("far")
x.add("12ab")

x.add('betty')
x.add('billen')
x.addList(['shambel', 'ababa', '123sa','@!#$','@@@','zzas','oojouh7','88','  45@!$', 'zxcvb'])
x.add('dfg')
x.add('vina')
x.add('abdu')
x.add('    ee')
x.remove("zzas")
print(x.contactList())
print(x.search('123'))
print(x.searchIndex('betsi  '))

