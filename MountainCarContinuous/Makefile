antlr4 = java -jar /usr/local/lib/antlr-4.9.1-complete.jar
codegen_dir = PiRL/GrammarParser
parser: clean
	$(antlr4) MetaGrammar.g4 -no-listener -visitor -Dlanguage=Python3 -o $(codegen_dir)

clean:
	rm -rf $(codegen_dir)/* 
