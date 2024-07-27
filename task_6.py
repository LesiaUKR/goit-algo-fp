items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_calories = 0
    selected_items = []

    for item, values in sorted_items:
        if budget >= values['cost']:
            budget -= values['cost']
            total_calories += values['calories']
            selected_items.append(item)

    return selected_items, total_calories

def dynamic_programming(items, budget):
    n = len(items)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    item_list = list(items.items())

    for i in range(1, n + 1):
        for w in range(budget + 1):
            item_name, item_values = item_list[i - 1]
            if item_values['cost'] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - item_values['cost']] + item_values['calories'])
            else:
                dp[i][w] = dp[i - 1][w]

    w = budget
    selected_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item_name, item_values = item_list[i - 1]
            selected_items.append(item_name)
            w -= item_values['cost']

    total_calories = dp[n][budget]
    return selected_items, total_calories

budget = 100
selected_items_greedy, total_calories_greedy = greedy_algorithm(items, budget)
print(f"Жадібний алгоритм: Вибрані страви: {selected_items_greedy}, Загальна калорійність: {total_calories_greedy}")

selected_items_dp, total_calories_dp = dynamic_programming(items, budget)
print(f"Динамічне програмування: Вибрані страви: {selected_items_dp}, Загальна калорійність: {total_calories_dp}")
