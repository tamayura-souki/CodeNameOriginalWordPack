import glob

word_pack_root = "words"
word_pack_ext = ".owp"
word_pack_output_path = "wordpack.txt"

word_pack_root = word_pack_root.strip().rstrip('/\\')
word_pack_ext = word_pack_ext.strip().replace('.', '')
search_path = f"{word_pack_root}/**/*.{word_pack_ext}"
word_pack_paths = glob.glob(search_path, recursive=True)

print(f"found {len(word_pack_paths)} owp files.")

def txt_load(text_file_path: str) -> str:
    with open(text_file_path, 'r', encoding='utf-8') as f:
        return f.read()

def txt_save(text_file_path: str, write_text: str) -> None:
    with open(text_file_path, 'w', encoding='utf-8') as f:
        f.write(write_text)

word_list = set()
for wp_path in word_pack_paths:
    wp_lines = txt_load(wp_path).split("\n")
    raw_words = filter(lambda w: w and w[0] != "#", wp_lines)
    striped_words = map(lambda w: w.strip(), raw_words)
    normalized_words = set(filter(lambda w: w, striped_words))

    word_list |= normalized_words

print(f"got {len(word_list)} words.")

txt_save(word_pack_output_path, '\n'.join(word_list))