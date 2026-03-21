Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> f = open('C:/Users/katie/Downloads/rosalind_ini5 (4).txt', 'r')
>>> lines = f.readlines()
>>> even_lines = lines[1::2]
>>> with open ('output.txt' , 'w') as out:
...     for line in even_lines:
...         out.write(line)
... 
...         
58
43
68
44
39
38
63
49
57
51
44
42
45
47
55
39
39
42
39
42
