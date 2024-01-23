ORG 100H
INCLUDE EMU8086.INC
                   

mov si,1000H
print 'enter a string: '
start:
 	mov ah,01H
 	int 21H
 	mov [si],al
 	inc si
 	cmp al,'$'
 	je end    
    	jmp start
end:
lea si,[1000H]
lea di,[2000h]  
mov cx,6
rep movsb
mov di,2000h
step1:
	mov al,[di]
	cmp al,'$'
	je end1
	sub al,32
	mov [di],al
	inc di
	jmp step1
end1:
printn
mov dx,offset [2000H]
mov ah,09H
int 21H
ret 
