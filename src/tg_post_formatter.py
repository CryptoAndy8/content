# Formats Telegram posts and enforces short hyphens only
def sanitize(text: str) -> str:
    return text.replace("—", "-").replace("–", "-")

def render_post(title: str, bullets: list[str], links: list[str] = None) -> str:
    title = sanitize(title)
    bullets = [f"- {sanitize(b)}" for b in bullets]
    links = links or []
    out = [title, ""]
    out += bullets
    if links:
        out += ["", "Links:"] + [f"- {l}" for l in links]
    out += ["", "Not financial advice."]
    return "\n".join(out).strip()

if __name__ == "__main__":
    post = render_post(
        "Linea - Plasma - quick update",
        ["Official listings are live.",
         "Plasma ~2x from listing, ~20x from sale.",
         "Check LXP on Owlto before TGE."],
        ["https://owlto.finance/tracker/lxp"]
    )
    print(post)
