# loading the german corpus
from ebooklib import epub
import ebooklib
import os
import nltk
import argparse
import glob

def main(epub_directory):
  fantasy_corpus = []
  book_corpus = glob.glob(epub_directory + '/*.epub')
  for book_name in book_corpus:
    book = epub.read_epub(book_name)
    for doc in book.get_items():
        doc_content = str(doc.content)
        for w in nltk.word_tokenize(doc_content):
            fantasy_corpus.append(w.lower())
        
if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("epub_directory", help="Directory with epub books.")
  args = parser.parse_args()
    
  main(args.epub_directory)
