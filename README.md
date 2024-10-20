This is a simple Python script I implemented that is able to compress and uncompress files
A sample text file is provided to test it out. 

-- COMMAND TO COMPRESS FILE --
 - python3 main.py [file-name].txt --z
output -> [file-name]/tree.txt
          [file-name]/data.bin

-- COMMAND TO UNCOMPRESS FILE --
 - python3 main.py [file-name] --u
output -> [file-name]_copy.txt

tree.py:
- Tree data structure used for Huffman Encoding Algorithm

zip.py:
- Huffman Encodes the data from the provided text file.
- Creates a new directory with the same name as the text file.
- The new directory contains a .bin file containing the encoded data from the text file and a tree.txt file that stores the encoding tree that will be used when uncompressing the file

unzip.py
- Takes the directory containing the tree.txt and .bin files
- Rebuilds the Huffman Encoding tree from the tree.txt file
- Decodes the .bin and writes the restored content into a new text file labeled after original with _copy tag.