SVGS = $(wildcard *.svg)
PNGS = $(addsuffix .png,$(basename ${SVGS}))

all: ${PNGS}

%.png: %.svg
	inkscape -f $< -e $@
