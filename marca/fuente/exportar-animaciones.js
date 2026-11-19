// Graba cada animación cuadro a cuadro y la convierte a MP4 y GIF con ffmpeg.
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path'); const { execFileSync } = require('child_process');
const R = path.resolve(__dirname, '..'); const hd = path.join(R, 'animaciones', 'html'); const tmp = process.env.TMPDIR_ANIM || path.join(require('os').tmpdir(), 'lq-anim');
const GIF = { 'logo-entrada': 540, 'loqui-vivo': 480, cargando: 300, 'loqui-expresiones': 360 };
(async () => {
  const b = await chromium.launch();
  for (const d of ['mp4', 'gif']) fs.mkdirSync(path.join(R, 'animaciones', d), { recursive: true });
  for (const f of fs.readdirSync(hd).filter((x) => x.endsWith('.html'))) {
    const n = f.replace('.html', ''); const p = await b.newPage(); await p.goto('file://' + path.join(hd, f)); await p.evaluate(() => document.fonts.ready);
    const { w, h, dur } = await p.evaluate(() => ({ w: +document.body.dataset.w, h: +document.body.dataset.h, dur: +document.body.dataset.dur }));
    await p.setViewportSize({ width: w, height: h }); const dir = path.join(tmp, n); fs.rmSync(dir, { recursive: true, force: true }); fs.mkdirSync(dir, { recursive: true });
    await p.evaluate(() => document.getAnimations().forEach((a) => a.pause()));
    const total = Math.round(dur * 30);
    for (let i = 0; i < total; i++) {
      await p.evaluate((t) => document.getAnimations().forEach((a) => { a.currentTime = t; }), (i / 30) * 1000);
      await p.screenshot({ path: path.join(dir, String(i).padStart(4, '0') + '.jpg'), type: 'jpeg', quality: 92 });
    }
    await p.close();
    execFileSync('ffmpeg', ['-loglevel', 'error', '-y', '-framerate', '30', '-i', path.join(dir, '%04d.jpg'), '-c:v', 'libx264', '-crf', '18', '-preset', 'veryfast', '-pix_fmt', 'yuv420p', path.join(R, 'animaciones', 'mp4', n + '.mp4')]);
    if (GIF[n]) execFileSync('ffmpeg', ['-loglevel', 'error', '-y', '-framerate', '30', '-i', path.join(dir, '%04d.jpg'), '-vf', `fps=15,scale=${GIF[n]}:-1:flags=lanczos,split[a][b];[a]palettegen=max_colors=64[p];[b][p]paletteuse=dither=bayer:bayer_scale=4`, path.join(R, 'animaciones', 'gif', n + '.gif')]);
    console.log(n, total, 'cuadros');
  }
  await b.close();
})();
