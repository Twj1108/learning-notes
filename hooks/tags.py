from urllib.parse import quote


def on_page_markdown(markdown, page, config, files):
    """在每页顶部渲染 front matter 中 tags 字段对应的关键词标签。"""
    meta = getattr(page, "meta", None) or {}
    tags = meta.get("tags", [])
    if not tags:
        return markdown

    site_url = str(config.get("site_url", "")).rstrip("/")
    chips = []
    for tag in tags:
        href = f"{site_url}/?q={quote(str(tag), safe='')}"
        chips.append(f'<a class="kw-chip" href="{href}">{tag}</a>')

    row = '<div class="kw-row"><span class="kw-label">关键词</span>' + "".join(chips) + "</div>\n\n"
    return row + markdown
