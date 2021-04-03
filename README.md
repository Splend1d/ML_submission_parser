# Parser for ML
1. go to NTUCOOL to download all submissions, paste to this directory, and rename the folder as 'submissions'
2. go to FB group to download 'student_list_grade.csv', and paste to this directory
3. write data to two columns in the csv : 'strong' and 'ranking', 'strong' is 1 if the student passes the strong baseline, 'strong' is 0 other
4. (Optional) Write data to the 'ranking', the output pdf order will be affected by this, default : lower ranking score is better.

3. execute unzip_data.sh

4. execute parse_strong.py(on linux) If the ranking is reversed, change line 21 to '''rank = sorted(rank, reverse = True)'''

