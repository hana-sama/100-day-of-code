[](bolding_texts_in_markdown)

You can bold texts by applying two asterisk marks before and after specific texts or words.

**This is bolded texts**

You can also bold texts or words inline.

This is **bolded** texts.

---
[](italisizing_texts_in_markdown)

You can italisize texts or words by applying underscore symbol(_) before and after specific texts or words.

_This is italisized texts_

You can also italisize specific texts inline.

This is _italisized_ texts.

---

[](creating_blockquotes_in_markdown)

You can create blockquotes by applying greater than sign(>)before texts.

Ayn Rand says:

> The government was set to protect man from criminals-and the constitution was written to protect man from the government. The Bill of Rights was not directed at private citizens, but against the government-as an explicit declaration that individual rights supersede any public or social power.

---
[](creating_headings_in_markdown)

You can create H1 to H6 headings by applying relevant amount of hashtag symbol(#) before texts.

# This is H1 heading
## This is H2 heading
### This is H3 heading
#### This is H4 heading
##### This is H5 heading
###### This is H6 heading

---
You can also create H1 heading by applying three equal symbol(===) before texts.

This is H1 heading appied by three equal symbols.
===

You can also apply three minus symbols(---) before texts to add horizontal rule.

## This is H2 headings with underline.
---

This is regular texts with underline.

---

[](creating_lists_in_markdown)

You can create unordered lists by applying plus(+), asterisk(*), or minus(-) sign before texts.

- Banana
You can also create sub-lists by applying tab and the above mentioned symbols but better to use different symbols used in top-lists for clarity sake.
  * Peru
  - Taiwan
  + Egypt
+ Potato
* Chips

---
[](creating_external_links_in_markdown)

You can create external links by specifying names in square bracket([]) followed by colon(:) and url.

[Google]: https://www.yahoo.com

[Google]

---
[](creating_internal_links_in_markdown)

You can create internal links by names in square bracket([]) followed by path in bracket.

## Table of Contents
---
[Chapter 1](#chapter-1)

[Chapter 2](#chapter-2)

[Chapter 3](#chapter-3)

[Chapter 4](#chapter-4)

---
### Chapter 1
[Return to TOC](#table-of-contents)
### Chapter 2
[Return to TOC](#table-of-contents)
### Chapter 3
[Return to TOC](#table-of-contents)
### Chapter 4
[Return to TOC](#table-of-contents)

[](inserting_image_in_markdown)

You can insert image by applying exclamation mark(!) followed by square bracket([]) with the name of your choice in it and bracket(()) with the path to image local or online.

![about_me](me_with_glasses.jpg)

You can also create short-cut to certain images by specifying name of your choice in square bracket([]) followed by colon(:) and url or path to the image and use them in other part of markdown file.

[glasses]: me_with_glasses_2.jpg

![me][glasses]

You can also add external link by encircling formatted image code with square bracket([]) and url in bracket(()).

[![me][glasses]](https://www.yahoo.com)

---
[](creating_tables_in_markdown)

You can create tables by using pipe symbol(|)

|   Model    |    Year    |   Brand   |
|------------|------------|-----------|
|   Prius    |    2000    |   Toyota  |
|   Accord   |    2010    |   Honda   |
|   Note     |    1985    |   Nissan  |

Tables in markdown is left-centered unless specified otherwise by adding colon(:) in the separator.

|   Model    |    Year    |   Brand   |
|:----------:|:----------:|:---------:|
|   Prius    |    2000    |   Toyota  |
|   Accord   |    2010    |   Honda   |
|   Note     |    1985    |   Nissan  |

|   Model    |    Year    |   Brand   |
|-----------:|-----------:|----------:|
|   Prius    |    2000    |   Toyota  |
|   Accord   |    2010    |   Honda   |
|   Note     |    1985    |   Nissan  |

---

[](inline_code_in_markdown)

You can highlight by encircling a word or texts with backtick(``).

In order to remove the files for the **/tmp** then run the : 

`$ rm -rf /tmp* `

`$ touch /tmp/something.txt`

`$ cat /tmp/something.txt | grep "tacos"`

