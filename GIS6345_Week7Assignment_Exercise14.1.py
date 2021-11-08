#Exercise 14.1
#Write a function called sed that takes as arguments a pattern string,a replacement string, and two filenames.
#It should read the first file and write the contents into the second file.

def sed(pattern,replacement,f1,f2):
    try:
        fout = open(f2, 'w')
        fin = open(f1)
        for line in fin:
            newline = line.replace(pattern,replacement)
            fout.write(newline)
    except: 
        print('Something went wrong.')

    fout.close()

sed('a',' ','words.txt','newwords.txt')
