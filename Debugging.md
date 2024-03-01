https://youtu.be/Yn1fGs8WwSM

$> radare2 -d /path/to/my/bin
[some addr]> aaa
[some addr]> afll
[some addr]> db sym.main
[some addr]> dc
[main addr]> v!

$> r2 -d a.out
[some addr]> aaaa
[some addr]> dc
(27479) Process exited with status=0x0
[some addr]> dc
(27479) Process terminated with status 0
INFO: ==> Process finished
[some addr]> oo
WARN: Relocs has not been applied. Please use `-e bin.relocs.apply=true` or `-e bin.cache=true` next time
[some addr]> ood
INFO: File dbg:///mnt/Multimedia/BUET/CSE406_Project/a.out reopened in read-write mode
WARN: Relocs has not been applied. Please use `-e bin.relocs.apply=true` or `-e bin.cache=true` next time
28081

[some addr]> dc
(27479) Process exited with status=0x0
[some addr]> ood
INFO: File dbg:///mnt/Multimedia/BUET/CSE406_Project/a.out reopened in read-write mode
WARN: Relocs has not been applied. Please use `-e bin.relocs.apply=true` or `-e bin.cache=true` next time
28081

F2 toggle breakpoint
F4 run to cursor
F7 step into
F8 step over
F9 continue
Or just use ds?
Usage: ds Step commands
| ds step one instruction
| ds <num> step <num> instructions
| dsb step back one instruction
| dsf step until end of frame
| dsi <cond> continue until condition matches
| dsl step one source line
| dsl <num> step <num> source lines
| dso <num> step over <num> instructions
| dsp step into program (skip libs)
| dss <num> skip <num> step instructions
| dsu[?] <address> step until <address>. See 'dsu?' for other step until cmds.

Visual Debugging

- VVp

ctrl + '-' : Zoom out
ctrl + shift + '+' : Zoom in

h: shift right
l: shift left
j: line down
k: line up

- v!
- press q to exit this mode

dc - debug continue

dsf - Step out of function

After opening in VV

- Can switch functions using the command beside function call like ; [od]

How to go back to parent function?
Find all cross references using 'x'. Then choose the desired index function.

From the visual mode we can go to visual panel mode by shift + '!'
Then from visual panel mode, press space to go to graph mode.

Press '-' to split a tab vertically

After program finishes in visual mode.

> oo
> ood
> https://youtu.be/xCYQtvGwXmI -> Visual panel mode

## Demonstration

`$ gcc -g test.c -o a.out`
`$ r2 -d a.out`
`> aa`
`> afl`
`> d?`
`> db main`
`> db`
`> dc`
`> V`
`> shift + !`
`> space`

Go back to visual debug mode
`> pp`
Demonstrate F7, F8, F9, F2, dsf

### Reverse Debugging

Start trace: dts+
Step back: dsb or 10dsb (To step back 10 step)
`dr rip` to check difference

- Problematic in function calls. Don't trace function call.

### How does io works in visual mode?

https://reverseengineering.stackexchange.com/a/16430
We need a separate terminal for i/o.
Open a new terminal and type `tty`.
We will get something like: `stdio=/dev/pts/4`
Then put to sleep by: `sleep 9999999`

Create rarun2 profile: profile.rr2

> \#!/usr/bin/rarun2
> stdio=/dev/pts/4

Then start debugging by:
`$ r2 -e dbg.profile=profile.rr2 -d a.out`

### Tutorial

https://youtu.be/oW8Ey5STrPI -> Visual mode
https://youtu.be/Yn1fGs8WwSM -> Debugging
https://youtu.be/WEsnOIU2KCg -> Graph View
https://youtu.be/xCYQtvGwXmI -> Visual Panel

In visual modes,
press ':' to type command.
Then, press enter to go back to Visual mode.
