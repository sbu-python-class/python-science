ALL: cfunc_multid.so

SOURCES := cfunc_multid.c
OBJECTS := $(SOURCES:.c=.o)

%.o: %.c
	gcc -c -fPIC $< -o $@


cfunc_multid.so: $(OBJECTS)
	gcc -shared -o cfunc_multid.so $(OBJECTS)

