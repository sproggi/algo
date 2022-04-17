def sleight_of_hand(amount_key, play_field):
    play_list = []
    for i in play_field:
        play_list += i
    cnt = 0
    for j in '123456789':
        if play_list.count(j)/2 <= amount_key and play_list.count(j) != 0:
            cnt += 1
    return cnt


if __name__ == "__main__":
    amount_key = int(input())
    play_field = [list(input()) for _ in range(4)]
    result = sleight_of_hand(amount_key, play_field)
    print(result)
