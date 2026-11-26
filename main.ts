// news-image-20261125 entry: copy the finished one-page newspaper image
// (entry.png, drawn by draw_entry.py with Python/PIL) to the grader's
// output directory. Node 22, standard library only.
//
// The image sums up Wednesday 25 November 2026 in 19 stories across
// 6 regions and 9 fields, with the Strait of Hormuz tanker mine strikes
// as the lead. It is a static PNG, so the program is just a copy.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
// /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outDir, { recursive: true });
copyFileSync(
  new URL('./entry.png', import.meta.url),
  join(outDir, 'entry.png'),
);
