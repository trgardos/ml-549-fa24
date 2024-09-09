# ML549 Readme

## Development Environment Setup for website and slides

The site and slides are created using [Quarto](https://quarto.org/). In order to
build the site and slides you need to install Quarto. You can install quarto from
this [link](https://quarto.org/docs/get-started/). Follow the instructions in the
*Get Started* section for VSCode. For VSCode you need to also install the 
Quarto extension. This allows you to preview the content you have created in VSCode.

## Python environment

> Tested on MacOS Sonoma 14.5 with python 3.12.4.

To execute the Python code used in the book requires several Python packages. 

We recommend using [`venv`](https://docs.python.org/3/library/venv.html) to
create a virtual environment with all the necessary pacakges. To set up this
environment use the following terminal commands

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Quarto Project Selection

We use [Quarto Projects](https://quarto.org/docs/projects/quarto-projects.html)
to manage the YAML configurations specific to the 
output type (e.g. website or lecture slides) using 
[project profiles](https://quarto.org/docs/projects/profiles.html).

Per profiles documentation, we define YAML configuration files for each project
type:

* `_quarto-web.yml`  to create the website in output directory `_site`
* `_quarto-slides.yml` to create slides in output directory `_revealjs`

along with a base `_quarto.yml` configuration.


## Building the Site Locally

> Tested with Quarto 1.5.55 on MacOS Sonoma 14.5.

```sh
# From ds701_book/ dir
quarto render --profile web
```

The html files are all located in the `_site` directory. The `_site` directory is
not committed in the repository.

### Previewing the Lecture Notes Website

To preview and individual chapter using VSCode, open that chapter's qmd file in 
VSCode and run `Shift-Command-K` in the terminal or click on the preview icon
on the upper right of the code window,.

Alternatively you can run `quarto preview --profile slides` or 
`quarto preview --profile web` from a terminal prompt.
To exit preview, hit `Ctl-c` in the same terminal window.

## Rendering Slides

To render slides for each lecture run
```sh
quarto render --profile slides
```
The resulting slides are writtein to `_revealjs` which
is ignored by git.

Any easy way to select slides to preview is to open the folder in a browser
such as `file:///<path-to-project-parent-folder>/DS701-Course-Notes/ds701_book/_revealjs/`.
Then you can just click on one of the `.html` files to view the slides.

You can render just one slide with a command like
```sh
quarto render filename.qmd --profile slides
```
