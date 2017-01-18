EPStoPDF = epstopdf

ALL: syllabus.pdf

%.pdf: %.tex
	pdflatex $<
	pdflatex $<

clean:
	$(RM) *.aux *.log
	$(RM) *~

.PHONY: clean
