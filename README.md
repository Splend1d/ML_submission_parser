# ML submission parser
Prerequisite : `pip install pikepdf`
1. go to NTUCOOL to download all submissions, paste to this directory, and rename the folder as 'submissions'
2. go to FB group to download 'student_list_grade.csv' (due to privacy concerns), and paste to this directory
3. write data to two columns in the csv : 'strong' and 'ranking', 'strong' is 1 if the student passes the strong baseline, 'strong' is 0 otherwise
4. (Optional) Write data to the 'ranking', the output pdf order will be affected by this, default : lower ranking score is better.

5. execute unzip_data.sh

6. execute parse_strong.py(on linux) If the ranking is reversed, change line 21 to ` rank = sorted(rank, reverse = True)` 

The 'strong_submissions' folder contains all the student's submission that passes the strong baseline, the folders are ordered by ranking

The 'strong.pdf' file is the concatenation of all the submitted reports, ordered by ranking.
