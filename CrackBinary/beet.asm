push ebp
mov ebp, esp
sub esp, 0x98
sub esp, 8
push dword [src]            ; const char *src
lea eax, [dest]
push eax                    ; char *dest
call sym.imp.strcpy         ; char *strcpy(char *dest, const char *src)
add esp, 0x10
mov dword [s2], 0x6167654d  ; 'Mega'
mov dword [var_8eh], 0x74656562 ; 'beet'
mov word [var_8ah], 0x73    ; 's' ; 115
sub esp, 0xc
lea eax, [s2]
push eax                    ; int32_t arg_8h
call sym.rot13
add esp, 0x10
sub esp, 8
lea eax, [s2]
push eax                    ; const char *s2
lea eax, [dest]
push eax                    ; const char *s1
call sym.imp.strcmp         ; int strcmp(const char *s1, const char *s2)
add esp, 0x10
test eax, eax
sete al
movzx eax, al
leave
ret
