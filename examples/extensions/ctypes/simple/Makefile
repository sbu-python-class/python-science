ALL: cfunc.so

SOURCES := cfunc.c
OBJECTS := $(SOURCES:.c=.o)

%.o: %.c
	gcc -c -fPIC $< -o $@


cfunc.so: $(OBJECTS)
	gcc -shared -o cfunc.so $(OBJECTS)

