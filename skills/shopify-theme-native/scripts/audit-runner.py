"""Bounded Shopify SEO/GEO tools in an isolated Python runtime."""
import argparse
import os
from pathlib import Path
import subprocess
import sys
import venv

ROOT = Path(__file__).resolve().parents[1]
ALLOWED = {
    'seo': {'fetch_page.py', 'parse_html.py', 'schema_ecommerce_validate.py', 'sitemap_discovery.py', 'content_verify.py'},
    'geo': {'fetch_page.py', 'citability_scorer.py', 'llmstxt_generator.py', 'brand_scanner.py'},
}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--setup', action='store_true')
    parser.add_argument('source', nargs='?', choices=sorted(ALLOWED))
    parser.add_argument('script', nargs='?')
    parser.add_argument('args', nargs=argparse.REMAINDER)
    opts = parser.parse_args()
    runtime = Path(os.environ.get('SHOPIFY_NATIVE_TOOLS', str(Path.home() / '.codex/tools/shopify-theme-native')))
    envdir = runtime / 'python'
    python = envdir / ('Scripts/python.exe' if os.name == 'nt' else 'bin/python')
    if opts.setup:
        if not python.exists():
            venv.EnvBuilder(with_pip=True).create(envdir)
        subprocess.run([str(python), '-m', 'pip', 'install', '-r', str(ROOT / 'assets/runtime/requirements.txt')], check=True)
    if not opts.source:
        if opts.setup: return
        parser.error('Choose a source and script')
    if opts.script not in ALLOWED[opts.source]:
        parser.error('Unsupported script')
    if not python.exists(): parser.error('Run --setup first')
    upstream = ROOT / 'vendor' / opts.source
    env = {**os.environ, 'PYTHONUTF8': '1', 'CLAUDE_PLUGIN_ROOT': str(upstream)}
    result = subprocess.run([str(python), str(upstream / 'scripts' / opts.script), *opts.args], env=env)
    raise SystemExit(result.returncode)

if __name__ == '__main__': main()
