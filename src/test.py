from main import *



def fakeIsWord(word,where):
    if word != "Error" and word != "":
        return True
    else:
        return False

#insert joke fake mock cake bake shake make
insert("joke",[],fakeIsWord)
insert("fake",[],fakeIsWord)
insert("mock",[],fakeIsWord)
insert("cake",[],fakeIsWord)
insert("bake",[],fakeIsWord)
insert("shake",[],fakeIsWord)
insert("make",[],fakeIsWord)
insert("at",[],fakeIsWord)
insert("attention",[],fakeIsWord)
insert("ab",[],fakeIsWord)

showAllWords()

clear()

showAllWords()