data = """
In office
January 20, 2009 – January 20, 2017
Vice President	Joe Biden
Preceded by	George W. Bush
Succeeded by	Donald Trump
"""
president_data = data.split("\n")
president_data_clean = president_data[1:-1]

dates = []
dates = president_data_clean[1].split("–")
start_date = dates[0]
end_date = dates[1].strip()
vp = president_data_clean[2].split("\t")[1]
pre_by = president_data_clean[3].split("\t")[1]
suc_by = president_data_clean[4].split("\t")[1]

output_data = {"Start_Date:" : start_date,
                "End_Date:" : end_date,
                "VP": vp,
                "Preceded by": pre_by,
                "Succeeded by": suc_by}

for key, value in output_data.items():
    #print(key, value, "\n")
    print(key, value)

import pprint
a = output_data
pprint.pprint(a)

#--------------
"""
output = {"start_date": "January 20, 2009",
         "end_date": "January 20, 2017",
         "VP": "Joe Biden",
         "Preceded by": "George W. Bush",
         "Succeeded by": "Donald Trump"
         }
"""
