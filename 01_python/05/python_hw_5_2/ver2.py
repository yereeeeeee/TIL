def count_character(word, char):
    result = 0 # 해당하는 알파벳이 나올 때 마다 1 씩 증가
    # 전체 순회
    for text in word:
        # 순회해서 얻은 text 변수에 든 값이
        # char 매게 변수에 들어 있는 값과 일치하다면
        if text == char:
            # result에 담긴 값이 1씩 증가해야 한다.
            result += 1

    # 전체 순회를 완료했다. -> 모든 상황에 대한 조사가 끝났다.
    return result

result = count_character("Hello, World!", "o")
print(result)  # 2