[](italizing_texts_in_markdown)

You can italisize a word, words, or texts by encircling them with underscore(_).

_This is italizied texts_

This is partially _italisized_ texts.

---
[](bolding_texts_in_markdown)

You can bold a word, words, or texts by encircling them with two asterisk marks.

**This is bolded texts.**

This is partially **bolded** texts.

---
[](strike_through_texts_in_markdown)

You can strike through a word, words, or texts by encircling them with two tilda (~).

~~This is struck through texts.~~

This is partially ~~struck through~~ texts.

---
[](creating_headings_in_markdown)

You can create from H1 to H6 headings by applying the relevant amount of hashtag signs before texts.

# This is H1 heading
## This is H2 heading
### This is H3 heading
#### This is H4 heading
##### This is H5 heading
###### This is H6 heading

You can also create H1 heading by applying three equal signs(===) beneath texts.

This is H1 heading created by three equal signs.
===

---
[](underling_texts_in_markdown)

You can underline texts by applying three minus signs(---) beneath texts with one newline.

This is underscored texts.

---

### This is H3 heading with underline
---
[](creating_blockquote_in_markdown)

You can create blockquotes by applying greater than sign(>) before texts you want to put in blockquotes.

Ayn Rand says:
> Do not let your fire go out, spark by irreplaceable spark in the hopeless swamps of the not-quite, the not-yet, and the not-at-all. Do not let the hero in your soul perish in lonely frustration for the life you deserved and have never been able to reach. The world you desire can be won. It exists.. it is real.. it is possible.. it's yours

---
[](creating_external_links_in_markdown)

You can create external links by encircling the name of link with square bracket([]) followed by colon() and url.

[Goole]: https://wwww.yahoo.com

[Goole]

---
[](creating_internal_links_in_markdown)

You can create internal links to specified headings by encircling the name of links with square bracket([]) followed by hashtag and the name of headings encircled in bracket(()).

## Table of Contents
[Chapter 1](#chapter-1)

[Chapter 2](#chapter-2)

[Chapter 3](#chapter-3)

[Chapter 4](#chapter-4)

### Chapter 1
Tempor sit dolor justo no accusam. Lorem diam labore sadipscing amet et sea dolores labore accusam, tempor accusam voluptua diam kasd aliquyam. Sit et duo tempor lorem ea sadipscing. Ipsum dolores stet et elitr sit aliquyam sanctus. Et dolor invidunt aliquyam erat. Accusam ut sanctus ut et no. Vero est sea eirmod sanctus et gubergren ipsum rebum, eirmod magna erat eos dolore dolor eirmod consetetur est tempor. Nonumy et ea sanctus amet amet vero lorem dolor, lorem et et justo takimata amet. Takimata ipsum diam dolores et dolor gubergren. Vero voluptua aliquyam lorem rebum, consetetur lorem et et rebum stet..

[Return to Table of Contents](#table-of-contents)

### Chapter 2
Et est diam nonumy ea magna justo et erat, dolore sadipscing sed et ipsum. Takimata magna ut amet sit dolores et vero diam accusam, dolor amet lorem tempor nonumy et aliquyam est diam consetetur, clita gubergren rebum ut est, sadipscing rebum dolor no ipsum at. Magna sit sea accusam dolor voluptua ipsum. Sea sea magna takimata at sed sit, rebum labore sed et voluptua sed et ut, sadipscing ipsum rebum gubergren elitr et. Gubergren erat voluptua voluptua sed invidunt labore et dolor accusam, amet tempor et duo takimata gubergren lorem. Diam no est at et sit eirmod. Sanctus amet eirmod.

[Return to Table of Contents](#table-of-contents)
### Chapter 3
Et kasd ipsum lorem amet elitr diam sit. Ea elitr amet dolores sed elitr. Clita sea ea dolor aliquyam no et, dolor sit dolor voluptua amet ea et, at ea sea diam dolor amet ea dolor sed, sadipscing sed at at dolores et ea. Et consetetur diam vero lorem gubergren est. Eirmod sit sit rebum ipsum aliquyam. Duo sed et consetetur nonumy elitr sed voluptua. Eos kasd diam stet sed ipsum magna eos diam, dolor clita nonumy elitr lorem ut vero at rebum et, gubergren accusam vero dolor rebum lorem, diam labore no sit erat diam dolore ut. Stet gubergren.

[Return to Table of Contents](#table-of-contents)
### Chapter 4
Elitr et ipsum invidunt invidunt erat sit lorem labore. Rebum duo sit sit dolor gubergren tempor et diam, sadipscing labore dolor et ea consetetur dolore, et dolor amet rebum sed eos stet et ipsum. Gubergren magna diam clita sit takimata sit gubergren nonumy sanctus, labore sanctus lorem rebum sit. Voluptua sadipscing dolores et sea accusam diam. Sed nonumy consetetur lorem et magna. Justo stet dolores gubergren sed voluptua, eirmod sanctus justo kasd nonumy tempor kasd sea eos erat, sadipscing erat elitr magna no et tempor rebum dolor. Et et ipsum et voluptua sanctus kasd lorem est invidunt, et invidunt labore.

[Return to Table of Contents](#table-of-contents)

---
[](creating_lists_in_markdown)

You can create unordered lists by applying plus(+), minus(-), or asterisk(*)marks before texts.

- Banana
You can also create sub-lists by tab and the aforementioned signs.
  + Taiwan
  * Peru
  - Panama
+ Tacos
* Red Chili

You can create orded lists by applying number with period sign(.) with once space and texts.

1. Toyota
2. Honda
3. Nissan

---
[](inserting_images_in_markdown)
You can insert images by encircling the name of links with bracket ([]) with exclamation mark before it followed by the path to the image in bracket(().)

![me](me_with_glasses.jpg)


You can create link to the image by encircling the name of link with square bracket([]) followed by colon (:) and the path to the image.

[with_glasses]: me_with_glasses_2.jpg

![about_me][with_glasses]

You can also create external link by encircling with square bracket([]) followed by url in bracket(()).

[![about_me][with_glasses]](https://www.yahoo.com)

---

[](inline_coding_in_markdown)

You can highligh a word, words, or texts by encircling them with tilda(``).

`This is highlight.`

To move directly, you need to follow the following steps:

`$ cd \path\to\file`

---

[](creating_code_block_in_markdown)

You can create a code block by encircling certain parts with three backticks(```)

You can also use some color code by specifying what languages you are using right after the initial three backticks.

Take a look this JavaScrit function:

```javascript

function add(x, y){
  return x + y;
}

```

```python

def hello(name):
  print(f"Hello, {name}!")

```

```java

public static void main(String[]args){
  Sytem.out.println("hello");
}
```
---
