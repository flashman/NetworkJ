##purpose

An early idea of what a social network analysis package could be in [Julia](http://julialang.org). Currently only supports undirected, unweighted graphs. Has the advantages of ease of use and fast graph modification routines.

##disclaimer

Not affiliated with NetworkX, although I'm attempting to create a package that is similarly easy to use. Their work is fantastic: you can check it out [here](http://networkx.github.io).

##second disclaimer

This is an early version and it is useful to remember that there could be bugs. This code is not intended for use in a research context yet, and I assume no responsibility for errors causing the sky to fall, etc. 

##license
This code is lisenced under a [GPL-3 license](https://www.gnu.org/copyleft/gpl.html).

##todo
1. weighted graphs
2. split functions into two parts: wrapper (call by node name) and function (call by node index)
3. a test suite comparing with a known-to-be-correct network package

##thanks to
- [Chris Cameron](https://github.com/chrisjcameron), who wrote the fast tie_range code