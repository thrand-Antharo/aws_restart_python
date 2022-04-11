{"filter":false,"title":"caesar_debug-3.py","tooltip":"/caesar_debug-3.py","undoManager":{"mark":11,"position":11,"stack":[[{"start":{"row":0,"column":0},"end":{"row":55,"column":24},"action":"insert","lines":["# Module Lab: Caesar Cipher Program Bug #3","#","# In a previous lab, you created a Caesar cipher program. This version of","# the program is buggy. Use a debugger to find the bug and fix it.","","# Double the given alphabet","def getDoubleAlphabet(alphabet):","    doubleAlphabet = alphabet + alphabet","    return doubleAlphabet","","# Get a message to encrypt","def getMessage():","    stringToEncrypt = input(\"Please enter a message to encrypt: \")","    return stringToEncrypt","","# Get a cipher key","def getCipherKey():","    shiftAmount = input(\"Please enter a key (whole number from 1-25): \")","    return shiftAmount","","# Encrypt message","def encryptMessage(message, cipherKey, alphabet):","    encryptedMessage = \"\"","    uppercaseMessage = \"\"","    uppercaseMessage = message.upper()","    for currentCharacter in uppercaseMessage:","        position = alphabet.find(currentCharacter)","        newPosition = position + int(cipherKey)","        if currentCharacter in alphabet:","            encryptedMessage = encryptedMessage + alphabet[newPosition]","        else:","            encryptedMessage = encryptedMessage + currentCharacter","    return encryptedMessage","","# Decrypt message","def decryptMessage(message, cipherKey, alphabet):","    decryptKey = -1 * int(cipherKey)","    return encryptMessage(message, cipherKey, alphabet)","","# Main program logic","def runCaesarCipherProgram():","    myAlphabet=\"ABCDEFGHIJKLMNOPQRSTUVWXYZ\"","    print(f'Alphabet: {myAlphabet}')","    myAlphabet2 = getDoubleAlphabet(myAlphabet)","    print(f'Alphabet2: {myAlphabet2}')","    myMessage = getMessage()","    print(myMessage)","    myCipherKey = getCipherKey()","    print(myCipherKey)","    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)","    print(f'Encrypted Message: {myEncryptedMessage}')","    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)","    print(f'Decrypted Message: {myDecryptedMessage}')","","# Main logic","runCaesarCipherProgram()"],"id":1}],[{"start":{"row":37,"column":55},"end":{"row":37,"column":56},"action":"insert","lines":[" "],"id":2},{"start":{"row":37,"column":56},"end":{"row":37,"column":57},"action":"insert","lines":["#"]},{"start":{"row":37,"column":57},"end":{"row":37,"column":58},"action":"insert","lines":["u"]},{"start":{"row":37,"column":58},"end":{"row":37,"column":59},"action":"insert","lines":["s"]},{"start":{"row":37,"column":59},"end":{"row":37,"column":60},"action":"insert","lines":["i"]}],[{"start":{"row":37,"column":60},"end":{"row":37,"column":61},"action":"insert","lines":["n"],"id":3},{"start":{"row":37,"column":61},"end":{"row":37,"column":62},"action":"insert","lines":["g"]}],[{"start":{"row":37,"column":62},"end":{"row":37,"column":63},"action":"insert","lines":[" "],"id":4}],[{"start":{"row":37,"column":57},"end":{"row":37,"column":58},"action":"insert","lines":[" "],"id":5},{"start":{"row":37,"column":58},"end":{"row":37,"column":59},"action":"insert","lines":["w"]},{"start":{"row":37,"column":59},"end":{"row":37,"column":60},"action":"insert","lines":["a"]},{"start":{"row":37,"column":60},"end":{"row":37,"column":61},"action":"insert","lines":["s"]}],[{"start":{"row":37,"column":61},"end":{"row":37,"column":62},"action":"insert","lines":[" "],"id":6}],[{"start":{"row":37,"column":68},"end":{"row":37,"column":77},"action":"insert","lines":["cipherKey"],"id":7}],[{"start":{"row":37,"column":77},"end":{"row":37,"column":78},"action":"insert","lines":[" "],"id":8},{"start":{"row":37,"column":78},"end":{"row":37,"column":79},"action":"insert","lines":["n"]},{"start":{"row":37,"column":79},"end":{"row":37,"column":80},"action":"insert","lines":["o"]},{"start":{"row":37,"column":80},"end":{"row":37,"column":81},"action":"insert","lines":["t"]}],[{"start":{"row":37,"column":81},"end":{"row":37,"column":82},"action":"insert","lines":[" "],"id":9}],[{"start":{"row":37,"column":82},"end":{"row":37,"column":92},"action":"insert","lines":["decryptKey"],"id":10}],[{"start":{"row":37,"column":35},"end":{"row":37,"column":43},"action":"remove","lines":["cipherKe"],"id":11},{"start":{"row":37,"column":35},"end":{"row":37,"column":45},"action":"insert","lines":["decryptKey"]}],[{"start":{"row":37,"column":44},"end":{"row":37,"column":45},"action":"remove","lines":["y"],"id":12}]]},"ace":{"folds":[],"scrolltop":120,"scrollleft":0,"selection":{"start":{"row":14,"column":0},"end":{"row":14,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":7,"state":"start","mode":"ace/mode/python"}},"timestamp":1649634835631,"hash":"8f8bf774487fcb11a049f662a00e93871310398b"}