#File is a collection of data which is  in unorganized form
#operations of files: read,write,delete,create
#modes of files:r-> it is used to read only mode
                #w->it is used to override the file
                #a->it is used to add the data at last
                #w+ -> is used to both (read and write)
f=open('sample.txt','w')
f.write('Achyuth')

print('write succesfully')

f.close()

f=open('sample.txt','r')
print(f.read())
