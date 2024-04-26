import argparse

if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    # required argument 
    parser.add_argument("test", help="can enter any thing just test")
    # option argument have "--" in front of variable name
    parser.add_argument("--physics", help="enter physics scores")
    parser.add_argument("--chemistry", help="enter --chemistry scores")
    parser.add_argument("--maths", help="enter maths scores")
    # add scope of argument
    parser.add_argument("--dislike", help="enter dislike subject", choices=["physics","chemistry","maths"])
    
    # all args is a string
    args = parser.parse_args()
    
    subject = dict(args._get_kwargs())
    subject.pop("test")
    subject.pop("dislike")
    
    total = 0
    count = 0
    for key in subject :
        try :
            total += int(subject[key])
            count += 1
        except TypeError as valErr :
            total += 0
            
    print("{:.2f}".format(total / count))