# CRISTHIAN BALAAM ARCOS DIAZ, MANUEL ALEXIS YTZA RODRIGUEZ, JESUS ARMANDO CABRERA PIñA, AXEL SALVADOR AGUILAR NUÑEZ
#LENGIAJE C++
# importacion de librerias necesarias + el archivo en donde se encuentran los tokens
import sys
import ply.yacc as yacc
from analizador_lexico import tokens

VERBOSE = 1
#------------------------------------- Importancia----------------------------------------------
precedence = (
	('left', 'INCLUDE', 'REQUIRE'),
	('left', 'COMA'),
	('left', 'IGUAL', 'PLUSEQUAL', 'MINUSEQUAL'),
	('left', 'PUNTOYCOMA'),
	('nonassoc', 'ES_IGUAL', 'DESIGUAL'),
	('nonassoc', 'MENOR', 'MENOR_IGUAL', 'MAYOR', 'MAYOR_IGUAL'),
	('left', 'SUMA', 'RESTA'),
	('right', 'CORCHETE_IZQ'),
	('nonassoc', 'NEW'),
	('left', 'ELSEIF'),
	('left', 'ELSE'),
	('right', 'PRIVATE', 'PROTECTED', 'PUBLIC'),
)

#----------------------------------------------------------------------------------------------
#-------------------------------------------- Apartados para metodos de interpretacion de codigo a leer
def p_program(p):
	'program : declaration_list'

	pass


def p_declaration_list(p):
	'''declaration_list : declaration_list  declaration
                           | declaration
                        | additive_expression
    '''
	pass

#---------------------------- Metodo para hacer un modelado de declaraciones
def p_declaration(p):
	'''declaration : var_declaration
				   | fun_declaration
				   | area fun_declaration
				   | header_declaration
				   | class_declaration
				   | echo_stmt
				   | selection_stmt
			       | iteration_stmt
				   | typeclass
				   | alert_stmt
				   | additive_expression
	'''
	pass

#--------------- Metodo para encontrar dentro del codigo en el archivo .js cadenas de asignación ejemplo "variable = 45;"

def p_echo_stmt(p):
	'''echo_stmt : echo_stmt ECHO STRING PUNTOYCOMA
				 | echo_stmt ECHO IDVAR PUNTOYCOMA
				 | empty
				 | echo_stmt ECHO NUMERO PUNTOYCOMA
				 | echo_stmt ECHO boolean PUNTOYCOMA
				 | echo_stmt ECHO fun_declaration PUNTOYCOMA
	'''
	pass


def p_alert_stmt(p):
	'''alert_stmt : ALERT PARENT_IZQ STRING PARENT_DER PUNTOYCOMA
				  | empty

	'''
	pass

#----------------------------------- Declaracion de encabezados---------------------
def p_header_declaration(p):
	'''header_declaration : REQUIRE PARENT_IZQ STRING PARENT_DER PUNTOYCOMA
                          | INCLUDE PARENT_IZQ STRING PARENT_DER PUNTOYCOMA
    '''
	pass

#-------------------------------------- Declaracion Clases
def p_class_declaration(p):
	'''class_declaration : area CLASS VARIABLE LLAVE_IZQ attribute LLAVE_DER
						 | CLASS VARIABLE LLAVE_IZQ attribute LLAVE_DER
	'''
	pass

#-------------------------------------- Declaracion de Atributos
def p_attribute1(p):
	'''attribute : attribute area var_declaration
				 | area var_declaration
				 | attribute area fun_declaration
				 | area fun_declaration
	'''
	pass


def p_area(p):
	'''area : PRIVATE
			| PUBLIC
			| PROTECTED
	'''
	pass

#---------------------------- Declaracion de Variables---------------------------------

