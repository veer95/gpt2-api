


from gpt import get_prediction

if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--post", help="A Sentence to complete", default="example_article")

    args = parser.parse_args()

    post = args.post
    # phrase = ''
    input_text = "%s "%post
    comment = get_prediction(input_text)
    def t(comment):
        for i in ["#","@","(",")",":","-",".com","link","wife","girl","woman",'/', 'reddit']:
            if i in comment:
                return False
        return True
    while True:
        if t(comment):
            break
        else:
            comment = get_prediction(input_text)

    print(comment)