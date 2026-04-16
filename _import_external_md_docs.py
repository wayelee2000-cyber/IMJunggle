r"""
Import external markdown docs into this static site.

Default source:
  C:\Users\LW\Desktop\IM Platform research\docs\docs

Output:
  - api-md/**/* (copied markdown + assets from source)
  - api-reference.html (tree nav + dynamic Markdown viewer via Marked.js)
"""

from __future__ import annotations

import argparse
import json
import shutil
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DEFAULT_SOURCE = Path(r"C:\Users\LW\Desktop\IM Platform research\docs\docs")
OUT_DIR = ROOT / "api-md"
MD_EXTS = {".md", ".markdown"}

INDEX_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="API reference imported from Markdown files." />
  <title>API Reference — IMJunggle</title>
  <link rel="icon" href="image/logo.svg" type="image/svg+xml" sizes="any" />
  <link rel="stylesheet" href="style.css" />
</head>
<body class="page-api-docs">
  <header class="site-header">
    <a class="logo" href="index.html" target="_top">
      <img class="logo-mark" src="image/logo.svg" alt="" width="36" height="36" decoding="async" />
      <span class="logo-text">IMJunggle</span>
    </a>
    <nav class="nav" aria-label="Primary">
      <a href="product.html" target="_top">Product</a>
      <a href="developers.html" target="_top">Developers</a>
      <a href="pricing.html" target="_top">Pricing</a>
      <a href="docs.html" target="_top">Docs</a>
      <a class="nav-cta" href="index.html#cta" target="_top">Request demo</a>
    </nav>
  </header>

  <main class="site-main">
    <section class="api-docs section" aria-labelledby="api-ref-title">
      <h1 id="api-ref-title" class="section-title">API Reference</h1>
      <div class="api-docs-layout">
        <nav class="api-sidebar api-md-tree" aria-label="Reference tree">
{tree_html}
        </nav>
        <article class="api-main api-md-main">
          <p class="api-md-current" id="api-md-current"></p>
          <div id="api-md-content" class="doc-juggle-body markdown api-md-content"></div>
        </article>
      </div>
    </section>
    <p class="subpage-back"><a href="docs.html" target="_top">← Documentation hub</a></p>
  </main>

  <script id="api-md-index-data" type="application/json">
{index_json}
  </script>
  <script src="https://cdn.jsdelivr.net/npm/marked@11.2.0/marked.min.js"></script>
  <script>
  (function() {{
    var tree = document.querySelector(".api-md-tree");
    var content = document.getElementById("api-md-content");
    var current = document.getElementById("api-md-current");
    var raw = document.getElementById("api-md-index-data");
    if (!tree || !content || !raw) return;

    var docs = [];
    try {{
      docs = JSON.parse((raw.textContent || "[]").replace(/^\\uFEFF/, "").trim());
    }} catch (e) {{
      docs = [];
    }}
    if (!docs.length) {{
      content.innerHTML =
        "<p><strong>Could not load the document index.</strong> The embedded JSON may be invalid. Check the browser console for details.</p>";
      return;
    }}
    if (!window.marked) {{
      content.innerHTML = "<p>Marked.js failed to load.</p>";
      return;
    }}

    marked.setOptions({{
      mangle: false,
      headerIds: true,
      breaks: true,
      gfm: true
    }});

    var parseMd = function (md) {{
      var fn = typeof marked.parse === "function" ? marked.parse.bind(marked) : marked;
      var out = fn(md || "");
      if (out && typeof out.then === "function")
        throw new Error("Marked returned a Promise; check the marked version.");
      return out;
    }};

    function escapeHtmlMdx(s) {{
      return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
    }}

    function escapeAttrMdx(s) {{
      return String(s).replace(/&/g, "&amp;").replace(/"/g, "&quot;");
    }}

    function parseDocusaurusTabHeaders(fullMatch) {{
      var m = fullMatch.match(/values=\\{{\\s*\\[([\\s\\S]*?)\\]\\s*\\}}/);
      var headers = [];
      if (m) {{
        var re = /\\{{\\s*label:\\s*['"]([^'"]+)['"]\\s*,\\s*value:\\s*['"]([^'"]+)['"]\\s*,?\\s*\\}}/g;
        var x;
        while ((x = re.exec(m[1]))) headers.push({{ label: x[1], value: x[2] }});
      }}
      return headers;
    }}

    function parseDocusaurusTabBodies(fullMatch) {{
      var inner = fullMatch.replace(/^<Tabs\\b[^>]*>/i, "").replace(/<\\/Tabs>\\s*$/i, "");
      var byVal = {{}};
      var re = /<TabItem\\s+value=["']([^"']+)["']>\\s*([\\s\\S]*?)\\s*<\\/TabItem>/gi;
      var x;
      while ((x = re.exec(inner))) byVal[x[1]] = x[2].trim();
      return byVal;
    }}

    function buildDocusaurusTabsHtml(fullMatch) {{
      var headers = parseDocusaurusTabHeaders(fullMatch);
      var byVal = parseDocusaurusTabBodies(fullMatch);
      var keys = Object.keys(byVal);
      if (!keys.length) return null;
      if (!headers.length) {{
        headers = keys.map(function(v) {{ return {{ label: v, value: v }}; }});
      }}
      var parts = [];
      parts.push('<div class="mdx-tabs" role="region" aria-label="Tabs">');
      parts.push('<div class="mdx-tab-bar" role="tablist">');
      headers.forEach(function(h, i) {{
        var active = i === 0 ? " is-active" : "";
        parts.push(
          '<button type="button" class="mdx-tab-btn' +
            active +
            '" role="tab" aria-selected="' +
            (i === 0 ? "true" : "false") +
            '" data-mdx-tab="' +
            escapeAttrMdx(h.value) +
            '">' +
            escapeHtmlMdx(h.label) +
            "</button>"
        );
      }});
      parts.push('</div><div class="mdx-tab-panels">');
      headers.forEach(function(h, i) {{
        var body = byVal[h.value] || "";
        var active = i === 0 ? " is-active" : "";
        parts.push(
          '<div class="mdx-tab-panel' +
            active +
            '" role="tabpanel" data-mdx-panel="' +
            escapeAttrMdx(h.value) +
            '"' +
            (i === 0 ? "" : " hidden") +
            ">" +
            parseMd(body) +
            "</div>"
        );
      }});
      parts.push("</div></div>");
      return parts.join("");
    }}

    function renderMdWithMdxTabs(md) {{
      var re = /<Tabs\\b[^>]*>[\\s\\S]*?<\\/Tabs>/gi;
      var out = [];
      var last = 0;
      var m;
      while ((m = re.exec(md))) {{
        out.push(parseMd(md.slice(last, m.index)));
        var tabsHtml = buildDocusaurusTabsHtml(m[0]);
        out.push(tabsHtml || parseMd(m[0]));
        last = re.lastIndex;
      }}
      out.push(parseMd(md.slice(last)));
      return out.join("");
    }}

    function stripFrontMatter(md) {{
      if (!md || md.indexOf("---") !== 0) return md;
      var end = md.indexOf("\\n---", 3);
      if (end === -1) return md;
      return md.slice(end + 4).replace(/^\\s+/, "");
    }}

    function dirname(path) {{
      var i = path.lastIndexOf("/");
      return i === -1 ? "" : path.slice(0, i + 1);
    }}

    function toResolved(basePath, rel) {{
      if (!rel) return rel;
      if (/^(https?:)?\\/\\//i.test(rel) || rel.startsWith("data:") || rel.startsWith("#")) return rel;
      var stack = (dirname(basePath)).split("/").filter(Boolean);
      rel.split("/").forEach(function(part) {{
        if (!part || part === ".") return;
        if (part === "..") stack.pop();
        else stack.push(part);
      }});
      return stack.join("/");
    }}

    function setActive(path) {{
      tree.querySelectorAll("a.is-active").forEach(function(a) {{ a.classList.remove("is-active"); }});
      var current = tree.querySelector('a[data-doc-path="' + path.replace(/"/g, '&quot;') + '"]');
      if (current) {{
        current.classList.add("is-active");
        var p = current.parentElement;
        while (p && tree.contains(p)) {{
          if (p.tagName === "DETAILS") p.open = true;
          p = p.parentElement;
        }}
      }}
    }}

    function rewriteLinksAndMedia(path) {{
      content.querySelectorAll("img[src]").forEach(function(img) {{
        var src = img.getAttribute("src");
        var resolved = toResolved(path, src);
        if (resolved) img.setAttribute("src", resolved);
      }});
      content.querySelectorAll("a[href]").forEach(function(a) {{
        var href = a.getAttribute("href");
        if (!href || href.startsWith("#")) return;
        var resolved = toResolved(path, href);
        if (!resolved) return;
        if (/\\.md($|#|\\?)/i.test(resolved)) {{
          var mdPath = resolved.replace(/\\.md(?=($|#|\\?))/i, ".md");
          a.setAttribute("href", "#" + encodeURIComponent(mdPath));
          a.setAttribute("data-doc-path", mdPath);
          a.removeAttribute("target");
        }} else if (/^(https?:)?\\/\\//i.test(resolved)) {{
          a.setAttribute("href", resolved);
          a.setAttribute("target", "_blank");
          a.setAttribute("rel", "noopener noreferrer");
        }} else {{
          a.setAttribute("href", resolved);
        }}
      }});
    }}

    function resolveDocPath(path) {{
      if (!path) return "";
      if (docs.some(function(d) {{ return d.path === path; }})) return path;
      if (/\.md$/i.test(path)) {{
        var mdxPath = path.replace(/\.md$/i, ".mdx");
        if (docs.some(function(d) {{ return d.path === mdxPath; }})) return mdxPath;
      }}
      if (/\.mdx$/i.test(path)) {{
        var mdPath = path.replace(/\.mdx$/i, ".md");
        if (docs.some(function(d) {{ return d.path === mdPath; }})) return mdPath;
      }}
      return path;
    }}

    var currentDocPath = "";

    function openDoc(path, push) {{
      if (!path) return;
      path = resolveDocPath(path);
      currentDocPath = path;
      var url;
      try {{
        url = new URL(path, window.location.href).href;
      }} catch (e) {{
        url = path;
      }}
      fetch(url)
        .then(function(r) {{
          if (!r.ok) throw new Error("HTTP " + r.status);
          return r.text();
        }})
        .then(function(md) {{
          var clean = stripFrontMatter(md || "");
          var html;
          try {{
            html = renderMdWithMdxTabs(clean);
          }} catch (e) {{
            html = "<p>Failed to render markdown: " + String(e) + "</p>";
          }}
          if (!html || !String(html).trim()) {{
            html =
              "<p>No content was produced for this page. The file may be empty after the front matter, or the Markdown parser returned nothing.</p>";
          }}
          content.innerHTML = html;
          rewriteLinksAndMedia(path);
          if (current) current.textContent = path;
        }})
        .catch(function(err) {{
          var hint =
            window.location.protocol === "file:"
              ? " Opening this page via <code>file://</code> blocks loading other local files. Run the site with the DevServer project (or any local HTTP server) and open <code>api-reference.html</code> over <code>http://</code>."
              : "";
          content.innerHTML =
            "<p>Failed to load markdown: " + String(err) + ".</p><p>" + hint + "</p>";
          if (current) current.textContent = path;
        }});
      setActive(path);
      if (push !== false) {{
        var targetHash = "#" + encodeURIComponent(path);
        if (location.hash === targetHash) return;
        try {{ history.pushState({{ docPath: path }}, "", targetHash); }} catch (e) {{}}
      }}
    }}

    document.addEventListener("click", function(e) {{
      var tabBtn = e.target.closest(".mdx-tab-btn");
      if (tabBtn && content.contains(tabBtn)) {{
        var root = tabBtn.closest(".mdx-tabs");
        if (root) {{
          var val = tabBtn.getAttribute("data-mdx-tab");
          root.querySelectorAll(".mdx-tab-btn").forEach(function(b) {{
            var on = b === tabBtn;
            b.classList.toggle("is-active", on);
            b.setAttribute("aria-selected", on ? "true" : "false");
          }});
          root.querySelectorAll(".mdx-tab-panel").forEach(function(p) {{
            var on = p.getAttribute("data-mdx-panel") === val;
            if (on) p.removeAttribute("hidden"); else p.setAttribute("hidden", "");
            p.classList.toggle("is-active", on);
          }});
        }}
        return;
      }}
      var a = e.target.closest("a[data-doc-path]");
      if (!a) return;
      e.preventDefault();
      openDoc(resolveDocPath(a.getAttribute("data-doc-path")), true);
    }});

    function hashToDocPath() {{
      var raw = (location.hash || "").slice(1);
      if (!raw) return "";
      try {{
        return decodeURIComponent(raw);
      }} catch (e) {{
        return "";
      }}
    }}

    window.addEventListener("hashchange", function() {{
      var h = hashToDocPath();
      var next = h ? resolveDocPath(h) : docs[0].path;
      if (next !== currentDocPath) openDoc(next, false);
    }});

    window.addEventListener("popstate", function() {{
      var h = hashToDocPath();
      var next = h ? resolveDocPath(h) : docs[0].path;
      if (next !== currentDocPath) openDoc(next, false);
    }});

    var initial = hashToDocPath();
    openDoc(initial ? resolveDocPath(initial) : docs[0].path, false);
  }})();
  </script>
</body>
</html>
"""


def ensure_inside(base: Path, child: Path) -> None:
    child.resolve().relative_to(base.resolve())


def nice_label(segment: str) -> str:
    txt = segment.replace("_", " ").replace("-", " ").strip()
    return txt if txt else segment


def add_to_tree(root: dict, rel_parts: list[str], path: str, title: str) -> None:
    node = root
    for part in rel_parts[:-1]:
        children = node.setdefault("children", {})
        node = children.setdefault(part, {"kind": "dir", "name": part, "children": {}})
    node.setdefault("files", []).append({"name": rel_parts[-1], "path": path, "title": title})


def render_tree(node: dict, depth: int = 0) -> str:
    lines: list[str] = []
    if depth == 0:
        lines.append('<ul class="api-md-tree-root">')
    else:
        lines.append("<ul>")

    for dname in sorted(node.get("children", {}).keys()):
        child = node["children"][dname]
        lines.append("<li>")
        lines.append(f'<details{" open" if depth < 2 else ""}><summary>{escape(nice_label(dname))}</summary>')
        lines.append(render_tree(child, depth + 1))
        lines.append("</details></li>")

    for f in sorted(node.get("files", []), key=lambda x: x["name"]):
        lines.append(
            f'<li><a href="#{escape(f["path"])}" data-doc-path="{escape(f["path"])}">{escape(nice_label(f["name"]))}</a></li>'
        )

    lines.append("</ul>")
    return "\n".join(lines)


def write_index(items: list[dict[str, str]]) -> None:
    tree_root: dict = {}
    for it in items:
        rel_parts = it["rel_no_ext"].split("/")
        add_to_tree(tree_root, rel_parts, it["path"], it["title"])
    tree_html = render_tree(tree_root)
    index_json = json.dumps([{"path": it["path"], "title": it["title"]} for it in items], ensure_ascii=False, indent=2)
    html = INDEX_PAGE.format(tree_html=tree_html, index_json=index_json)
    (ROOT / "api-reference.html").write_text(html, encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    args = ap.parse_args()

    src = args.source
    if not src.exists():
        raise SystemExit(f"Source not found: {src}")

    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    copied_assets = 0
    copied_md = 0
    created: list[dict[str, str]] = []
    for f in src.rglob("*"):
        if not f.is_file():
            continue
        rel = f.relative_to(src)
        if f.suffix.lower() in MD_EXTS:
            rel_out = rel.with_suffix(".md")
            copied_md += 1
        else:
            rel_out = rel
            copied_assets += 1
        dest = OUT_DIR / rel_out
        ensure_inside(OUT_DIR, dest)
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(f, dest)
        if f.suffix.lower() in MD_EXTS:
            created.append(
                {
                    "rel_no_ext": str(rel.with_suffix("")).replace("\\", "/"),
                    "path": str(dest.relative_to(ROOT)).replace("\\", "/"),
                    "title": nice_label(rel.stem),
                }
            )

    write_index(created)
    print(f"Imported {len(created)} markdown files into {OUT_DIR.relative_to(ROOT)}/")
    print(f"Copied {copied_md} markdown files")
    print(f"Copied {copied_assets} non-markdown assets")
    print("Wrote api-reference.html (tree + Marked.js dynamic viewer)")


if __name__ == "__main__":
    main()
