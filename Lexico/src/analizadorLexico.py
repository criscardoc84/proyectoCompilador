import ply.lex as lex
import re
import codecs
import os
import sys

tokens = [
  'ID','NUMBER','PLUS','MINUS','TIMES','DIVIDE','ODD','ASSIGN','NE','LT','LTE','GT','GTE','LPARENT','RPARENT','COMMA','SEMICOLOM','DOT','UPDATE'
]

reservadas = {
  'begin':'BEGIN',
  'end':'END',
  'if':'IF',
  'then':'THEN',
  'while':'WHILE',
  'do':'DO',
  'call':'CALL',
  'const':'CONST',
  'int':'INT',
  'procedure':'PROCEDURE',
  'out':'OUT',
  'in':'IN',
  'else':'ELSE',
}

tokens = tokens+list(reservadas.values())

t_ignore = '\t '
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ODD = r'ODD'
t_ASSIGN = r'='
t_NE = r'<>'
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COMMA = r','
t_SEMMICOLOM = r';'
t_DOT = r'\.'
t_UPDATE = r':='

def t_ID(t):
  r'[a-zA-Z_][a-zA-Z0-9_]*'
  if t.value.upper() in keywords:
      t.value = t.value.upper()
      t.type = t.value
  return t

def t_COMMENT(t):
  r'\#.*'
  pass

def t_CONST(t):
  r'\d+'
  t.value = int(t.value)
  return t

def t_error(t):
  print("Caracter Invalido '%s'" % t.value[0])
  t.lexer.sikip(1)
  
def buscarFicheros(directorio):
  ficheros = []
  numArchivo = ''
  respuesta = False
  cont = 1
  
  for base, dirs, files in os.walk(directorio):
    ficheros.append(files)
    
  for file in files:
    print(str(cont)+". "+file)
    cont= cont+1
    
  while respuesta == False:
    numArchivo = raw_input('\nNumero del test: ')
    for file in file:
      if file == files[int(numArchivo)-1]:
        respuesta = True
        break
  
#Esta linea va a variar de acuerdo a donde gaurdas el archivo.
#C:\Users\crist\Documents\GitHub\proyectoCompilador\Lexico\test
#C:\Users\crist\Documents\GitHub\proyectoCompilador\Lexico\test
directorio = '/c/Users/crist/Documents/GitHub/proyectoCompilador/Lexico/test'
archivo = buscarFicheros(directorio)
test = directorio+archivo
fp = codecs.open(test,"r","utf-8")
cadena = fp.read()
fp.close()

analizador.input(cadena)

while True:
  tok = analizador.token()
  if not tok : break
  print(tok)