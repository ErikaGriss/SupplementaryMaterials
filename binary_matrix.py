#This script makes a binary matrix using the aligments from the gene families. Columns = Gene families; rows = "species" (external branches)
#using only 1 or 0 depending if a gene family is present in the external branch or not (I have 98 external branches)

gene_families = 100                                                 # How many files I want to analize
species = []                                                        # An empty list that will store each name of my 98 "species" (external branches)
for i in range (1, gene_families+1):                                # Make a loop to open "i" files (range of files)
    if len(species) < 95:                                           # This stop the loop, because when I reach the 98 species, there is no need to keep opening files and looping (it is complete with 98)
        with open("%i.bmge" % i,"r") as f:                          # Open the file
            for line in f:                                          # Read lines in file
                if line.startswith(">"):                            # The name of species is in the lines starting with ">", so this only read the lines starting with ">"
                    name = line[1:9]                                # Make a variable with only the section of the line that has the name
                    if name not in species:                         # Check if "name" is already in the list "species" (so you don't have repeated names)
                        species.append(name)                        # Append the species name to the list  
#print(species)                                                     # Checkpoint (it works!)

matrix = {}                                                         # Create an empty dictionary so you can store the data
for i in range(0,len(species)):                                     # Tell that you want 98 (len of species) keys in that dictionary
    matrix[species[i]] = []                                         # Make an empty list as the value for each key 

old_name = []                                                       # This would help to NOT append a gene family more than once for each specie 
for i in range (1, gene_families+1):                                # How many files you want to analize
    with open("%i.bmge" % i,"r") as f :                             # Open file (r is for open as a reading object)
        for line in f:                                              # Read lines
            if line.startswith(">"):                                # This is the same as above, you need to get the "name" again so you can compare if it is present in "species", rememeber that if it is present you have to later put 1 to the matrix
                name = line[1:9]
                for i in range (len(species)):                      # Define a range so you compare the new variable "name" with EACH item in your list "species"
                    if name == old_name :                           # If name = old_name means that gene family was already ompared so this line helps to not append two times (or more) a gene family. Remember that the files of the aligments have more than one sequence and sometimes those sequences corresponds to more than 1 species (sometimes all corresponds to one specie)
                        break                                       # Break the loop
                    if name == species[i]:                          # Compare the name variable with the species name (remember the i establish/set the range so it goes from the first item in the list "species" to the last one)
                        matrix[species[i]].append(1)                # Append a "1" in the empty list of the dictionary (value) for each specie (key) 
                    else:                                           # If it is not the same...
                        matrix[species[i]].append(0)                # Append a "0". Remember 1 is if the gene is present in that species, 0 means there is no presence of that gene in that species
                old_name = name                                     # Now save that name so you don't compare it more than once

                
#print(matrix)

import pandas as pd                                                 # Import the package
df = pd.DataFrame(matrix.items())                                   # Make a data frame from the directory
#print(df)

#df.to_csv(r'C:\Users\Pascuallita\Desktop\cien_alignments\binary_matrix.csv', index = False) #Exporrt your dataframe into a csv file!
#with open ("binary_matrix.csv") as bm :
    #for line in bm :
        #line.strip(",")
        #print(line)

names, binary_data = [], []                                          # Create 2 empty lists (one from the keys in matrix and for the values in matrix)
for key, value in matrix.items():                                    # Create the loop that will append in the keys and values of the dictionary called: matrix
    names.append(key)                                                # Append the keys(species) in the list called names
    binary_data.append(value)                                        # Append the values(1´s and 0´s) in the list called "binary data"

with open("my_fasta.txt", "w") as ofile:                             # Create and open a .txt file
    for i in range(len(names)):                                      # Start the loop in the range of i which is equal to the numer of species present in the matrix 
        ofile.write(">" + str(names[i]) + "\n" + ''.join( str(binary_data[i]) ) + "\n")   # Write in a fasta format, starting with the ">" for each name of the species and in the second line paste the 1´s and 0´s (as it was a normal sequence of aminoacids)

                    
# Then I convert the .txt file in .phy (phylip format) file using BioEdit software, but I have to remove the commas:
# Well, I end up not using the "BioEdit" but that could be really really useful in the future, so I'm going to leave that comment here (:
# Surely I did a hundred of unnecessary steps but well, I did it... so:

with open ("my_new_fasta.fasta", "a") as fi :                        # This is a new file just in writing mode (later I will convert this into phylip)
    with open ("my_fasta.txt", "r") as file :                        # Reading the above file to extract the data (I could not make it to read and write at the same time, that is why I create "my_new_fasta")
        for line in file :                                           # To iterate through each line in file
            st = line.replace(", ", "")                              # Removing the commas and spaces between numbers
            s = st.replace("[","")                                   # Remove the " [ " for each part (it has this because it used to be a list)
            t = s.replace("]", "")                                   # Same thing but with the " ] "
            fi.write(t)                                              # Write the corrections into the new file
            print(t)
        

# The next part is just to convert the file from fasta to phylip using biopython module

from Bio import SeqIO
count = SeqIO.convert("my_new_fasta.fasta", "fasta", "my_new_phylip.phy", "phylip")
print("Converted %i records" % count)
