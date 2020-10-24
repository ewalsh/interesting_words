import numpy
import pendulum

# define text parser for presidential speeches
def parse_ps(filename, name, doc_num):
    with open(filename, 'r') as fobj:
        raw_title = fobj.readline()
        parsed_title = raw_title.strip().replace('<title=','').replace('>','').replace('"','')
        raw_date = fobj.readline()
        parsed_date_txt = raw_date.strip().replace('<date=','').replace('>','').replace('"','')
        parsed_date = pendulum.parse(parsed_date_txt, strict=False)
