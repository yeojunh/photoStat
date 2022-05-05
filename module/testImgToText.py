from cmath import exp
from unittest import expectedFailure
from imgReader import *

def testImgOne():
    expected = "Windows PowerShell\nCopyright (C) Microsoft Corporation. All rights reserved.\n\nInstall the latest PowerShell for new features and improvements! https://aka.ms/PSwindows\n"
    result = imgToText('data/img/test.jpg')
    # print(result)
    assert expected == result

def testImageTwo():
    expected = "hello there!"
    result = imgToText('data/img/test2.jpg')
    # print(result)
    assert expected == result

# testImgOne()
# testImageTwo()