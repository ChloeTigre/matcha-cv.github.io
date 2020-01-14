#!/usr/bin/env python
"""build CVs.

This lazy script builds all the resume datafiles in data/ with all the resume
templates in tpl and puts them in the current directory
"""

import yaml
from glob import glob
from jinja2 import Template

def run():
    ftemplate = glob('matcha-cv/tpl/*.jinja2')
    datafiles = glob('matcha-cv/data/*.yml')
    # just keep the base names in a very dirty but working way
    data = { df.split('/')[-1][0:-4]: yaml.load(open(df)) for df in datafiles }
    tpls = { t.split('/')[-1][0:-7]: Template(open(t, 'rb').read().decode('utf-8')) for t in ftemplate }
    for t_name, t in tpls.items():
        for d_name, d in data.items():
            o = t.render(cv=d)
            out_name = d.get('options', {}).get('force_file_name') or './{d_name}.{t_name}'.format(d_name=d_name, t_name=t_name)
            with open(out_name, 'w') as fh:
                fh.write(o)
            print(o)

if __name__ == '__main__':
    run()
