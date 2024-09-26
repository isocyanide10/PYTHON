letter='''
Dear <|Name|>,
You are selected !
<|Date|>'''
replace=letter.replace('Name','Nirmal').replace('Date','20:08:24').replace('<|','').replace('|>','')

print(replace)