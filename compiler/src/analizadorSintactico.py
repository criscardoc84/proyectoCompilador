import ply.yacc as yacc
import os
import codecs
import re
from analizadorLexico import tokens
from sys import stdin

precedence = (
  ('right', 'ASSIGN'),
  ('right', 'UPDATE'),
  ('left', 'NE'),
  ('left','LT','LTE','GT','GTE'),
  ('left','PLUS','MINUS'),
  ('left','TIMES','DIVIDE'),
  ('right','ODD')
  ('left','LLPARENT','RPPARENT')
  )

def p_program(p):
  '''program = block'''
  p[0] = proogram(p[1],"pprogram")

def p_constDecl(p):
  '''constDecl = const constAssignment '''