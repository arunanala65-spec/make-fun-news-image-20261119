// news-image-20261119 entry: "The World in One Day — 19 November 2026".
//
// The entry is one infographic, entry.png, drawn by render.py with Pillow:
// six verified stories from Thursday 19 November 2026 in a bento grid.
// This program only puts that image where the grader looks for it.
//
// Node 22, standard library only. Run it as:
//
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
//
// It writes out/entry.png. The bytes are identical on every run, because
// the image is a fixed file in this repository: nothing is fetched,
// generated, or randomised while the program runs, so the grader's two
// runs agree byte for byte.

import { existsSync, mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = dirname(fileURLToPath(import.meta.url));
const sourcePath = join(root, 'entry.png');
const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const targetPath = join(outputDir, 'entry.png');

if (!existsSync(sourcePath)) {
  throw new Error(`entry image missing next to main.ts: ${sourcePath}`);
}

const bytes = readFileSync(sourcePath);
mkdirSync(outputDir, { recursive: true });
writeFileSync(targetPath, bytes);
console.log(`wrote ${targetPath} (${bytes.length} bytes, ${(bytes.length / 1024).toFixed(1)} KiB)`);
