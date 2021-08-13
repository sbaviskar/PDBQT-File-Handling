## Author : Swapnil Baviskar
#import os package to use file related methods
import os
print("Enter extension of file which you want ot modify \n eg : .txt , .pdbqt \n ")
extenStr =input(" => ");      #for extension

#for reading files from directory 
for file in os.listdir():
    if extenStr in file:   # read
        # creating folder
        if not os.path.exists('my_folder'):  
            os.makedirs('my_folder')
        #     
        f = open(file)
        count = 0 ;
        le = 0 ;
        alist =[]
        idx = 0
        # reading data from file 
        for i in f:
             alist.append(i)
        f.close()
        #for new file name and path  
        cwd = os.getcwd ();  # geeting path of current working directory
        cwd += "\my_folder\\"+file # modifing name for writing 
        f = open(cwd,"w+")
        # writing to file
        for i in range(1,(len(alist)-1)):
            f.write(alist[i])
        f.close();

        
        # notification 
        print(file,"\t-------Done-----")
        ##print(alist)
      
    
 input(">>>>>>>>> Press Enter to  EXIT <<<<<<<<<");


