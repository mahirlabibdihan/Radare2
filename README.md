## RADARE2

The Radare2 project is a set of small command-line utilities that can be used together or independently.

- [Official Website](https://rada.re/n/)

### Installation

- `git clone https://github.com/radare/radare2.git`
- `cd radare2`
- `./sys/install.sh`

### Tutorials

- [A journey into Radare2](https://github.com/ITAYC0HEN/A-journey-into-Radare2)

### radare2

The main tool of the whole framework. It uses the core of the hexadecimal editor and debugger. radare2 allows you to open a number of input/output sources as if they were
simple, plain files, including disks, network connections, kernel drivers, processes under debugging, and so on.
It implements an advanced command line interface for moving around a file, analyzing data, disassembling, binary patching, data comparison, searching, replacing, and
visualizing. It can be scripted with a variety of languages, including Python, Ruby, JavaScript, Lua, and Perl.

#### User Interface

r2 has an embedded webserver and ships some basic user interfaces written in html/js. You can start them like this:
`$ r2 -c=H /bin/ls`

#### Common Usage Pattern

Quickly get into an r2 shell without opening any file.
`$ r2 -`

Open a file.
`$ r2 file`

Open a file and analyze all.
`$ r2 -A file`

#### Command Line

`> pdc@main`

- List strings in data sections
  `> iz`

- Search for Strings in the whole binary
  `> izz`

- Seek
  `> s main`

- Enable `e scr.utf8=true` and `e scr.utf8.curvy=true` to make the outlines beautiful.

#### Disassembly

- Print Disassemblr function
  `> pdf @ main`

#### Debugging

#### Hex Editor

- wz: string write zero terminated string (like w + \x00)
- `> "wz Mahir Labib Dihan"`
- `> VV` then `> x` then `> c`

### r2pm

Package Manager for radare2

### rabin2

A program to extract information from executable binaries, such as ELF, PE, Java CLASS, Mach-O, plus any format supported by r2 plugins. rabin2 is used by the core to
get data like exported symbols, imports, file information, cross references (xrefs), library dependencies, and sections.

#### usage

- Show binary info (see iI command in r2)
  
  `$ rabin2 -I a.out`

### rasm2

A command line assembler and disassembler for multiple architectures (including Intel x86 and x86-64, MIPS, ARM, PowerPC, Java, and myriad of others).

### rahash2

An implementation of a block-based hash tool. From small text strings to large disks, rahash2 supports multiple algorithms, including MD4, MD5, CRC16, CRC32, SHA1,
SHA256, and others. rahash2 can be used to check the integrity or track changes of big files, memory dumps, or disks.

- `!rahash2 -E rot -S s:13 -s "Megabeets\n"`

### radiff2

A binary diﬀing utility that implements multiple algorithms. It supports byte-level or delta diﬀing for binary files, and code-analysis diﬀing to find changes in basic code blocks
obtained from the radare code analysis.

### rafind2

A program to find byte patterns in files.

### ragg2

A frontend for r_egg. ragg2 compiles programs written in a simple high-level language into tiny binaries for x86, x86-64, and ARM.

### rarun2

A launcher for running programs within different environments, with different arguments, permissions, directories, and overridden default file descriptors. rarun2 is useful for:
• Solving crackmes
• Fuzzing
• Test suites

### rax2

A minimalistic mathematical expression evaluator for the shell that is useful for making base conversions between floating point values, hexadecimal representations, hexpair
strings to ASCII, octal to integer, and more. It also supports endianness settings and can be used as an interactive shell if no arguments are given.

## Plugins

### r2dec

plugin in r2 repo to generate the pseudo C code

##### installation

- `$ r2pm install r2dec`

##### usage

- `> pdd@main`


### Cutter

Graphical interface

##### Installation

- Url: [Cutter-v2.3.2-Linux-x86_64.AppImage](https://github.com/rizinorg/cutter/releases/download/v2.3.2/Cutter-v2.3.2-Linux-x86_64.AppImage)

- Source: https://cutter.re/docs/building.html 
sudo apt install meson
### r2pipe

Scripting

##### Installation

- pip install r2pipe

##### Usage

- `r2pipe.open(binary_path)`
- `r2.cmd(command)`
- `r2.cmdj(command_to_return_json)`
- `r2.quit()`
