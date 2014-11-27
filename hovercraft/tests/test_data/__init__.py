HTML_OUTPUTS = {

    'simple': (
        b'<!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml"><body><div '
        b'id="impress"><div class="step step-level-1" step="0" '
        b'data-rotate-x="0" data-rotate-y="0" data-rotate-z="0" data-scale="1" '
        b'data-x="0" data-y="0" data-z="0"><h1 id="simple-presentation">Simple '
        b'Presentation</h1><p>This presentation has two slides, each with a '
        b'header and some text.</p></div><div class="step step-level-1" '
        b'step="1" data-rotate-x="0" data-rotate-y="0" data-rotate-z="0" '
        b'data-scale="1" data-x="1600" data-y="0" data-z="0"><h1 '
        b'id="second-slide">Second slide</h1><p>There is no positioning or '
        b'anything fancy.</p></div></div><script type="text/javascript" '
        b'src="js/impress.js"></script><script type="text/javascript" '
        b'src="js/hovercraft-minimal.js"></script></body></html>'
    ),

    'extra_css': (
        b'<!DOCTYPE html SYSTEM "about:legacy-compat"><html '
        b'xmlns="http://www.w3.org/1999/xhtml"><head><title></title><link '
        b'rel="stylesheet" href="css/style.css" media="all"></link><link '
        b'rel="stylesheet" href="css/print.css" media="print"></link><link '
        b'rel="stylesheet" href="css/impressConsole.css" '
        b'media="screen,projection"></link><link rel="stylesheet" '
        b'href="extra.css" media="all"></link><script type="text/javascript" '
        b'src="js/dummy.js"></script></head><body '
        b'class="impress-not-supported"><div id="impress"><div class="step '
        b'step-level-1" step="0" data-rotate-x="0" data-rotate-y="0" '
        b'data-rotate-z="0" data-scale="1" data-x="0" data-y="0" data-z="0"><h1 '
        b'id="simple-presentation">Simple Presentation</h1><p>This presentation '
        b'has two slides, each with a header and some text.</p></div><div '
        b'class="step step-level-1" step="1" data-rotate-x="0" '
        b'data-rotate-y="0" data-rotate-z="0" data-scale="1" data-x="1600" '
        b'data-y="0" data-z="0"><h1 id="second-slide">Second '
        b'slide</h1><p>There is no positioning or anything '
        b'fancy.</p></div></div><div id="hovercraft-help" '
        b'class="show"><table><tr><th>Left, Down, Page Down, Space</th><td>Next '
        b'slide</td></tr><tr><th>Right, Up, Page Up</th><td>Previous '
        b'slide</td></tr><tr><th>H</th><td>Toggle this '
        b'help</td></tr></table></div><script type="text/javascript" '
        b'src="js/impress.js"></script><script type="text/javascript" '
        b'src="js/impressConsole.js"></script><script type="text/javascript" '
        b'src="js/hovercraft.js"></script></body></html>'
    ),

    'advanced': (
        b'<!DOCTYPE html SYSTEM "about:legacy-compat"><html '
        b'xmlns="http://www.w3.org/1999/xhtml"><head><title>Presentation '
        b'title</title><link rel="stylesheet" href="css/style.css" '
        b'media="all"></link><link rel="stylesheet" href="css/print.css" '
        b'media="print"></link><link rel="stylesheet" '
        b'href="css/impressConsole.css" media="screen,projection"></link>'
        b'<link rel="stylesheet" href="extra.css" media="screen"></link>'
        b'<script type="text/javascript" src="js/dummy.js"></script></head>'
        b'<body class="impress-not-supported"><div id="impress" '
        b'data-transition-duration="2000" auto-console="True"><div class="step '
        b'step-level-1" step="0" data-x="1000" data-y="1600" data-rotate-x="0" '
        b'data-rotate-y="0" data-rotate-z="0" data-scale="1" '
        b'data-z="0"><h1 id="advanced-presentation">Advanced Presentation'
        b'</h1><p>Here we show the positioning feature, where we can '
        b'explicitly set a position\non one of the steps.</p></div><div '
        b'class="step step-level-1" step="1" id="name-this-step" data-x="2600" '
        b'data-rotate-x="0" data-rotate-y="0" data-rotate-z="0" data-scale="1" '
        b'data-y="1600" data-z="0"><h1 '
        b'id="formatting">Formatting</h1><p>Let us also try some basic '
        b'formatting, like <em>italic</em>, and <strong>bold</strong>.</p><ul>'
        b'<li>We can also</li><li>have a list</li><li>of things.</li></ul>'
        b'</div><div class="step step-level-1" step="2" data-rotate-x="0" '
        b'data-rotate-y="0" data-rotate-z="0" data-scale="1" data-x="4200" '
        b'data-y="1600" data-z="0"><p>There should also be possible to '
        b'have\npreformatted text for code.</p><pre class="highlight code '
        b'python"><span class="k">def</span> <span class="nf">foo</span>'
        b'<span class="p">(</span><span class="n">bar</span><span '
        b'class="p">):</span>\n    <span class="c"># Comment</span>\n    <span '
        b'class="n">a</span> <span class="o">=</span> <span '
        b'class="mi">1</span> <span class="o">+</span> <span '
        b'class="s">"hubbub"</span>\n    <span class="k">return</span> <span '
        b'class="bp">None</span></pre></div><div class="step step-level-1" '
        b'step="3" data-rotate-x="0" data-rotate-y="0" data-rotate-z="0" '
        b'data-scale="1" data-x="5800" data-y="1600" data-z="0"><p>An image, '
        b'with attributes:</p><img src="images/python-logo-master-v3-TM.png" '
        b'width="50%" class="imageclass"></img></div><div class="step '
        b'step-level-1" step="4" data-rotate-x="0" data-rotate-y="0" '
        b'data-rotate-z="0" data-scale="1" data-x="7400" data-y="1600" '
        b'data-z="0"><h1 id="character-sets">Character sets</h1><p>The '
        b'character set is UTF-8 as of now. Like this: &#xE5;&#xE4;&#xF6;.</p>'
        b'</div></div><div id="hovercraft-help" class="show"><table><tr>'
        b'<th>Left, Down, Page Down, Space</th><td>Next slide</td></tr><tr>'
        b'<th>Right, Up, Page Up</th><td>Previous slide</td></tr><tr>'
        b'<th>H</th><td>Toggle this help</td></tr></table></div><script '
        b'type="text/javascript" src="js/impress.js"></script><script '
        b'type="text/javascript" src="js/impressConsole.js"></script><script '
        b'type="text/javascript" src="js/hovercraft.js"></script></body>'
        b'</html>'
    ),

    'default-template': (
        b'<!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml"><head>'
        b'<title>Presentation title</title><meta name="generator" '
        b'content="Hovercraft! 1.0 http://regebro.github.com/hovercraft"></meta>'
        b'<link rel="stylesheet" href="css/hovercraft.css" media="all"></link>'
        b'<link rel="stylesheet" href="css/impressConsole.css" media="all">'
        b'</link><link rel="stylesheet" href="css/highlight.css" media="all">'
        b'</link><link rel="stylesheet" href="extra.css" media="screen"></link>'
        b'</head><body class="impress-not-supported"><div id="impress" '
        b'data-transition-duration="2000" auto-console="True">'
        b'<div class="step step-level-1" step="0" data-x="1000" '
        b'data-y="1600" data-rotate-x="0" data-rotate-y="0" data-rotate-z="0" '
        b'data-scale="1" data-z="0"><h1 id="advanced-presentation">Advanced '
        b'Presentation</h1><p>Here we show the positioning feature, where we can '
        b'explicitly set a position\non one of the steps.</p></div><div '
        b'class="step step-level-1" step="1" id="name-this-step" data-x="2600" '
        b'data-rotate-x="0" data-rotate-y="0" data-rotate-z="0" data-scale="1" '
        b'data-y="1600" data-z="0"><h1 id="formatting">Formatting</h1><p>Let us also try '
        b'some basic formatting, like <em>italic</em>, and <strong>bold</strong>'
        b'.</p><ul><li>We can also</li><li>have a list</li><li>of things.</li>'
        b'</ul></div><div class="step step-level-1" step="2" data-rotate-x="0" '
        b'data-rotate-y="0" data-rotate-z="0" data-scale="1" data-x="4200" '
        b'data-y="1600" data-z="0"><p>There should also be possible to have\npreformatted '
        b'text for code.</p><pre class="highlight code python"><span class="k">'
        b'def</span> <span class="nf">foo</span><span class="p">(</span><span '
        b'class="n">bar</span><span class="p">):</span>\n    <span class="c">'
        b'# Comment</span>\n    <span class="n">a</span> <span class="o">='
        b'</span> <span class="mi">1</span> <span class="o">+</span> <span '
        b'class="s">"hubbub"</span>\n    <span class="k">return</span> '
        b'<span class="bp">None</span></pre></div><div class="step step-level-1" '
        b'step="3" data-rotate-x="0" data-rotate-y="0" data-rotate-z="0" '
        b'data-scale="1" data-x="5800" data-y="1600" data-z="0"><p>An image, with attributes:</p>'
        b'<img src="images/python-logo-master-v3-TM.png" width="50%" '
        b'class="imageclass"></img></div><div class="step step-level-1" step="4" '
        b'data-rotate-x="0" data-rotate-y="0" data-rotate-z="0" data-scale="1" '
        b'data-x="7400" data-y="1600" data-z="0"><h1 id="character-sets">Character sets</h1>'
        b'<p>The character set is UTF-8 as of now. Like this: '
        b'&#xE5;&#xE4;&#xF6;.</p></div></div>'
        b'<div id="hovercraft-help"><table><tr><th>Space</th><td>Forward</td>'
        b'</tr><tr><th>Right, Down, Page Down</th><td>Next slide</td></tr>'
        b'<tr><th>Left, Up, Page Up</th><td>Previous slide</td></tr>'
        b'<tr><th>P</th><td>Open presenter console</td></tr>'
        b'<tr><th>H</th><td>Toggle this help</td></tr></table></div>'
        b'<script type="text/javascript" src="js/impress.js"></script><script '
        b'type="text/javascript" src="js/impressConsole.js"></script><script '
        b'type="text/javascript" src="js/hovercraft.js"></script></body></html>'
    ),

    'presenter-notes': (
        b'<!DOCTYPE html SYSTEM "about:legacy-compat"><html '
        b'xmlns="http://www.w3.org/1999/xhtml"><head><title>Document '
        b'title</title><link rel="stylesheet" href="css/style.css" '
        b'media="all"></link><link rel="stylesheet" href="css/print.css" '
        b'media="print"></link><link rel="stylesheet" '
        b'href="css/impressConsole.css" media="screen,projection"></link>'
        b'<script type="text/javascript" src="js/dummy.js"></script></head>'
        b'<body class="impress-not-supported"><div id="impress"><div '
        b'class="step step-level-1" step="0" data-rotate-x="0" '
        b'data-rotate-y="0" data-rotate-z="0" data-scale="1" data-x="0" '
        b'data-y="0" data-z="0"><h1 '
        b'id="hovercrafts-presenter-notes">Hovercrafts presenter notes</h1>'
        b'<p>Hovercraft! supports presenter notes. It does this by taking '
        b'anything in a\nwhat is calles a "notes-admonition" and making that '
        b'into presenter notes.</p><div class="notes"><p>Hence, this will '
        b'show up as presenter notes.\nYou have still access to a lot of '
        b'formatting, like</p><ul><li>Bullet lists</li><li>And <em>all</em> '
        b'types of <strong>inline formatting</strong></li></ul></div></div>'
        b'<div class="step step-level-1" step="1" data-rotate-x="0" '
        b'data-rotate-y="0" data-rotate-z="0" data-scale="1" data-x="1600" '
        b'data-y="0" data-z="0"><img '
        b'src="images/python-logo-master-v3-TM.png"></img><div class="notes">'
        b'<p>You don\'t have to start the text on the same line as\nthe note, '
        b'but you can.</p><p>You can also have several paragraphs. You can not '
        b'have any\nheadings of any kind though.</p><p><strong>But you can '
        b'fake them through bold-text</strong></p><p>And that\'s useful '
        b'enough for presentation notes.</p></div></div></div><div '
        b'id="hovercraft-help" class="show"><table><tr><th>Left, Down, Page '
        b'Down, Space</th><td>Next slide</td></tr><tr><th>Right, Up, Page '
        b'Up</th><td>Previous slide</td></tr><tr><th>H</th><td>Toggle this '
        b'help</td></tr></table></div><script type="text/javascript" '
        b'src="js/impress.js"></script><script type="text/javascript" '
        b'src="js/impressConsole.js"></script><script type="text/javascript" '
        b'src="js/hovercraft.js"></script></body></html>'
    ),

    'skip-presenter-notes': (
        b'<!DOCTYPE html SYSTEM "about:legacy-compat"><html '
        b'xmlns="http://www.w3.org/1999/xhtml"><head><title>Document title'
        b'</title><link rel="stylesheet" href="css/style.css" media="all">'
        b'</link><link rel="stylesheet" href="css/print.css" '
        b'media="print"></link><link rel="stylesheet" '
        b'href="css/impressConsole.css" '
        b'media="screen,projection"></link><script type="text/javascript" '
        b'src="js/dummy.js"></script></head><body '
        b'class="impress-not-supported"><div id="impress">'
        b'<div class="step step-level-1" step="0" data-rotate-x="0" '
        b'data-rotate-y="0" data-rotate-z="0" data-scale="1" data-x="0" '
        b'data-y="0" data-z="0">'
        b'<h1 id="hovercrafts-presenter-notes">Hovercrafts presenter '
        b'notes</h1><p>Hovercraft! supports presenter notes. It does this by '
        b'taking anything in a\nwhat is calles a "notes-admonition" and making '
        b'that into presenter notes.</p></div>'
        b'<div class="step step-level-1" step="1" data-rotate-x="0" '
        b'data-rotate-y="0" data-rotate-z="0" data-scale="1" data-x="1600" '
        b'data-y="0" data-z="0">'
        b'<img '
        b'src="images/python-logo-master-v3-TM.png">'
        b'</img></div></div><div id="hovercraft-help" class="show"><table><tr>'
        b'<th>Left, Down, Page Down, Space</th><td>Next slide</td></tr><tr>'
        b'<th>Right, Up, Page Up</th><td>Previous slide</td></tr><tr><th>H</th>'
        b'<td>Toggle this help</td></tr></table></div><script type="text/javascript" '
        b'src="js/impress.js"></script><script type="text/javascript" '
        b'src="js/impressConsole.js"></script><script type="text/javascript" '
        b'src="js/hovercraft.js"></script></body></html>'
    ),

    'table': (
        b'<!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml">'
        b'<body><div id="impress">'
        b'<div class="step step-level-1" step="0" data-rotate-x="0" '
        b'data-rotate-y="0" data-rotate-z="0" data-scale="1" data-x="0" '
        b'data-y="0" data-z="0">'
        b'<table cellpadding="0" cellspacing="0" class="my-table-class">'
        b'Truth table for "not"'
        b'<thead><tr><th><p>Name</p></th><th><p>Money Owed</p></th></tr>'
        b'</thead><tbody>'
        b'<tr><td><p>Adam Alpha</p></td><td><p>100</p></td></tr>'
        b'</tbody></table>'
        b'<table cellpadding="0" cellspacing="0" id="my-table">'
        b'<thead><tr><th><p>Number</p></th><th><p>Two</p></th></tr>'
        b'</thead><tbody>'
        b'<tr><td><p>Adam Alpha</p></td><td><p>100</p></td></tr>'
        b'</tbody></table>'
        b'</div></div>'
        b'<script type="text/javascript" src="js/impress.js"></script>'
        b'<script type="text/javascript" src="js/hovercraft-minimal.js">'
        b'</script></body></html>'
    ),

    'slide_with_class': (
        b'<!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml">'
        b'<body><div id="impress">'
        b'<div class="step step-level-1 something-else" step="0" data-rotate-x="0" '
        b'data-rotate-y="0" data-rotate-z="0" data-scale="1" data-x="0" '
        b'data-y="0" data-z="0">'
        b'<p>This is some text</p></div></div>'
        b'<script type="text/javascript" src="js/impress.js"></script>'
        b'<script type="text/javascript" src="js/hovercraft-minimal.js">'
        b'</script></body></html>'
    ),

    'container_directive': (
        b'<!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml"><body>'
        b'<div id="impress"><div class="step step-level-1" step="0" '
        b'data-rotate-x="0" data-rotate-y="0" data-rotate-z="0" data-scale="1" '
        b'data-x="0" data-y="0" data-z="0"><div class="my-class"><p>This is '
        b'some text in the container</p></div><div id="my-thing"><p>This '
        b'should have an id</p></div></div></div><script '
        b'type="text/javascript" src="js/impress.js"></script><script '
        b'type="text/javascript" src="js/hovercraft-minimal.js"></script>'
        b'</body></html>'
    ),

    'class_directive': (
        b'<!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml">'
        b'<body><div id="impress"><div class="step step-level-1" step="0" '
        b'data-rotate-x="0" data-rotate-y="0" data-rotate-z="0" data-scale="1" '
        b'data-x="0" data-y="0" data-z="0"><p class="my-class">This is '
        b'some text in the class</p></div></div><script '
        b'type="text/javascript" src="js/impress.js"></script><script '
        b'type="text/javascript" src="js/hovercraft-minimal.js"></script>'
        b'</body></html>'
    ),

    'comment': (
        b'<!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml">'
        b'<body><div id="impress"><div class="step step-level-1" step="0" '
        b'data-rotate-x="0" data-rotate-y="0" data-rotate-z="0" data-scale="1" '
        b'data-x="0" data-y="0" data-z="0">'
        b'<p>This text should appear.</p></div></div>'
        b'<script type="text/javascript" src="js/impress.js"></script>'
        b'<script type="text/javascript" src="js/hovercraft-minimal.js">'
        b'</script></body></html>'
    )
}

