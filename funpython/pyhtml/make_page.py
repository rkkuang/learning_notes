#! /usr/bin/env python3
import subprocess
import argparse
import os.path
import os
import re
# py3 make_page.py /Users/anything/THU/astro/softwares/aeroastro/gravlen/microlensing_table/pdfs --destdir lcs --htmlname lcs.html --htmltitle "Microlensing Planet Lightcurves"

css = '''
body {
    font-family: helvetica, arial, freesans, clean, sans-serif;
    font-size: 18px;
    color: #222;
    background-color: lightgrey;
}
.lfbtable {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-around;
}

.row {
    display: flex;
    flex-direction: row;
}

.cell {
    max-width: 24.9%;
    max-height: 24.9%;
    width: auto;
    height: auto;
    background-position: center center;
    background-repeat: no-repeat;
    background-size: cover;
    overflow: hidden;
    transition: .2s ease opacity;

    position:relative;
    float:left; /* optional */

}

.cell > p {
    margin-bottom: 0;
}

.image {
    position:relative;
    float:left; /* optional */
}
.cell .text {
    position:relative;
    top:0px; /* in conjunction with left property, decides the text position */
    left:1px;
    width:300px; /* optional, though better have one */
    color: black;
}

img {
    max-width: 100%;
    display: block;
    padding-bottom: 2px;
}

.cell:hover {
    opacity: 0.8;
}
.cell:hover:after {
    opacity: 1;
}

.copy {
    font-size: 1.2rem;
}

h1 {
    font-size: 1.8rem;
    margin-bottom: 0.63rem;
}

h2 {
    font-size: 1.6rem;
    margin-bottom: 0.86rem;
}

h3 {
    font-size: 1.4rem;
}

h4 {
    font-size: 1.2rem;
}
@media screen and (max-width: 990px) {
    .cell {
        max-width: 33.15%;
        max-height: 33.15%;
    }
}
@media screen and (max-width: 640px) {
    .cell {
        max-width: 49.9%;
        max-height: 49.9%;
    }
}
'''


class Picture(object):
    '''Picture represents the portions of a picture we're interested in.'''

    def __init__(self, name, diskpath, relpath, thumbpath):
        self.name = name
        self.diskpath = diskpath
        self.relpath = relpath
        self.thumbpath = thumbpath

def re_match_urls(txtfilename):
    contents = ""
    with open(txtfilename) as f:
        for line in f.readlines():
            contents += line
    urls = re.findall("https://.*?abstract", contents)
    # print(urls)
    # print(len(urls))
    return urls


def make_thumbnail(diskpath, thumbfolder, maxsize=640):
    '''Takes the path to an image on disk and the path to the output thumbnail
    folder and creates a thumbnail image in the thumbnail directory. If the
    thumbnail directory doesn't exist, it's created.'''
    if not os.path.exists(thumbfolder):
        os.makedirs(thumbfolder)
    # Use imagemagick for thumbnail creation
    thumbpath = os.path.join(
        os.path.abspath(thumbfolder), os.path.basename(diskpath))
    # resize_opts = '-resize {size}x{size}^ -gravity Center -crop {size}x{size}+0+0 '.format(size=maxsize)
    # resize_opts = '-resize {size}x{size}^ -gravity Center'.format(size=maxsize)
    resize_opts = '-thumbnail {size}x{size} -gravity Center'.format(size=maxsize)
    # https://apple.stackexchange.com/questions/335635/where-is-the-convert-command-in-macos
    # Where is the convert command in macOS?
    args = ['convert', "'{}'".format(diskpath), resize_opts, '-quality', '60',
            "'{}'".format(thumbpath)]
    if os.path.exists(thumbpath):
        print("Thumbnail path '{}' already exists, skipping".format(thumbpath))
        return thumbpath
    os.system(" ".join(args))
    return thumbpath


def link_image(diskpath, output_dir):
    '''Creates a symbolic link in the output_dir pointing to the diskpath. The
    name of the symbolic link is the basename of the diskpath.'''
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    source = os.path.abspath(diskpath)
    dest = os.path.join(output_dir, os.path.basename(diskpath))
    if os.path.exists(dest):
        print("Symlink '{}' already exists, skipping".format(dest))
        return dest
    # os.symlink(source, dest)
    try:
        os.system(" ".join([ "cp", source, dest ]))
    except:
        print("cp source failed, maybe not exists")
    return dest

