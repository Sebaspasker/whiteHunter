White Email.

Excel data extraction for send specify messages from txt file via email. It save all emails from excel (Excel col named Email) and asociate it to another variables inside the file.
Can send to all saved emails or manual introduction. Proven on Windows, no Mac or Linux.

--------------------------------------------------------

Usage:
	gitclone https://github.com/Sebaspasker/whiteHunter.git	
	cd whiteHunter
	python whiteEmail.py

--------------------------------------------------------

Direct terminal commands:
"-h" or "--help" --> Help command
"-u" or "--user" --> User introduction, need one value after introduction
"-p" or "--password" --> User introduction, need one value after introduction
"-std" or "--standard" --> Standard host and port introduction ("smtp.gmail.com", 587)

The txt file format have to be next:
{v[VARIABLE_NAME]}

Example:

txt File Example
Hello {v[Name]}!

How are you? I send you this message to remember you owe me {v[Money]} because of the page web {v[WebPage]} ,
when you have some time send me a transfer please. 

Good bye, Daryl

Excel File Example
Name	    | Surname    | Money   | Email 			| WebPage
Sebastian   | Pasker     | 10,00€  | sebaspssps@gmail.com	| www.hello.com
Jose        | Velazquez  | 21,21€  | josevelz@gmail.com         | www.bye.com
Alberto     | Gonzalez   | 112,00€ | albeergoonz@gmail.com      | www.goodnight.com

Created with Python by Sebastian Pasker.
