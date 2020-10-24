import os

folder_root = 'Presidential_Speeches'
speeches_dir = os.listdir(folder_root)

for d in speeches_dir:
    pres_speeches = folder_root + '/' + d
    speech_files = os.listdir(pres_speeches).sort()
    for speech_file in speech_files:
        speech_path = pres_speeches + '/' + speech_file
        # line 1 is title

        # line 2 is date
        # line 3 onward is the speech text
