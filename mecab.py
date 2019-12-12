from wordcloud import WordCloud
import MeCab
import sys


def get_words(file):
    data = open(file, "r")
    mecab = MeCab.Tagger("-Ochasen")
    words = []
    for line in data:
        node = mecab.parseToNode(line)
        while node:
            if node.feature.split(",")[0] in ["名詞"]:
                words.append(node.surface)
            node = node.next
            if node is None:
                break

    return words


def generate_word_cloud(text):
    # 適宜変更する
    font_path = "/Library/Fonts/ipaexg.ttf"
    stop_words = [
        "もの", "自分", "みんな", "会社", "こと", "よう", "がち",
        "ため", "そう", "感じ", "これ", "ところ", "さん", "それ", "そこ",
        "素敵", "メンバー", "チーム", "取り組み", "すてき"
    ]

    word_cloud = WordCloud(
        background_color="white",
        font_path=font_path,
        stopwords=set(stop_words),
        width=900,
        height=500
    ).generate(text)
    word_cloud.to_file("./output/word_cloud.png")


def main():
    args = sys.argv
    words = get_words("./input/" + args[1] + ".txt")
    generate_word_cloud(text=' '.join(words))


if __name__ == "__main__":
    main()
