# lesson14
Closed Key Encryption

#### Complete the lesson at [https://projects.raspberrypi.org/en/projects/secret-agent-chat](https://projects.raspberrypi.org/en/projects/secret-agent-chat). You do not have to do this as a stand alone app.  See Enhancements below.  Either use the provided wordproccessor app or your enhanced lesson13

### Enhancements

1. Instead of making a text based menu, use your word processor app from lesson 13.  Program the encrypt and decrypt buttons to run the functions talked about in this lesson.
2. Alter the program so that capital letters are preserved.
3. Alter the program so that punctuation and numbers are also encrypted.

### Discussion Questions

1. If I were to encrypt "this word is not this word", "this" and "word" will not have the same characters in both cases.  Why does your program do this?
2. Why is this an advantage to the owner of the message?
3. In the intro to computer science class, we talk about using frequency attacks to determine which character must be the letter "E" because it happens the most in the message.  Why doesn't that attack work here?
4.  With the example in number one, I could use the fact that "is" has two characters to guess that it is the word "is".  Why can't I then use that information to break the encryption for the last two letters of "this"?
5. True or False.  In your App, each letter is shifted the same number of characters in the Cypher Alphabet.
