# encoding: utf-8

from PIL import Image, ImageDraw
import collections

class ChessImage(object):

    @staticmethod
    def get_pixels(filepath, step=0):
        img = Image.open(filepath)
        pixels = list(img.getdata())
        width, height = img.size
        pixels = [pixels[i * width:(i + 1) * width:step] for i in xrange(0, height, step)]
        return pixels

    @staticmethod
    def get_lattice_by_alpha(filepath, step=0):
        img = Image.open(filepath)
        pixels = list(img.getdata())
        width, height = img.size
        pixels = [pixels[i * width:(i + 1) * width:step] for i in xrange(0, height, step)]
        lattice = []
        for row in pixels:
            lattice_row = []
            for pixel in row:
                lattice_row.append(1 if pixel[3] > 0 else 0)
            lattice.append(lattice_row)
        return lattice

    @staticmethod
    def get_lattice_image_by_alpha(srcpath, destpath, fillcolor, step=0):
        srcimg = Image.open(srcpath)
        destimg = Image.new("RGBA", srcimg.size)
        pixels = list(srcimg.getdata())
        width, height = srcimg.size
        pixels = [pixels[i * width:(i + 1) * width:step] for i in xrange(0, height, step)]
        for j in range(len(pixels)):
            row = pixels[j]
            for k in range(len(row)):
                pixel = row[k]
                if pixel[3] > 0:
                    draw = ImageDraw.Draw(destimg)
                    draw.ellipse([k * step, j * step, (k + 0.5) * step, (j + 0.5) * step], fill=fillcolor)
        destimg.save(destpath)

    @staticmethod
    def get_lattice_by_filter_color(filepath, filtercolor, step=0):
        img = Image.open(filepath)
        pixels = list(img.getdata())
        width, height = img.size
        pixels = [pixels[i * width:(i + 1) * width:step] for i in xrange(0, height, step)]
        lattice = []
        compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
        for row in pixels:
            lattice_row = []
            for pixel in row:
                lattice_row.append(1 if not compare(filtercolor, pixel[0:3]) else 0)
            lattice.append(lattice_row)
        return lattice

    @staticmethod
    def get_lattice_image_by_filter_color(srcpath, destpath, filtercolor, fillcolor, step=0):
        srcimg = Image.open(srcpath)
        destimg = Image.new("RGBA", srcimg.size)
        pixels = list(srcimg.getdata())
        width, height = srcimg.size
        pixels = [pixels[i * width:(i + 1) * width:step] for i in xrange(0, height, step)]
        compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
        for j in range(len(pixels)):
            row = pixels[j]
            for k in range(len(row)):
                pixel = row[k]
                if not compare(filtercolor, pixel[0:3]):
                    draw = ImageDraw.Draw(destimg)
                    draw.ellipse([k * step, j * step, (k + 0.5) * step, (j + 0.5) * step], fill=fillcolor)
        destimg.save(destpath)

    @staticmethod
    def get_circle_points_drawing_doc_by_filter_color(srcpath, filtercolor, destpath, radius, fillcolor="rgba(226, 226, 226, 1)", step=0):
        img = Image.open(srcpath)
        pixels = list(img.getdata())
        width, height = img.size
        pixels = [pixels[i * width:(i + 1) * width:step] for i in xrange(0, height, step)]
        lattice = []
        compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
        for row in pixels:
            lattice_row = []
            for pixel in row:
                lattice_row.append(1 if not compare(filtercolor, pixel[0:3]) else 0)
            lattice.append(lattice_row)
        htmlfile = open(destpath, "w")
        htmlfile.write('<!DOCTYPE html>\n')
        htmlfile.write('<html>\n')
        htmlfile.write('<head lang="en">\n')
        htmlfile.write('<title></title>\n')
        htmlfile.write('</head>\n')
        htmlfile.write('<body>\n')
        htmlfile.write('<canvas id="myCanvas" width="960" height="491"></canvas>\n')
        htmlfile.write('<script>\n')
        htmlfile.write('var lattice = ' + lattice.__str__() + ';\n')
        htmlfile.write('var canvas = document.getElementById("myCanvas");\n')
        htmlfile.write('var context = canvas.getContext("2d");\n')
        htmlfile.write('context.fillStyle = "' + fillcolor + '";\n')
        htmlfile.write('for (var i = 0, numRows = lattice.length; i < numRows; i++) {\n')
        htmlfile.write('\tvar row = lattice[i];\n')
        htmlfile.write('\tfor (var j = 0, numPixels = row.length; j < numPixels; j++) {\n')
        htmlfile.write('\t\tif (row[j]) {\n')
        htmlfile.write('\t\t\tcontext.beginPath();\n')
        htmlfile.write('\t\t\tcontext.arc(j * %d, i * %d, + %d, 0, 2 * Math.PI, false);\n' % (step, step, radius))
        htmlfile.write('\t\t\tcontext.fill();\n')
        htmlfile.write('\t\t}\n')
        htmlfile.write('\t}\n')
        htmlfile.write('}\n')
        htmlfile.write('</script>\n')
        htmlfile.write('</body>\n')
        htmlfile.write('</html>\n')
        htmlfile.close()