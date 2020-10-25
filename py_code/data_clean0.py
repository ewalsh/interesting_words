import numpy as np
import pandas as pd
import pendulum
import nltk
from cassconn import session

nltk.download("punkt")
nltk.download("maxent_ne_chunker")
nltk.download("universal_tagset")
nltk.download("stopwords")
nltk.download('averaged_perceptron_tagger')

from nltk import regexp_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords


def run_cleaner0():
    party_aff = [('obama', 'D'), ('clinton', 'D'), ('bush', 'R'), ('gwbush', 'R')]

    file_nms_rows = session.execute("SELECT DISTINCT filename FROM iwords.raw")
    file_nms0 = []
    for row in file_nms_rows:
        file_nms0.append(row.filename)


    file_nms = np.array(file_nms0)

    for fnm in file_nms:
        sub_stmt = """SELECT * FROM iwords.raw WHERE filename = '{}';""".format(fnm)
        #print('sub')
        #print(sub_stmt)
        tmp_sub = session.execute(sub_stmt)
        #print('sub executed')
        # pull each row and organize data
        data = []
        for row in tmp_sub:
            tmp = {
                'filename': row.filename,
                'line_num': row.line_num,
                'doc_num': row.doc_num,
                'pres': row.pres,
                'speech_title': row.speech_title,
                'speech_dt': row.speech_dt,
                'in_office': row.in_office,
                'text': row.text
            }
            data.append(tmp)

        # clean data
        df0 = pd.DataFrame(data)
        #print(row.speech_dt)
        time_input = df0['speech_dt'][0]
        if time_input != None:
            talk_time = pendulum.parse(str(time_input))
            pres = df0['pres'][0]
            title = df0['speech_title'][0]
            prty = [p for n, p in party_aff if n == pres][0]
            io_val = df0['in_office'][0]
            for txt_str in df0['text']:
                sw_en = stopwords.words('english')
                stemming = PorterStemmer()
                pattern = "\w+"
                #\w+(?:'\w+)?|[^\w\s]
                #arr = nltk.word_tokenize(df0["text"][0])
                #list(map(lambda x: nltk.pos_tag(x, tagset='universal', lang='eng'), arr))
                arr0 = regexp_tokenize(txt_str, pattern)
                arr1 = map(lambda x: stemming.stem(x), arr0)
                arr2 = [word for word in arr1 if word not in sw_en]
                pos0 = nltk.pos_tag(arr2, tagset='universal', lang='eng')
                for word, pos in pos0:
                    input_time = str(talk_time)
                    if(len(input_time) > 30):
                        input_time = str(talk_time)[0:23]+"+00:00"
                    else:
                        input_time = talk_time
                    stmt = """INSERT INTO iwords.clean0 (filename, talk_time, pres, party, in_office, word, pos) VALUES ('{}', '{}', '{}', '{}', {}, '{}', '{}');""".format(fnm, input_time, pres, prty, io_val, word, pos)
                    #print(stmt)
                    session.execute(stmt)
                    talk_time = talk_time.add(seconds=0.26)
