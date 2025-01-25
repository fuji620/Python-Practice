def fibnn(n):   # 関数の名前は "fib"、引数は "n"
    if n == 0:
        return 0  # 0番目のフィボナッチ数
    elif n == 1:
        return 1  # 1番目のフィボナッチ数
    else:
        return fibnn(n-1) + fibnn(n-2)  # 再び fib 関数を呼び出す
print(fibnn(32))  # 出力: 5