def render_markdown(md):
    '''Calls out to pandoc to render markdown. '''
    args = ['pandoc', '-f', 'markdown', '-t', 'html']
    pandoc = subprocess.Popen(
        args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
    output = pandoc.communicate(input=md)[0]
    return output

def group_rows(pictures,urls,solimgsfolder,maxsize=480):
    rv = ""
    cells = []
    for pic in pictures:
        # <img title="Title Tag Goes Here" src="image.png" alt="Your Alt Tag is Here" />
        # pic.relpath = orgimgs/01_OGLE20120563.png
        solimgpath = solimgsfolder + "/" + pic.relpath.split("/")[-1][:-4]+"_sol.png"
        # print(solimgpath)
        # input()


        # print(solimgpath)
        # input()

        # print(pic.diskpath)
        # input()
        # soldiskpath = pic.diskpath.split("/")
        # soldiskpath[-2] = "solimgs"
        # diskpath = ""
        # for sec in soldiskpath:
        #     diskpath += sec+"/"
        # diskpath = diskpath[:-1]
        # diskpath = diskpath[:-4]+"_sol.png"



        if os.path.exists(solimgpath):
            solimgtitle = "solution"
        else:
            solimgtitle = ""
        solimgpath = solimgpath.split("/")[-2]+"/"+solimgpath.split("/")[-1]

        refurl = urls[int(pic.relpath.split("/")[-1][:2])-1]

        cell = '''
        <div class='cell'><a href='{}'><img src='{}' height="{size}" width="{size}"</a>
        <div class="text"> <p> {}, <a href="{solimg}" title="{solimgtitle}">{solimgtitle}</a>, <a href="{refurl}" title="refurl">refurl</a> </p>  </div>
        </div>
        '''.format(pic.relpath, pic.thumbpath, pic.relpath.split("/")[-1][:-4], size=maxsize, solimg=solimgpath, refurl=refurl, solimgtitle=solimgtitle)
        cells.append(cell)
    rv = "\n".join(cells)
    return rv

def create_gallery(dir_full_path, target=None):
    images = []
    solimgs = []
    for filename in os.listdir(dir_full_path):
        #目录的路径和文件名拼接起来，得到了文件的绝路路径
        # print(os.path.join(path,filename))
        # print(filename)
        if filename.endswith(".png") or filename.endswith(".jpg"):
            if not "sol" in filename:
                images.append(os.path.join(dir_full_path,filename))
                solimgs.append(os.path.join(dir_full_path,filename[:-4]+"_sol.png"))

    images = sorted(images, key=lambda k: float(k.split("/")[-1][:2]))
    solimgs = sorted(solimgs, key=lambda k: float(k.split("/")[-1][:2]))
    return images, solimgs



def create_page_v2(imagesdir, output_dir, copy_path, htmlname,htmltitle,urls):
    '''Create_page accepts a list of paths to images and the location of the
    directory to place the gallery within. Each image must have an extension of
    one of the following:
        .jpg
        .jpeg
        .png
        .gif
    Any file that lacks those extensions will be ignored.
    '''
    
    thumbfolder = os.path.join(os.path.abspath(output_dir), "thumbnails")
    orgimgsfolder = os.path.join(os.path.abspath(output_dir), "orgimgs")
    solimgsfolder = os.path.join(os.path.abspath(output_dir), "solimgs")
    pictures = []

    accepted_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    # images = [img for img in images if img.endswith(tuple(accepted_extensions))]
    images, solimgs = create_gallery(imagesdir)
    for solimg in solimgs:
        _ = link_image(solimg, solimgsfolder)

    for idx, img in enumerate(images):
        abs_thumbpath = make_thumbnail(img, thumbfolder)
        rel_thumbpath = os.path.relpath(abs_thumbpath, output_dir)
        # relpath is the path to the full-resolution image, relative to the
        # output directory. Will point to a symlink, usually.
        # fullres_link = link_image(img, output_dir)
        fullres_link = link_image(img, orgimgsfolder)
        relpath = os.path.relpath(fullres_link, output_dir)
        pic = Picture("", os.path.abspath(img), relpath, rel_thumbpath)
        pictures.append(pic)

        print("{}% complete\r".format(int(100 * (idx / len(images)))), end="")
    print()

    body_md = ""
    if copy_path and os.path.exists(copy_path):
        with open(copy_path) as c:
            body_md = render_markdown(c.read())
    if copy_path and not os.path.exists(copy_path):
        print("The provided path '{}' to a markdown file for the body text does not exist".format(copy_path))


    page = """<!DOCTYPE html>
<html>
<style type="text/css">
{}
</style>
<body>
<head>
    <title>{title}</title>
</head>
<p title="{title}">{title}</p>
<div class='copy'>
{}
</div>
{}
</body>
</html>"""
    table = '<div class="lfbtable">{}\n</div>'
    rows = group_rows(pictures, urls, solimgsfolder)
    table = table.format(rows)

    rv = ""
    rv = page.format(css, body_md, table,title=htmltitle)

    # with open(os.path.join(output_dir, 'index.html'), 'w+') as index:
    with open(os.path.join(output_dir, htmlname), 'w+') as index:
        index.write(rv)

    return rv

def main():
    parser = argparse.ArgumentParser(
        description='Create a web-page with nice tiled links to all the images provided.'
    )
    parser.add_argument('--destdir', type=str, default="./gallery/")
    parser.add_argument('--htmlname', type=str, default="index.html")
    parser.add_argument('--htmltitle', type=str, default="Title")
    parser.add_argument('--bodymarkdown', type=str, help='Location of markdown file to use for the body text.')
    parser.add_argument('images', type=str, nargs='+')
    # parser.add_argument('images', type=str, nargs='+')

    args = parser.parse_args()

    # _ = create_page(args.images, args.destdir, args.bodymarkdown)
    # print(args.images)
    # print(type(args.images))
    pdffolder = args.images[0]
    urltextfile = pdffolder+"/infos.txt"
    urls = re_match_urls(urltextfile)

    _ = create_page_v2(args.images[0], args.destdir, args.bodymarkdown, args.htmlname, args.htmltitle, urls)


if __name__ == '__main__':
    main()




# def create_page(images, output_dir, copy_path):
#     '''Create_page accepts a list of paths to images and the location of the
#     directory to place the gallery within. Each image must have an extension of
#     one of the following:
#         .jpg
#         .jpeg
#         .png
#         .gif
#     Any file that lacks those extensions will be ignored.
#     '''
#     thumbfolder = os.path.join(os.path.abspath(output_dir), "thumbnails")

#     pictures = []

#     accepted_extensions = ['.jpg', '.jpeg', '.png', '.gif']
#     images = [img for img in images if img.endswith(
#         tuple(accepted_extensions))]
#     for idx, img in enumerate(images):
#         abs_thumbpath = make_thumbnail(img, thumbfolder)
#         rel_thumbpath = os.path.relpath(abs_thumbpath, output_dir)
#         # relpath is the path to the full-resolution image, relative to the
#         # output directory. Will point to a symlink, usually.
#         fullres_link = link_image(img, output_dir)
#         relpath = os.path.relpath(fullres_link, output_dir)
#         pic = Picture("", os.path.abspath(img), relpath, rel_thumbpath)
#         pictures.append(pic)

#         print("{}% complete\r".format(int(100 * (idx / len(images)))), end="")
#     print()

#     body_md = ""
#     if copy_path and os.path.exists(copy_path):
#         with open(copy_path) as c:
#             body_md = render_markdown(c.read())
#     if copy_path and not os.path.exists(copy_path):
#         print("The provided path '{}' to a markdown file for the body text does not exist".format(copy_path))


#     page = """<!DOCTYPE html>
# <html>
# <style type="text/css">
# {}
# </style>
# <body>
# <div class='copy'>
# {}
# </div class="image">
# {}
# </body>
# </html>"""
# #     page = """<!DOCTYPE html>
# # <html>
# # <style type="text/css">
# # {}
# # </style>
# # <body>
# # <div class='copy'>
# # {}
# # </div >
# # {}
# # </body>
# # </html>"""
#     table = '<div class="lfbtable">{}\n</div>'
#     rows = group_rows(pictures)
#     table = table.format(rows)

#     rv = ""
#     rv = page.format(css, body_md, table)

#     with open(os.path.join(output_dir, 'index.html'), 'w+') as index:
#         index.write(rv)

#     return rv