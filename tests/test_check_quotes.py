from src.check_quotes import check_record, classify, html_texts, normalize, score_quote

PAGE = """<html><head><meta name="description" content="Early-stage VC fund from Prague."></head>
<body><nav>Menu</nav><article><h1>About</h1>
<p>Example&nbsp;Ventures invests in B2B software and fintech. Our first cheque is typically
EUR 100k to 750k.</p><p>We lead pre-seed and seed rounds across Central and Eastern Europe, with a team based in Prague and Brno.</p>
<p>„Investujeme do zakladatelů“ – říká partner.</p></article><script>var x = "hidden quote text";</script></body></html>"""


def texts():
    return html_texts(PAGE)


def test_normalize_unifies_spaces_quotes_and_case():
    assert normalize("A B  “C”–D") == 'a b "c"-d'


def test_exact_quote_found():
    assert classify(score_quote("Our first cheque is typically EUR 100k to 750k.", texts())) == "found"


def test_quote_across_line_break_found():
    assert classify(score_quote("cheque is typically EUR 100k to 750k", texts())) == "found"


def test_meta_description_counts():
    assert classify(score_quote("Early-stage VC fund from Prague", texts())) == "found"


def test_paraphrase_not_found():
    s = score_quote("The fund typically writes initial tickets between one and five million euros.", texts())
    assert classify(s) == "missing"


def test_wrong_number_lowers_score():
    good = score_quote("first cheque is typically EUR 100k to 750k", texts())
    bad = score_quote("first cheque is typically EUR 300k to 950k", texts())
    assert bad < good


def test_ellipsis_fragments_each_checked():
    assert classify(score_quote("invests in B2B software ... team based in Prague and Brno", texts())) == "found"
    assert classify(score_quote("invests in B2B software ... team based in Vienna and Graz", texts())) != "found"


def test_script_text_ignored():
    assert classify(score_quote("var x = hidden quote text", texts())) == "missing"


def test_czech_typographic_quotes():
    assert classify(score_quote('"Investujeme do zakladatelů" - říká partner.', texts())) == "found"


def test_check_record_marks_unreachable():
    rec = {"id": "x", "type": {"value": "vc", "source": {"url": "https://a.example/", "quote": "Early-stage VC fund"}},
           "evidence_of_activity": [{"source": {"url": "https://b.example/", "quote": "anything"}}]}
    pages = {"https://a.example/": {"texts": texts(), "http_status": 200, "note": ""},
             "https://b.example/": {"texts": [], "http_status": 403, "note": "HTTP 403"}}
    out = check_record(rec, pages)
    st = {it["path"]: it["status"] for it in out["items"]}
    assert st == {"type": "found", "evidence_of_activity[0]": "unreachable"}
