---
title: The Language Transliteration Project
emoji: 🔡
colorFrom: indigo
colorTo: gray
sdk: streamlit
sdk_version: 1.25.0
app_file: app.py
pinned: false
license: cc
---
Use this application on HuggingFace🤗 :- https://huggingface.co/spaces/DebasishDhal99/The-Language-Transliteration-Project

Blog discussing the results :- https://medium.com/@debasishdhaldd99/simplifying-language-through-python-aae6ee7113d9

This space is aimed at helping people with getting familiarized with Polish, Turkish, Hungarian, Serbo-Croatian-Bosniak (both Latin and Cyrillic based) and Romanian spelling system. 

**Why?**

The languages mentioned above, use a modified Latin script with a lot of diacritic marks and digraphs, thus often making them difficult for non-native speakers to pronounce or read the words 
properly. This space offers simplified spelling of words/sentence in the said languages. More languages are on the pipeline.

For example, the Polish word Jarosław, an English speaker who isn't familiar with Polish orthography will pronounce it as Jaroslav, while its actual Polish pronunciation 
is Yaroswav. Similary, the city of Przemyśl should be pronounced as Pzhemyshl, even though its not evident to an English speaker.

The approach for transliterating Polish language taken in this space is converting Polish character combinations to Cyrillic equivalents, which are single characters, thus 
simplifying our task greately.

Features added as of now:- 
-    Polish, Turkish, Hungarian, Serbo-Croatian-Bosnian, Romanian language added.
-    Option for the user to choose any of the 3-4 examples available and pass it as input to the model.
-    Option for the user to generate a random but coherent sentence and pass it as input to the model. Acts as a nice playground for the user.

# Results in brief
For each language, some names/placenames in that language were given to this web app as input, the simplified outputs are presented below. 

## Polish 
Polish spelling => Simplified form

- Wojciech Szczęsny => Voytsiekh Shensny (Polish footballer)
- Grzegorz Krychowiak => Gzhegozh Krykhoviak (zh is pronounced like the "s" in measure/vision) (Polish footballer)
- Łódź => Wuj (Major Polish city)
- Rzeszow => Zheshov (Polish city near Ukraine)

## Hungarian
Hungarian spelling => Simplified form

- Dominik Szoboszlai => Dominik Soboslai (Hungarian footballer)
- Budapest => Budapesht (Hungarian capital)
- Debrecen => Debretsen (Major Hungarian city)
- Pozsony => Pozhony (Hungarian name for Bratislava)

## Turkish
Turkish spelling => Simplified form

- Azerbaycan => Azerbayjan
- Türkiye => Tyurkiye
- Recep Tayyip Erdoğan => Rejep Tayyip Erdo’an (Turkish president)
- Barış Alper Yılmaz => Baresh Alper Yelmaz (Turkish footballer)

## Serbo-Croatian-Bosnian
Serbo-Croatian-Bosnian spelling => Simplified form

- Novak Đoković => Novak Jokovich (No introduction needed)
- Karadžić => Karajich (Serbain war criminal)
- Edin Džeko => Edin Jeko (Bosnian Footballer)
- Artiljerija => Artilyeriya (Artillery)

## Romanian
Romanian spelling => Simplified form

- Cluj-Napoca => Kluzh Napoka (A city in Romanian Translyvania)
- București => Bukureshti (Bucharest)
- Angela Gheorghiu => Anjela Georgiu (Romanian singer)
- Constantin Brâncuși => Konstantin Brunkushi (Romanian Sculptor)


*************************************************************************************************
Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
