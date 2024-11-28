# Install

There are different ways to install python-psignifit:

- [Install the latest release](#install-pip) using `pip`. 
This is the recommended approach for most users.

- Download and install the source from the [Github repository](https://github.com/wichmann-lab/python-psignifit/).
Use this approach to inspect and modify the source code or to use a
psignifit version, that was not published in the package index.

*python-psignifit* depends on a few python packages, standard in scientific computing:
`numpy`, `scipy` and `matplotlib`.

These packages are often shipped with scientific python distributions
or, if not already there, are installed automatically during the
installation of python-psignifit. We [automatically check](https://github.com/wichmann-lab/python-psignifit/actions)
compatibility with different python 3 versions on Ubuntu Linux and
Windows. We do not support python 2.

(install-pip)=
## Installing the latest release (preferred method)

Install python-psignifit with all dependencies:

```bash
pip install psignifit
```

## Installing from source

Use this approach to inspect and modify the source code.
To install psignifit, go to 
the [Github repository](https://github.com/wichmann-lab/python-psignifit/).
and click on the "Clone or Download" button on the right.
Then unpack the ZIP file, navigate with the command line inside the
folder python-psignifit, and then run:

```
pip install .
```

## Using Git to be kept up to Date

Instructions on how to install git can be found
[here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

If you have git installed you can also use this to get the newest
version and to keep yourself up to date:

To clone the repository for the first time, change to the directory
where psignifit should be placed. There use the following command in a
terminal:

```
git clone https://github.com/wichmann-lab/python-psignifit.git
```

Now you should have a directory called "python-psignifit" there. This
contains all the code you need and you can proceed to adding the code to
your path as well.

To update your local copy you only need to change to the
"python-psignifit" folder and type:

```
git pull
```

Then reinstall the new version with

```
pip install .
```
