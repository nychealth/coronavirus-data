####################################################################
# Configuration
####################################################################

fancybeamerdocsbase = \

fancybeamerdocs = \
	$(fancybeamerdocsbase:body.latex.tex=handout.latex.tex)	\
	$(fancybeamerdocsbase:body.latex.tex=slides.latex.tex)
# 	$(fancybeamerdocsbase:body.latex.tex=article.latex.tex)

plainbeamerdocs = 			\


latexdocs =	\
	Covid19GarbageInGarbageOut.tex	\
	COVID19TheDataAbusePandemicSlides.tex

epsgraphics = \

pdfgraphics = \

gifgraphics = \

jpggraphics = \

figgraphics = \

pnmgraphics = \

gnuplotscripts =	\

####################################################################
# Stock setup.
####################################################################

docs =	\
	$(fancybeamerdocs)	\
	$(plainbeamerdocs)	\
	$(latexdocs)

SRC = $(docs) $(fancybeamerdocsbase)

dvis = $(docs:.tex=.dvi)
pses = $(docs:.tex=.ps)
pdfs = $(docs:.tex=.pdf)
4ups = $(plainbeamerdocs:.tex=.4up.ps) $(docs:.tex=.4up.pdf)
4ups2 = $(plainbeamerdocs:.tex=.4up2.ps) $(docs:.tex=.4up2.pdf)

logs = 	$(docs:.tex=.log)	\
	$(docs:.tex=.aux)	\
	$(docs:.tex=.nav)	\
	$(docs:.tex=.out)	\
	$(docs:.tex=.snm)	\
	$(docs:.tex=.toc)	\
	$(docs:.tex=.bbl)	\
	$(docs:.tex=.blg)	\
	$(docs:.tex=-blx.bib)	\
	$(docs:.tex=.run.xml)	

madegraphics = $(pdfgraphics:.pdf=.eps) $(gifgraphics:.gif=.eps) $(figgraphics:.fig=.eps) $(jpggraphics:.jpg=.eps)

graphics = $(madegraphics) $(epsgraphics)

all : $(pdfs)

artifacts :
	-mkdir $(ARTIFACTSDIR)
	cp $(pdfs) $(ARTIFACTSDIR)

slides	: $(fancybeamerdocsbase:body.latex.tex=slides.latex.dvi)	\
	  $(fancybeamerdocsbase:body.latex.tex=slides.latex.pdf)

# Don't make 4up versions by default - they take too long...
4ups : $(4ups)
4ups2 : $(4ups2)

# Don't make .ps versions by default - they're too big!
pses : $(pses)

clean : cleandoc cleangraphics cleandeps

cleangraphics : $(gnuplotscripts:.gp=.gp.clean)
	-rm $(madegraphics) $(gifgraphics:.gif=.pnm) $(jpggraphics:.jpg=.pnm)

cleandoc :
	-rm $(dvis) $(pses) $(pdfs) $(logs) $(4ups) $(4ups2)

cleandeps :
	-rm $(SRC:.tex=.d) $(gnuplotscripts:.gp=.d)

## Generic

%.pdf : %.tex
	-rm $(<:.tex=.bbl) $(<:.tex=.aux)
	pdflatex -file-line-error --synctex=1 -interaction=nonstopmode "\input" $<
	if egrep -q "No file.*\.bbl|Citation.*undefined" $(<:.tex=.log) ; then bibtex $(<:.tex=) ; else echo No bibtex needed. ; fi
	pdflatex -file-line-error --synctex=1 -interaction=nonstopmode --synctex "\input" $<
	pdflatex -file-line-error --synctex=1 -interaction=nonstopmode --synctex "\input" $<

# %.dvi : %.tex
# 	-rm $(<:.tex=.bbl) $(<:.tex=.aux)
# 	latex $<
# 	if egrep -q "No file.*\.bbl|Citation.*undefined" $(<:.tex=.log) ; then bibtex $(<:.tex=) ; else echo No bibtex needed. ; fi
# 	latex $<
# 	latex $<

%.eps : %.pdf
	pdftops -eps $^ $@

%.ps : %.dvi
	dvips -o $@ $<

%.pps : %.dvi
	dvips -Ppdf -o $@ $<

%.pdf : %.pps
	ps2pdf -dSubsetFonts=true -dEmbedAllFonts=true $< $@

%.eps : %.fig
	fig2dev -L eps $^ $@

### Enhanced to run bibtex if necessary - if we're latexing the doc,
### remove the .bbl file if it exists.  Then, if latex complains, we
### need to run bibtex.

