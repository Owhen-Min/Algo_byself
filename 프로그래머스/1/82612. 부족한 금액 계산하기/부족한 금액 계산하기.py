def solution(price, money, count):
    t_price = (count+1)*count/2 * price

    return max(t_price - money, 0)