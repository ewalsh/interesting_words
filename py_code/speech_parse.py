import numpy
import pendulum
from cassconn import session

def date_check(dt_txt):
    if dt_txt == '':
        return(None)
    else:
        parsed_dt = pendulum.parse(dt_txt, strict=False)
        return(parsed_dt)

# define text parser for presidential speeches
def parse_ps(filename, name, doc_num):
    with open(filename, 'r', encoding='ISO-8859-1') as fobj:
        raw_title = fobj.readline()
        parsed_title = raw_title.strip().replace('<title=','').replace('>','').replace('"','')
        raw_date = fobj.readline()
        parsed_date_txt = raw_date.strip().replace('<date=','').replace('>','').replace('"','')
        parsed_date = date_check(parsed_date_txt)
        counter = 0
        line1 = fobj.readline()
        while line1:
            session.execute(
                """
                INSERT INTO iwords.raw (filename, doc_num, line_num, pres, text)
                VALUES ('{}', {}, {}, '{}', '{}')
                """.format(filename, doc_num, counter, d, line1)
            )
            counter = counter + 1
            print(filename)
            print(parsed_title)
            print(parsed_date)
