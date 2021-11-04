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


