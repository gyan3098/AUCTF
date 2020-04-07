 # Walkthrough of thanks giving dinner</h1>
 ## Author: @arrow1326</h2>
 
This is a pwn challenge from AUCTF. 
Link for the binary is [turkey](turkey)
 
If we disassemble the code (Here I have use gdb as well as ghidra tool to disassemble) ,then we would find that
![Disassemble Code](thanks_giving_dinner/disassembled_turkey.png)

the vulnerability in the code is that it assign space for 16 byte but it takes for 36 bytes.
The 20 bytes(36 bytes - 16 bytes) space are used to assign value to the other 4 variables. 


![Turkey variable](thanks_giving_dinner/turkey_variable.png)

If we see closely then we would find that base pointer _ebp_ takes the char value from [ebp-0x2c] and starts filling the **stack**
Since value are assigned from top to bottom for the stack .We will fill the value to the space assigned to different variables
Let's see the disassembled program and it's equivalent C program
So address assigned for variables
* local_10 is [ebp-0xc]
* local_14 is [ebp-0x10]
* local_18 is [ebp-0x14]
* local_1c is [ebo-0x18]
* local_20 is [ebp-0x1c]
* local_2c is [ebp-0x2c]



![variable compare](thanks_giving_dinner/variable_compare.png)

Now we have to do only one thing we have to assign value to variables such that they all occupy 4 bytes in the memory.
For the if statement to be run it should be true to all conditions 
local_10 should be equal to 0x1337
local_14 should be less than -0x14(means less than 0xffffffec)
local_18 should be equal to 0x667463
local_1c should not be equal to 0x14
local_20 should be equal to 0x2a.
Therefore the value that should be assigned to the different variables are

![value](thanks_giving_dinner/value.png)

Link to my python file is [exploit](thanks_giving_dinner/exploit.py).


After that we have to run the python file and redirects its output to the nc session.

`bash>:`python exploit.py > nc -session
And Hurray we got the flag : auctf{I_s@id_1_w@s_fu11!}
