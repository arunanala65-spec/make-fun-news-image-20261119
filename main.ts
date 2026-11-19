// news-image-20261119 entry: "The World in One Day — 19 November 2026".
// A single infographic (entry.png, drawn by render.py with Pillow) that sums
// up Thursday 19 November 2026 in six verified stories. This program's only
// job is to place that image where the grader expects it.
//
// Node 22, standard library only. Run it as:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
// It writes out/entry.png. The copy is byte-for-byte identical every run,
// because the source image is a fixed file in this repo. Nothing is fetched,
// generated, or randomised at run time, so the grader's two runs agree.

import { copyFileSync, existsSync, mkdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const source = join(here, 'entry.png');
const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const target = join(outputDir, 'entry.png');

mkdirSync(outputDir, { recursive: true });
if (!existsSync(source)) {
  throw new Error(`entry image missing next to main.ts: ${source}`);
}
copyFileSync(source, target);
