grammar MetaGrammar;		
sketch:	start production+;
start: non_terminal_group ';';
production: non_terminal_group '->' rhs ';';
rhs:  expansion ('|' expansion+)*;
expansion : (non_terminal_group | terminal_group)+;
terminal_group: TERMINAL+;
non_terminal_group: NON_TERMINAL+;

NON_TERMINAL: '<'[a-zA-Z0-9]+'>';
// TODO all ascii
TERMINAL: ('-')?[a-zA-Z0-9.]+ | [+*=-]+ | [,()>]+;
NS : [ \t\n]+ -> skip;