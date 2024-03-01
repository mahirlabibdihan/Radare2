`r2 -h` shows the possible radare2 commands. Note that radare2 can be written as r2 

#rabin2 
>rabin2 allows extracting information from binary files including Sections, Headers, Imports, Strings, Entrypoints, etc. It can then export the output in several formats. 
so we use `rabin2 -I project_binary` to see information about the file , this could also be done by using the radare2 directly


```
r2 project_binary
i
```


#Analysis
>radare2 doesn’t analyze the file by default because analysis is a complex process that can take a long time, especially when dealing with large files.


***
To analyze the file we can use the `aa` or `aaa` command. However to start analysis at the beginning we can perform `r2 -A project_binary`
During the analysis of the file radare2 assigns flag to the sections and store then in a flagspace. In order to see the necessary flags contained in the binary file , we can use 
```
fs
fs strings; f
fs imports; f
```
--- 
To see the provided strings , we can use `iz` or `izz` command. _iz shows all the strings in the data section and izz shows all the strings in the whole binary_.


Now to find where those strings are used (namely the location and the corresponding function) , we use a key feature of radare2 known as analyze x-refs to (`axt` command). We can see that all 4 strings in the data section, are used in the main function by using the command 
`axt @@ str.*` 

>>The special operator @@ is like a foreach iterator sign, used to repeat a command over a list of offsets (see @@?), and str.* is a wildcard for all the flags that start with str.. This combination helps us not just to list the strings flags but also to list the function name, where they are used and the referencing instruction. 

_So , all the strings are in the main function, so we need to seek towards the main_
In order to seek in radare2 , we use the `s` command , from `s?` , we can find that we can seek to main using `s main`



#Disassemble
In order the disassemble the main function , we can use the command `pdf` (print disassemble function)



The disassemble codes , can be viewed in different formats (such as hexdump, strings, colorcode) by enter 'V'. You can switch the modes using 'P/p'. To quit from a specific mode , we can use the 'q' command. To view the assembly code in graph mode , use 'VV'.


From the code , we can see that it is using a beet function. Our binary checks the result of beet that is called with the argument we pass to the program. If we want to see the assembly code for the beet function, we use `pdf @sym.beet` .


**Overall, this code appears to copy a string(Mega+beet+s) from source to destination, perform a ROT13 transformation on the string stored in s2, and then compare it with the original destination string. Finally, it returns a boolean indicating whether the two strings are equal after the ROT13 transformation.**



So in , order to get a success message , we need give input as the correct ROT13 value for "Megabeets". Radare2 has a functionally called _rahash2_ , if we run `man rahash2` from radare2 , we can see : 

>>This program is part of the radare project.Rahash2 allows you to calculate, check and show the hash values of each block of a target file. The block size is 32768 bytes by default.You can hash big files by hashing each block and later determine what part of it has been modified. Useful for filesystem analysis.This command can be used to calculate hashes of a certain part of a file or a command line passed string.This is the command used by the 'ph' command of radare.

So, we can execute the encryption of the string "Megabeets" from our radare2 command line using :  `!rahash2 -E rot -S s:13 -s "67xSojib\n"` - the output shows the value "67kFbwvo" . 

Now , let's open the binary file inside radare2 using the `ood` command , so we run `ood Zrtnorrgf`. Then use the `dc` (debug continue) to run the code and we see that we are getting the success message .
                  