
def extractSection(resumedata,type):
    resumedata = resumedata.split("\n")
    education_text = ""
    first = None
    last = None
    for line in resumedata:
        if first == None:
            if type in line.lower(): 
                splitline = line.split()
                if len(splitline) < 4 and len(splitline) > 0: 
                    firstindex = resumedata.index(line)
                    first = firstindex + 1 
                    break
    section_words = [
        'Objective',
        'Summary',
        'Education',
        'Experience',
        'Skills',
        'Projects',
        'Certifications',
        'Licenses',
        'Awards',
        'Honors',
        'Publications',
        'References',
        'ACHIEVEMENT',
        'ACTIVITIES'
        ]
    for i in range(first,len(resumedata)):
        if last == None:
            if i == len(resumedata)-1:
                last = len(resumedata)-1
            split_line = resumedata[i].split()
            if len(split_line) < 4 and len(split_line) > 0 :
                for word in section_words:
                    if word.lower() in resumedata[i].lower():
                        lastindex = resumedata.index(resumedata[i])
                        last = lastindex
                        break
    extracted_op = ""
    for i in range(first,last):
        extracted_op += resumedata[i]+"\n"
    return extracted_op

