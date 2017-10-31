# -*- mode: ruby -*-
# vi: set ft=ruby :

$script = <<SCRIPT
sudo apt-get update
sudo apt-get -y install texlive texlive-latex-extra python-pip texlive-lang-german
cd /vagrant
sudo pip2 install -r requirements.txt 
wget http://www.cs.cmu.edu/afs/cs/misc/tex/common/teTeX-3.0-distrib/share/texmf/tex/latex/g-brief/g-brief.cls
wget http://www.cs.cmu.edu/afs/cs/misc/tex/common/teTeX-1.0.1/lib/texmf/tex/latex/misc/pdfpages.sty
wget http://computer-vision.org/4authors/eso-pic.sty
wget http://computer-vision.org/4authors/crv_eso.sty
wget http://code.haskell.org/~byorgey/TMR/Issue16/ucsencs.def
wget http://code.haskell.org/~byorgey/TMR/Issue16/ucs.swgetty
wget http://code.haskell.org/~byorgey/TMR/Issue16/uni-global.def
wget https://ocw.mit.edu/courses/mathematics/18-310-principles-of-discrete-applied-mathematics-fall-2013/recitations/ulem.sty
wget https://raw.github.com/rivercheng/cv/master/currvita.sty
wget http://mirror.math.ku.edu/tex-archive/macros/latex/contrib/ucs/utf8x.def
wget http://ctan.mirrors.hoobly.com/language/german/ngerman.sty 
python2 wal.py & 
SCRIPT


Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"
    config.vm.network "forwarded_port", guest: 5000, host: 5000
    config.vm.provision "shell", inline: $script
end
