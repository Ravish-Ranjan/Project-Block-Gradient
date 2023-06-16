from PIL import Image
import json
import colorsys

def rgba_to_hsla(rgba):
    r,g,b,a = rgba
    tohls = colorsys.rgb_to_hls(r/256,g/256,b/256)
    h,l,s = tohls
    h *=360
    return[round(h,0),round(s,2),round(l,2),round(a/256,2)]

def avgimg(filepath):
    img = Image.open(filepath)
    pixeldata = img.load()
    img.close()
    r,g,b,a = 0,0,0,0
    for y in range(16):
        for x in range(16):
            color = pixeldata[x,y]
            if len(color) != 4:
                color = (color[0],color[1],color[2],255)
            r += color[0]
            g += color[1]
            b += color[2]
            a += color[3]
    r = int(r/256)
    g = int(g/256)
    b = int(b/256)
    a = int(a/256)
    return rgba_to_hsla([r,g,b,a])

blockget = "C:/sem4/vs code/project blocks/scandir.json"
blockpost = "C:/sem4/vs code/project blocks/block color data.json"

def dictgenerator(filename):
    global block_root
    filepath = block_root+filename
    col = avgimg(filepath)
    trans = False
    if col[3] != 1:
        trans = True
    block_id = {
        "name":filename.split(".png")[0],
        "path":filepath,
        "color":col,
        "transparent":trans,
        "exclusive":False,
    }
    return block_id

with open(blockget) as job:
    block_data = json.load(job)
    block_root = block_data['root']
    block_files = block_data['files']

main_block_data = []

for flnm in block_files:
    print(flnm)
    main_block_data.append(dictgenerator(flnm))

with open(blockpost,"w") as afterjob:
    dump_data = json.dumps(main_block_data,indent=4)
    afterjob.write(dump_data)

# print(dictgenerator("azalea_top.png"))
# print(avgimg(block_root+"azalea_top.png"))