def p_var_declaration(p):
	'''var_declaration : VARIABLE PUNTOYCOMA var_declaration
                       | VAR VARIABLE IGUAL simple_expression
					   | VARIABLE PUNTOYCOMA
                       | TIMESTIMES VARIABLE PUNTOYCOMA
                       | TIMESTIMES VARIABLE PUNTOYCOMA var_declaration
                       | VARIABLE IGUAL NUMERO PUNTOYCOMA var_declaration
                       | VARIABLE IGUAL NUMERO PUNTOYCOMA
                       | VARIABLE IGUAL boolean PUNTOYCOMA var_declaration
                       | VARIABLE IGUAL boolean PUNTOYCOMA
                       | VARIABLE IGUAL VARIABLE PUNTOYCOMA var_declaration
                       | VARIABLE IGUAL VARIABLE PUNTOYCOMA
                       | AMPERSANT VARIABLE PUNTOYCOMA var_declaration
                       | AMPERSANT VARIABLE IGUAL VARIABLE PUNTOYCOMA selection_stmt
                       | AMPERSANT VARIABLE PUNTOYCOMA
                       | VARIABLE IGUAL simple_expression PUNTOYCOMA
	'''
	pass

#------------------------------------------- Delaracion de Funciones ---------------------------

def p_fun_declaration(p):
	'''fun_declaration : FUNCTION VARIABLE PARENT_IZQ params PARENT_DER
					   | FUNCTION VARIABLE PARENT_IZQ params PARENT_DER compount_stmt
	'''
	pass

#------------------------------------------- Delaracion de Parametros ---------------------------

def p_params(p):
	'''params : param_list
			  | empty
	'''
	pass


def p_param_list(p):
	'''param_list : param_list COMA param_list
				  | param
	'''
	pass


def p_param(p):
	'''param : VARIABLE
             | VARIABLE CORCHETE_IZQ CORCHETE_DER PUNTOYCOMA
    '''
	pass


def p_compount_stmt(p):
	'compount_stmt : LLAVE_IZQ echo_stmt local_declarations echo_stmt statement_list echo_stmt LLAVE_DER'
	pass


def p_local_declarations(p):
	'''local_declarations : local_declarations var_declaration
						  | empty
	'''
	pass


def p_statement_list(p):
	'''statement_list : statement_list statement
					  | empty
					  | alert_stmt
	'''
	pass


def p_statement(p):
	'''statement : expression_stmt
				 | compount_stmt
				 | selection_stmt
				 | iteration_stmt
			     | return_stmt
			     | class_declaration
				 | echo_stmt
				 | expression
				 | additive_expression
				 | alert_stmt
	'''
	pass


def p_expression_stmt(p):
	'''expression_stmt : expression PUNTOYCOMA
					   | additive_expression
					   | alert_stmt
	'''
	pass


def p_selection_stmt_1(p):
	'''selection_stmt : IF PARENT_IZQ expression PARENT_DER statement
					  | IF PARENT_IZQ expression PARENT_DER statement selection

	'''
	pass

#----------------------------- Formulas de Condicionales ---------------
def p_selection(p):
	'''selection : ELSE statement
				 | ELSEIF statement selection
	 '''
	pass


def p_selection_stmt_2(p):
	'''selection_stmt : SWITCH PARENT_IZQ var PARENT_DER statement
					  | CASE NUMERO DOS_PUNTOS statement BREAK PUNTOYCOMA
					  | DEFAULT DOS_PUNTOS statement BREAK PUNTOYCOMA

	'''
	pass

#---------------------------------------- Formulas de Bucles -------------------------------------

def p_iteration_stmt_1(p):
	'iteration_stmt : FOR PARENT_IZQ var_declaration PUNTOYCOMA expression PUNTOYCOMA additive_expression PARENT_DER statement '
	pass


def p_iteration_stmt_2(p):
	'iteration_stmt : WHILE PARENT_IZQ expression PARENT_DER statement'
	pass


def p_iteration_stmt_3(p):
	'iteration_stmt : DO LLAVE_IZQ statement PUNTOYCOMA LLAVE_DER WHILE PARENT_IZQ expression PARENT_DER'
	pass


def p_return_stmt(p):
	'''return_stmt : RETURN PUNTOYCOMA
				   | RETURN expression PUNTOYCOMA
	'''
	pass

#------------------------------------- Expresiones de Variables Simples y complejos ----------------------------

