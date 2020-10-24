import numpy
import pendulum
from cassconn import create_session

def date_check(dt_txt):
    if dt_txt == '':
        return(None)
    else:
        parsed_dt = pendulum.parse(dt_txt, strict=False)
        return(parsed_dt)

# define text parser for presidential speeches
def parse_ps(filename, name, doc_num):
    with open(filename, 'r', encoding='mbcs') as fobj:
        raw_title = fobj.readline()
        parsed_title = raw_title.strip().replace('<title=','').replace('>','').replace('"','')
        raw_date = fobj.readline()
        parsed_date_txt = raw_date.strip().replace('<date=','').replace('>','').replace('"','')
        parsed_date = date_check(parsed_date_txt)
        print(filename)
        print(parsed_title)
        print(parsed_date)
