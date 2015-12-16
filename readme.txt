This is a Twitter bot that can tweet lines from a .txt file when the path is specified.
The .txt document must be prepared in some ways ahead of time.
Though the bot can parse lines into 140-character sets, it cannot account for blank lines and will read them as the end of the file.
It also cannot yet skip repeated lines.
To run this code, your .txt file must be saved in ASCII. 
You must remove any blank lines and ensure there are no repeated lines.
I wrote this program in Sublime 2 using Python 2.7.X and Tweepy 3.4.0 (which is not Python standard library and must be installed)
Not tested with text files other than .txt.
Not tested on a Windows machine.

In consumer.conf, specify the consumer key, auth token, etc., for the twitter app you are linking to bot.