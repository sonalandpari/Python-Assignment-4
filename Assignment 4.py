# TASK 1: Read a File and Handle Errors

try:
        
        with open("Sample Text.txt") as file_1:   
             print("Reading File Content:")                                # My friend helped me with this line
             for i, line in enumerate(file_1, start=1):                    # So that it would print "Line 1:" as in the task (Expected output)
                print(f"Line {i}: {line.strip()}")
    
        file_1.close()

except FileNotFoundError:

    print("Error: The file 'Sample Text.txt' was not found.")

# Task 2: Write and Append Data to a File

file_2_w= open("output.txt",'w')
writting= input("Enter text to write to the file: ")
print(file_2_w.write(writting+"\n"))
file_2_w.close()
print("Data Successfully written to output.txt\n")


file_2_a= open("output.txt",'a')
append= input("Enter text to append to the file: ")
print(file_2_a.write(append+"\n"))
file_2_a.close()
print("Data Successfully appended\n")


print("Final content of output.txt:")
file2 = open("output.txt",'r')
print(file2.read())
file2.close()