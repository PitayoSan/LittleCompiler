# LittleCompiler
Little compiler for my Compilers Design class

To execute the program, do `python3 plyyacc.py`  
The input of the program is the file `input.txt` with the desired text to parse.  
An example is already available in the repository, but for further refrence the user can replace or insert text in the file while respecting the following rules and tokens:

- **Allowed types**: 
	- int: [0-9]+
	- float: [0-9]+\.[0-9]+
	- string: .*
	- boolean: true, false 
	- **ID**'s can be used to identify variables
		- [A-Za-z_][A-Za-z_0-9]*
- **Number operations**: +, -. *, /, ^
- **Boolean operations**: ==, !=, >, <, >=, <=
- **String operations**: +
- **Flow control**: (), {}
- **End of statement**: ;
- **Assignation**: =


| Reserved words | Use | 
|-------|-----|
| if, elif, else | if statement |
| do while, while, for | loops |
| int, float, string, boolean | declarations |
| and, or | boolean operations |
| true, false | boolean values |



## Important notes

* The lexer and parser are complete.
* However, the Three Address Code functionality is incomplete. Therefore, as of right now, the program only works until the point of creating the AST.
* In other words, by running the said file the program will analyze the inserted text, parse each token and insert them in nodes of the tree.