def p_expression(p):
	'''expression : VARIABLE relop NUMERO
				  | simple_expression
				  | VARIABLE IGUAL AMPERSANT VARIABLE
			      | expression AND expression
				  | expression OR expression
				  | additive_expression
				  | alert_stmt
	'''
	pass


def p_var(p):
	'''var : VARIABLE
		   | VARIABLE CORCHETE_IZQ expression CORCHETE_DER
	'''
	pass


def p_simple_expression(p):
	'''simple_expression : additive_expression relop additive_expression
						 | additive_expression
						 | alert_stmt
	'''
	pass

#-------------------------------------- Expresiones de Comparación ----------------------------
def p_relop(p):
	'''relop : MENOR
			 | MENOR_IGUAL
			 | MAYOR
			 | MAYOR_IGUAL
			 | DESIGUAL
			 | DISTINTO
			 | ES_IGUAL
	'''
	pass

#------------------------------------------------ Expresiones de incrementos y decrementos ejemplo "i++;" "i--;"

def p_additive_expression(p):
	'''additive_expression : additive_expression addop term
    					   | term
    					   | VARIABLE DECREMENTO PUNTOYCOMA
    				       | VARIABLE INCREMENTO PUNTOYCOMA
						   | VARIABLE DECREMENTO
    				       | VARIABLE INCREMENTO
	'''
	pass

#------------------------------------------- Operadores arimétricos -------------------------------
def p_addop(p):
	'''addop : SUMA
			 | RESTA
	'''
	pass


def p_term(p):
	'''term : term mulop factor
			| factor
	'''
	pass


def p_mulop(p):
	'''mulop : MULTIPLICACION
			 | DIVISION
	'''
	pass


def p_factor(p):
	'''factor : PARENT_IZQ expression PARENT_DER
			  | var
			  | NUMERO
			  | boolean
			  | IDVAR PARENT_IZQ args PARENT_DER
	'''
	pass


def p_args(p):
	'''args : args_list
			| empty
			| VOID
	'''
	pass


def p_args_list(p):
	'''args_list : args_list COMA expression
				 | expression
	'''
	pass

#------------------------------------- Expresiones Booleanas ----------------------
def p_boolean(p):
	'''boolean : TRUE
			   | FALSE
	'''
	pass


def p_tclass(p):
	'typeclass : VARIABLE IDVAR IGUAL NEW constructor PUNTOYCOMA'
	pass

#------------------------------------- Contructores ----------------------
def p_costructor(p):
	'''constructor : VARIABLE PARENT_IZQ PARENT_DER
				   | VARIABLE PARENT_IZQ args PARENT_DER
	'''
	pass


def p_empty(p):
	'empty :'
	pass

#--------------------- Metodo para detectar errores durante la compilacion y en el analisis de tokens-------------
def p_error(p):
	if VERBOSE:
		if p is not None:
			print("\x1b[1;33m" + "\t ERROR: Syntax error - Unexpected token" + chr(27) + "[0m")
			print("\n" + "\t\tLine: " + str(p.lexer.lineno) +"\t 👉🏻  " + str(p.value))
		else:
			print(chr(27) + "[1;31m" + "\t Error durante la compilación: “Error de sintáxis”" + chr(27) + "[0m")
			print("\t\tLine:  " + str(p))

	else:
		raise Exception('syntax', 'error')


parser = yacc.yacc()

#---------------------------------------------- Lectura del archivo .cpp
codigo = 'CodigoC.cpp'
scriptfile = open(codigo, 'r', encoding= 'UTF-8')
scriptdata = scriptfile.read()

#---------------------- Formato de impresion en consola y asigancion del analizador sintactico al archivo .cpp--------------------------

print ("\u001b[32m"+"\nINICIA ANALISIS SINTACTICO"+"\u001b[32m")

print("\n" + "\u001b[31;1m" + "REPORTE DE ERRORES:  ------------------------------------------- 👉🏻")
parser.parse(scriptdata, tracking=False)

print ("\u001b[32m"+"\nFINAL ANALISIS SINTACTICO"+"\u001b[32m")
