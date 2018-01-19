FROM debian:stretch-slim

RUN apt-get update && apt-get --no-install-recommends -y install python-setuptools wget texlive texlive-latex-extra python-pip texlive-lang-german
RUN wget http://www.cs.cmu.edu/afs/cs/misc/tex/common/teTeX-3.0-distrib/share/texmf/tex/latex/g-brief/g-brief.cls
RUN wget http://www.cs.cmu.edu/afs/cs/misc/tex/common/teTeX-1.0.1/lib/texmf/tex/latex/misc/pdfpages.sty
RUN wget http://computer-vision.org/4authors/eso-pic.sty
RUN wget http://computer-vision.org/4authors/crv_eso.sty
RUN wget http://code.haskell.org/~byorgey/TMR/Issue16/ucsencs.def
RUN wget http://code.haskell.org/~byorgey/TMR/Issue16/uni-global.def
RUN wget https://ocw.mit.edu/courses/mathematics/18-310-principles-of-discrete-applied-mathematics-fall-2013/recitations/ulem.sty
RUN wget https://raw.github.com/rivercheng/cv/master/currvita.sty
RUN wget http://mirror.math.ku.edu/tex-archive/macros/latex/contrib/ucs/utf8x.def
RUN wget http://ctan.mirrors.hoobly.com/language/german/ngerman.sty

COPY . /
WORKDIR /
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["wal.py"]
