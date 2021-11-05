import ply.lex as lex
import re
import codecs
import os
import sys

tokens = [
  'CONST','ID','OPPAR','CLPAR','OPKEY','CLKEY','COMI','EQUAL','PLUS','MINUS','MULTI','DIV','MINQ','MORQ','DOTC','TDOT','DOT'
]

reservadas = {
  'imp':'IMPORT',
  'random':'RANDOM',
  'df':'DEF',
  'fr':'FOR',
  'in':'IN',
  'rng':'RANGE',
  'ln':'LEN',
  'rtrn':'RETURN',
  'prt':'PRINT',
  'stg':'STRING',
  'whl':'WHILE',
  '.ppd':'.APPEND',
  'nt':'INT',
  '.rndt':'.RANDINT',
}

tokens = tokens+list(reservadas.values())

t_ignore = '\t'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTI = r'\*'
t_DIV = r'/'
t_EQUAL = r'='
t_OPPAR = r'\('
t_CLPAR = r'\)'
t_OPKEY = r'\{'
t_CLKEY = r'\}'
t_COMI = r'"'
t_MINQ = r'<'
t_MORQ = r'>'
t_DOTC = r';'
t_TDOT = r':'
t_DOT = r','

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
  print "Caracter Invalido '%s'" % t.value[0]
  t.lexer.sikip(1)
  
#Esta linea va a variar de acuerdo a donde gaurdas el archivo.
directorio = '/c/Users/crist/Documents/GitHub/proyectoCompilador/src/test'
archivo = buscarFicheros(directorio)
test = directorio