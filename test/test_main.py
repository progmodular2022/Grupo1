import sys
path_to_module = "./src/"
sys.path.append(path_to_module)

from main import *

def fake_isWord(word,fromWhere):
    if word in fromWhere:
        return True
    else:
        return False


def test_insert():
    #joke fake mock cake bake shake make lake
    words = ['joke','fake','mock','cake','bake','shake','make','ab','abcde','abcd']
    for word in words:
        insert(word,words,fake_isWord)==True
    
    assert insert("lake",words,fake_isWord) == False


def test_search():
    assert search("") == False
    assert search("ab") == True
    assert search("abcd") == True
    assert search("abcde") == True
    assert search("jake") == False

def test_show():
    assert showAllWords() == None

def test_delete():
    assert delete("") == False
    assert delete("jake") == False
    assert delete("ab") == True
    assert delete("abcd") == True
    assert delete("abcde") == True


def test_random():
    #joke fake mock cake bake shake make
    words = ['joke','fake','mock','cake','bake','shake','make','at','attention','ab']
    for word in words:
        insert(word,words,fake_isWord)

    assert random() in words

def test_wordsWith():
    #assert wordsWith("") == []
    assert wordsWith("joke") == ['joke']
    assert wordsWith('at') == ['at','attention']
    assert wordsWith('attention') == ['attention']
    assert wordsWith('a') == ['at','attention','ab']
    assert wordsWith('so') == []