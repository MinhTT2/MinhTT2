"""Render an original, seamless basketball loop with NumPy and Pillow.

No external media, fonts, logos, or image-generation services are used.
"""
from pathlib import Path
import math
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / 'assets'
SIZE = 320
FRAMES = 60


def render(phase, size=SIZE):
    yy, xx = np.mgrid[:size, :size].astype(float)
    xx /= size
    yy /= size
    # A quiet midnight stage, matching GitHub's dark default background.
    glow = np.exp(-(((xx-.48)/.42)**2 + ((yy-.54)/.52)**2)*2)
    background = np.zeros((size, size, 3)) + [13, 17, 23]
    background += glow[..., None] * np.array([1, 4, 9])
    frame = Image.fromarray(np.uint8(background))
    floor = .84*size
    bounce = 4*phase*(1-phase)
    impact = math.exp(-(min(phase, 1-phase)/.035)**2)
    radius = .235*size
    rx = radius*(1+.065*impact)
    ry = radius*(1-.055*impact)
    cy = floor-ry-.245*size*bounce
    cx = .5*size

    shadow = Image.new('RGBA', (size, size))
    sd = ImageDraw.Draw(shadow)
    spread = radius*(.88+.24*bounce)
    alpha = round(115-65*bounce)
    sd.ellipse((cx-spread, floor-.035*size, cx+spread, floor+.035*size),
               fill=(0, 0, 0, alpha))
    shadow = shadow.filter(ImageFilter.GaussianBlur(size*(.016+.02*bounce)))
    frame = Image.alpha_composite(frame.convert('RGBA'), shadow)

    y, x = np.mgrid[:size, :size].astype(float)
    x = (x-cx)/rx
    y = (y-cy)/ry
    rr = x*x+y*y
    z = np.sqrt(np.maximum(0, 1-rr))
    # Rotate the spherical material, while lighting stays fixed in the room.
    tilt = .37
    xt = math.cos(tilt)*x-math.sin(tilt)*y
    yt = math.sin(tilt)*x+math.cos(tilt)*y
    angle = 2*math.pi*phase+.5
    u = math.cos(angle)*xt + math.sin(angle)*z
    v = yt
    w = -math.sin(angle)*xt + math.cos(angle)*z
    # Two great-circle seams and two curved side seams form the ball panels.
    distance = np.minimum.reduce([np.abs(u), np.abs(v),
                                  np.abs(w-.68), np.abs(w+.68)])
    seam = np.clip((.023-distance)/.009, 0, 1)
    # Fine pebbled rubber texture, anchored to the rotating sphere.
    grain = np.sin(u*245+np.sin(v*93))*np.sin(v*238+w*111)
    pebble = .965+.035*grain
    key = np.maximum(0, -.47*x-.62*y+.63*z)
    light = .21+.77*key
    color = np.zeros((size, size, 3)) + [220, 88, 27]
    color *= (light*pebble)[..., None]
    specular = np.maximum(0, -.29*x-.44*y+.85*z)**38
    color += specular[..., None]*np.array([35, 23, 12])
    rim = np.maximum(0, x*.8-y*.13)*(1-z)**2
    color += rim[..., None]*np.array([15, 28, 55])
    groove = np.stack([light*17, light*14, light*13], axis=-1)
    color = color*(1-seam[..., None]) + groove*seam[..., None]
    edge = np.clip((1-np.sqrt(rr))*radius, 0, 1)
    ball = Image.fromarray(np.dstack([np.uint8(np.clip(color, 0, 255)),
                                      np.uint8(edge*255)]))
    return Image.alpha_composite(frame, ball).convert('RGB')


if __name__ == '__main__':
    frames = [render(i/FRAMES) for i in range(FRAMES)]
    # One shared palette prevents background flicker between GIF frames.
    sheet = Image.new('RGB', (SIZE*10, SIZE*6))
    for i, frame in enumerate(frames):
        sheet.paste(frame, ((i % 10)*SIZE, (i//10)*SIZE))
    palette = sheet.quantize(colors=128)
    frames = [frame.quantize(palette=palette, dither=Image.Dither.NONE)
              for frame in frames]
    durations = [40, 40, 40, 40, 40, 50]*10
    frames[0].save(ASSETS/'basketball-loop.gif', save_all=True,
                   append_images=frames[1:], duration=durations,
                   loop=0, optimize=True, disposal=1)
    render(.32, 640).save(ASSETS/'basketball-poster.png', optimize=True)
    print('Rendered basketball-loop.gif and basketball-poster.png')
