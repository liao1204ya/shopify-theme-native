import { createRequire } from 'node:module';
import { homedir } from 'node:os';
import { join } from 'node:path';
import { spawnSync } from 'node:child_process';
const root = process.env.SHOPIFY_NATIVE_TOOLS || join(homedir(), '.codex', 'tools', 'shopify-theme-native');
const require = createRequire(join(root, 'package.json'));
const [tool, ...args] = process.argv.slice(2);
let executable = process.execPath;
let callArgs;
try {
  if (tool === 'lighthouse') callArgs = [join(root, 'node_modules/lighthouse/cli/index.js'), ...args];
  else if (tool === 'gemini') callArgs = [join(root, 'node_modules/@pilio/gemini-watermark-remover/bin/gwr.mjs'), ...args];
  else if (tool === 'exiftool') {
    const bin = require(process.platform === 'win32' ? 'exiftool-vendored.exe' : 'exiftool-vendored.pl');
    executable = typeof bin === 'string' ? bin : bin.default;
    callArgs = args;
  } else throw new Error('Choose lighthouse, gemini, or exiftool');
  const result = spawnSync(executable, callArgs, { stdio: 'inherit', shell: false });
  if (result.error) throw result.error;
  process.exitCode = result.status ?? 1;
} catch (error) { console.error(error.message); process.exitCode = 1; }
