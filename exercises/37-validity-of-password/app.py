passt = ["ABd1234@1","a F1#","2w3E*","2We3345"]
def validity (list):
    for xex in list:
        val1=0
        val2=0
        val3=0
        val4=0
        val5=0
        for yey in xex:
            if yey.isalpha():
                val1=1
                if yey.isupper():
                   val2=1 
            if yey.isdigit():
                val3=1
            if (yey=="$" or yey=="#" or yey=="@"):
                val4=1
            if(len(xex)>6 and len(xex)<12):
                val5=1
        if (val1+val2+val3+val4+val5)>4:
            print(xex)

validity(passt)

"""
check the validity of password (Se pasan varias claves separadas por Coma, ver cual cumple.)
-->Pass: ABd1234@1,a F1#,2w3E*,2We3345
Output: ABd1234@1
1. At least 1 letter between [a-z] 
2. At least 1 number between [0-9] 1. 
        At least 1 letter between [A-Z] 
3. At least 1 character from [$#@] 
4. Minimum length of transaction password: 6 
5. Maximum length of transaction password: 12
"""