#!/usr/bin/env python3

def no_c(my_string):
  upd_str = ''
  for i in my_string:
        if i != 'c' and i != 'C':
            upd_str += i
    return (upd_str)
