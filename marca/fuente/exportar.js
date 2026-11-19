// Exporta logos, mascota, iconos y patrones a PNG, y las plantillas a PDF y PNG.
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
const R = path.resolve(__dirname, '..');
(async () => {
  const b = await chromium.launch();
  const png = async (dir, ancho) => {
    const src = path.join(R, dir, 'svg'), dst = path.join(R, dir, 'png'); fs.mkdirSync(dst, { recursive: true });
    for (const f of fs.readdirSync(src).filter((x) => x.endsWith('.svg'))) {
      const s = fs.readFileSync(path.join(src, f), 'utf8'); const m = /width="([\d.]+)" height="([\d.]+)"/.exec(s); const w = +m[1], h = +m[2], k = ancho / w;
      const p = await b.newPage({ viewport: { width: Math.round(ancho), height: Math.round(h * k) } });
      await p.setContent(`<body style="margin:0">${s.replace(/width="[\d.]+" height="[\d.]+"/, 'style="display:block;width:100vw;height:100vh"')}</body>`);
      await p.screenshot({ path: path.join(dst, f.replace('.svg', '.png')), omitBackground: true }); await p.close();
    }
  };
  if (process.argv[2] !== 'plantillas') { await png('logo', 2000); await png('mascota', 1200); await png('iconos', 512); await png('patrones', 1600); }
  const hd = path.join(R, 'plantillas', 'html');
  for (const d of ['pdf', 'png']) fs.mkdirSync(path.join(R, 'plantillas', d), { recursive: true });
  for (const f of fs.readdirSync(hd).filter((x) => x.endsWith('.html'))) {
    const p = await b.newPage(); await p.goto('file://' + path.join(hd, f)); await p.evaluate(() => document.fonts.ready);
    const { w, h, u } = await p.evaluate(() => { const e = document.querySelector('.hoja'); return { w: +e.dataset.w, h: +e.dataset.h, u: e.dataset.u }; });
    const px = u === 'mm' ? 96 / 25.4 : 1, W = Math.round(w * px), H = Math.round(h * px), esc = Math.min(3, Math.max(1, 2400 / Math.max(W, H)));
    await p.pdf({ path: path.join(R, 'plantillas', 'pdf', f.replace('.html', '.pdf')), width: w + u, height: h + u, printBackground: true, pageRanges: '1' });
    await p.close();
    const q = await b.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: u === 'px' ? 1 : esc }); await q.goto('file://' + path.join(hd, f)); await q.evaluate(() => document.fonts.ready); await q.waitForTimeout(150);
    await q.screenshot({ path: path.join(R, 'plantillas', 'png', f.replace('.html', '.png')) }); await q.close();
  }
  await b.close(); console.log('exportado');
})();