survivalCurves.pdf : survivalCurves.dvi
	dvips -Ppdf -o survivalCurves.pps $<
	ps2pdf -dSubsetFonts=true -dEmbedAllFonts=true survivalCurves.pps $@

BV.pdf : BV.tex
	pdflatex $<
	pdflatex $<

predictable.pdf : predictable.tex
	pdflatex $<
	pdflatex $<

survivalCurves.dvi : survivalCurves.tex
	latex $<
	latex $<

%.pnm : %.gif
	giftopnm $^ >$@

%.pnm : %.bmp
	bmptoppm $^ >$@

%.pnm : %.jpg
	jpegtopnm $^ >$@

%.eps : %.pnm
	pnmtops -rle -nosetpage -noturn -imagewidth 4.5 $^ >$@

ersk-logo.eps : ersk-logo.pnm
	pnmtops -rle -nosetpage -noturn -imagewidth 18 $^ >$@

%.pnm : %.png
	pngtopnm $^ >$@

%.png : %.m
	octave <$^

%.4up2.ps : %.pdf
#	acroread -toPostScript -size letter -landscape -pairs -expand $< $@.temp
	acroread -toPostScript -pairs $< $@.temp
#	mpage -R -a -b Letter -l $@.temp >$@
	mpage -R -a $@.temp >$@
	rm $@.temp

%.4up.ps : %.ps
	mpage -R -a $^ >$@

%.4up2.pdf : %.4up2.ps
	ps2pdf14 $< $@

%.fsl : %.lsp
	echo '(compile-file "$^")' | xlispstat

################################ Autodeps

## Tex deps
define get_dependencies
	deps=`perl -ne '($$_)=/^[^%]*\\\(?:include|input)\{(.*?)\}/;@_=split /,/;foreach $$t (@_) {if ($$t =~ /\./) { print "$$t "; } else { print "$$t.tex "; }}' $<`
endef

define get_eps
	epses=`perl -ne '@foo=/^[^%]*\\\(includegraphics|psfig|epsffile)(\[.*?\])?\{(.*?)\}/g;if (defined($$foo[2])) { if ($$foo[2] =~ /\.....?$$/) { print "$$foo[2] "; } else { print "$$foo[2].eps "; }}' $< $$deps`
endef

define get_bibs
	bibs=`perl -ne '($$_)=/^[^%]*\\\(?:bibliography)\{(.*?)\}/;@_=split /,/;foreach $$t (@_) {print "$$t.bib "}' $<`
endef

%.d	: %.tex
	$(get_dependencies) ; echo DEPS = $$deps                ; \
	$(get_eps) ; echo EPSES = $$epses                       ; \
	$(get_bibs) ; echo BIBS = $$bibs                        ; \
	echo "$@ : $< $$deps" > $@	; \
	echo "$*.dvi $*.pdf : $@ $< $$deps $$epses $$bibs" >> $@	; \

### Generating deps from gnuplot script:
# 1. Get rid of commented out code
# 2. Only select plot and output commands
# 3. Get rid spurious output & plot commands
# 4. Extract just the file name parts
# 5. gawk to search for what looks like input & output files and
#    create corresponding dependencies.
#
## Note - If input files are other than .csv or .dat, add them to list.
##      - If output files are other than .eps, .ps, .gif or .png, add them to list.

%.d : %.gp
	echo Processing $^
	echo >$@
	sed 's/^\([^#]*\)#\(.*\)/\1/' $^    |\
	grep 'plot  *"\|set \+output'           |\
	grep -v '/dev/null\|^ *$$'  |\
	sed 's/[^"]*"\([^"]*\)".*/\1/' |\
	sed 's/^[ \\t]*$$//g'	| tee $@.1.log | sort | tee $@.2.log | uniq | sed 's/\r//g' | tee $@.3.log | \
        gawk -v gpfile=$^ '{for (i = 1 ; i <= NF ; i++)  \
                              { if ($$i ~ /\.(dat|csv)$$/)   \
                                   {datf = datf " " $$i}    \
                                else if ($$i ~ /\.(eps|ps|gif|png)$$/)   \
                                   {outf = $$i " " outf} } }    \
                           END {printf("%s : %s %s\n\tgnuplot <$^\n\n%s.clean :\n\t-rm %s\n", outf, datf, gpfile, gpfile, outf)}' >>$@

# This is a rule to generate a file of prerequisites for a given .tex file

include $(SRC:.tex=.d) $(gnuplotscripts:.gp=.d)
