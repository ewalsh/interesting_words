import os
from speech_parse import parse_ps

folder_root = 'Presidential_Speeches'
speeches_dir = os.listdir(folder_root)

for d in speeches_dir:
    pres_speeches = folder_root + '/' + d
    speech_files = os.listdir(pres_speeches)
    speech_files.sort()
    counter = 0
    for speech_file in speech_files:
        speech_path = pres_speeches + '/' + speech_file
        # line 1 is title
        parse_ps(speech_path, d, counter)
        counter = counter + 1
        # line 2 is date
        # line 3 onward is the speech text
